# Arabic Voice Chatbot

## Overview

This project is an Arabic voice chatbot developed using Python. It records the user's voice, converts speech to text using OpenAI Whisper, generates a response using Cohere AI, and converts the generated response back into speech.

## Features

- Record voice from the microphone.
- Convert speech to text using Whisper.
- Generate intelligent responses using Cohere AI.
- Convert text responses into speech.
- Simple command-line interface.

## Technologies Used

- Python 3.11
- OpenAI Whisper
- Cohere API
- gTTS
- Pygame
- SoundDevice
- NumPy
- SciPy
- python-dotenv

## Project Structure

```
voice_chatbot_task/
│── main.py
│── requirements.txt
│── README.md
│── .gitignore
│── .env.example
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Ahmed-AlBakhat/voice-chatbot-task.git
cd voice-chatbot-task
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows**

```bash
.venv\Scripts\activate
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Install FFmpeg

Whisper requires FFmpeg to process audio files.

Verify the installation:

```bash
ffmpeg -version
```

### 5. Configure the API Key

Create a `.env` file and add your Cohere API key:

```env
COHERE_API_KEY=YOUR_API_KEY
```

## Running the Project

```bash
python main.py
```

After the program starts:

1. Press **Enter** to begin recording.
2. Speak for approximately 8 seconds.
3. The application will:
   - Convert your speech to text.
   - Generate an AI response.
   - Convert the response into speech.

To exit the program, type:

```text
q
```

and press **Enter**.

## Workflow

```
Microphone
      │
      ▼
Speech Recording
      │
      ▼
OpenAI Whisper
(Speech-to-Text)
      │
      ▼
Cohere AI
(Response Generation)
      │
      ▼
Text-to-Speech
      │
      ▼
Audio Response
```

## Notes

- An internet connection is required for Cohere and gTTS.
- FFmpeg must be installed before running Whisper.
- Do not upload your `.env` file because it contains your private API key.

## Author

Ahmed AlBakhat
