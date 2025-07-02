# Projet_Ultron - Assistant Vocal Autonome (Projet IA)

## Description

Ce projet est un assistant vocal personnel et agent autonome conçu pour :

- Ecouter vos commandes vocales (multilingue) et activer un mot‑clé (wake word)
- Transcrire la voix en texte via OpenAI Whisper
- Répondre oralement avec une voix clonée (celle de l’acteur anglais d’Ultron)
- Lancer des applications ou scripts sur votre PC (via `pyautogui`, `subprocess`)
- Effectuer des recherches sur internet
- Envoyer et rédiger des mails automatiquement
- Vous apprendre le piano ou la guitare (guidage interactif)
- Converser avec vous en plusieurs langues

## Objectifs

1. **Reconnaissance vocale** multilingue
2. **Synthèse vocale** personnalisée
3. **Contrôle du PC et automatisation**
4. **Agent autonome** (via LangChain ou Auto‑GPT)
5. **Gestion des mails**
6. **Modules pédagogiques pour instruments**
7. **Interface multilingue**

## Technologies & Outils

| Fonctionnalité        | Outils recommandés                                                                                                                                       |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reconnaissance vocale | OpenAI Whisper, SpeechRecognition, Porcupine (wake word)                                                                                               |
| Synthèse vocale       | Coqui TTS (clonage voix Ultron), playsound                                                                                                               |
| Contrôle PC           | pyautogui, subprocess, webbrowser, selenium                                                                                                              |
| Agent autonome        | LangChain, Auto‑GPT                                                                                                                                     |
| Mails                 | `smtplib`, `imaplib`                                                                                                                                   |
| Apprentissage musical | Pitch detection (aubio/pyaudio), API MuseScore/YouTube                                                                                                  |
| Multilingue           | Whisper + GPT multilingue + TTS multilingue                                                                                                             |

## Structure du projet

## Structure du projet

```bash
assistant-ia/
├── data/
│   └── (enregistrements, modèles)
├── modules/
│   ├── recognition.py        # capture et transcription
│   ├── tts.py                # synthèse vocale clonée
│   ├── control.py            # contrôle PC
│   ├── autonomy.py           # agent autonome
│   ├── email.py              # envoi/réception mail
│   └── music.py              # cours piano/guitare
├── main.py                   # point d'entrée
├── requirements.txt          # dépendances Python
├── README.md                 # ce document
└── LICENSE.txt               # licence propriétaire
```



## Installation

1. Cloner le dépôt :
   ```bash
   git clone https://github.com/votreProfil/assistant-ia.git
   cd assistant-ia
2. Créer un environnement virtuel :
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # ou `venv\Scripts\activate` sous Windows
3. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
4. Préparer vos modèles (Whisper, TTS, outils d’autonomie).


## Utilisation

Exécutez l’assistant :
   ```bash
   python main.py
   ```

Activez le wake word, puis commandez vocalement :

« Ultron, ouvre Spotify »
« Ultron, envoie un mail à Paul »

L’assistant répond avec la voix d’Ultron, exécute la commande, et peut initier un cours de guitare ou piano.

## ℹ️ Contributions
Ce projet est sous licence propriétaire (voir LICENSE.txt). Toute utilisation, modification ou distribution nécessite mon accord écrit et une mention claire :

Développé par Sainth-Nathan AHOUSSI – [Github](https://github.com/sainth-nathan-ahoussi)


## 📧 Contact

Pour toute question, autorisation, ou collaboration :
Sainth-Nathan AHOUSSI – nathanahoussi502@gmail.com
sainth-nathan.fr
