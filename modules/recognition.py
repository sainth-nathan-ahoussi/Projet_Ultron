import pvporcupine
import pvrecorder
import webrtcvad
import whisper
import numpy as np

# 🔧 Paramètres audio/VAD
ACCESS_KEY = "rl8LPZ9jn5tEK1vxdwH+l7fbqFYRVq4fsi9NoRjwWLNcRKh1MY+W1Q=="
WAKE_PPN = "ultron_en_windows_v3_0_0.ppn"
SAMPLE_RATE = 16000
FRAME_MS = 30  # durée en ms (valide: 10, 20, 30)
FRAME_LEN = int(SAMPLE_RATE * FRAME_MS / 1000)  # samples/frame (480)
MAX_SILENCE = int(2000 / FRAME_MS)  # ~1 seconde de silence

def detect_wake():
    porcupine = pvporcupine.create(access_key=ACCESS_KEY, keyword_paths=[WAKE_PPN])
    rec = pvrecorder.PvRecorder(device_index=-1, frame_length=porcupine.frame_length)
    rec.start()
    print("👉 En attente du wake word…")
    while True:
        pcm = rec.read()
        if porcupine.process(pcm) >= 0:
            print("✅ Wake word détecté !")
            return rec, porcupine

def record_until_silence(rec):
    vad = webrtcvad.Vad(2)
    rec = pvrecorder.PvRecorder(device_index=-1, frame_length=FRAME_LEN)
    frames = []
    silence_frames = 0
    print("🎤 Enregistrement en cours…")
    rec.start()
    while True:
        pcm = rec.read()  # liste d’entiers length=480
        pcm_bytes = np.array(pcm, dtype=np.int16).tobytes()
        if vad.is_speech(pcm_bytes, SAMPLE_RATE):
            frames.append(pcm)
            silence_frames = 0
        elif frames:
            silence_frames += 1
            if silence_frames > MAX_SILENCE:
                break

    rec.stop()
    audio = np.concatenate(frames).astype(np.int16) / 32768.0
    return audio.astype(np.float32)

def main():
    model = whisper.load_model("base")
    try:
        while True:
            rec, porcupine = detect_wake()
            audio = record_until_silence(rec)
            audio = audio.astype(np.float32)
            text = model.transcribe(audio, language="fr")["text"]
            print("🗣 Transcription :", text)
            porcupine.delete()
            rec.delete()
    except KeyboardInterrupt:
        print("Arrêt du programme.")

if __name__ == "__main__":
    main()
