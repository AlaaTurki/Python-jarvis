# Python Jarvis

A simple voice assistant built in Python with speech recognition, text-to-speech, translation, and chat capabilities.

## Features

- Voice input using `SpeechRecognition`
- Speech output using `pyttsx3`
- Web search and opening Chrome browser
- Text translation using `googletrans`
- Chatbot responses using `chatterbot`
- Configurable assistant names via environment variables

## Requirements

- Python 3.9+
- Windows (uses `sapi5` voice engine)

## Installation

1. Create and activate a Python virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with the following values:

```env
username=YourName
botname=Jarvis
```

## Usage

Run the assistant from the project directory:

```bash
python main.py
```

Speak commands such as:

- `open chrome`
- `search for <query>`
- `translate <text>`
- `let's chat`

## Project files

- `main.py` — main voice assistant loop and command handling
- `dialogue_manager.py` — chatbot integration and response generation
- `tools.py` — helper functions for browser actions and translation
- `requirements.txt` — Python package dependencies

## Notes

- The assistant uses the default microphone configured on the system.
- Translation requires an internet connection for `googletrans`.
- `chatterbot` training may take a few moments on first run.
