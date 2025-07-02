import pvporcupine, pvrecorder

def detect_wake_word(access_key: str = "rl8LPZ9jn5tEK1vxdwH+l7fbqFYRVq4fsi9NoRjwWLNcRKh1MY+W1Q==", model_path=None, keyword_path=None):
    porcupine = pvporcupine.create(
        access_key=access_key,
        keyword_paths=[keyword_path]  # ou keywords=[...] pour wake words intégrés
    )
    recorder = pvrecorder.PvRecorder(device_index=-1, frame_length=porcupine.frame_length)
    recorder.start()
    return porcupine, recorder

class WakeDetector:
    def __init__(self, porcupine, recorder):
        self.porcupine = porcupine
        self.rec = recorder

    def wait_for_wake(self):
        print("En attente du wake word...")
        while True:
            pcm = self.rec.read()
            if self.porcupine.process(pcm) >= 0:
                return

    def close(self):
        self.rec.stop()
        self.porcupine.delete()
        self.rec.delete()
