import os
import sys
import time
from pathlib import Path

import cohere
import numpy as np
import pygame
import sounddevice as sd
import whisper
from dotenv import load_dotenv
from gtts import gTTS
from scipy.io.wavfile import write


SAMPLE_RATE = 16_000
RECORD_SECONDS = 8
AUDIO_FILE = Path("user_audio.wav")
RESPONSE_FILE = Path("response.mp3")
WHISPER_MODEL = "base"
COHERE_MODEL = "command-r7b-arabic-02-2025"


def record_audio(filename: Path, duration: int = RECORD_SECONDS) -> None:
    """Record audio from the default microphone and save it as a WAV file."""
    print(f"\n🎙️ تكلم الآن... التسجيل لمدة {duration} ثوانٍ.")
    audio = sd.rec(
        int(duration * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32",
    )
    sd.wait()

    # Convert float audio (-1.0 to 1.0) to signed 16-bit PCM.
    audio_int16 = np.int16(np.clip(audio, -1.0, 1.0) * 32767)
    write(filename, SAMPLE_RATE, audio_int16)
    print("✅ انتهى التسجيل.")


def transcribe_audio(model: whisper.Whisper, filename: Path) -> str:
    """Convert recorded speech to text using local Whisper."""
    print("📝 جاري تحويل الصوت إلى نص...")
    result = model.transcribe(str(filename), language="ar", fp16=False)
    text = result.get("text", "").strip()

    if not text:
        raise RuntimeError("لم يتم التعرف على كلام واضح. حاول مرة أخرى بصوت أعلى.")

    print(f"أنت: {text}")
    return text


def generate_response(client: cohere.ClientV2, user_text: str) -> str:
    """Generate an Arabic response using Cohere Chat API."""
    print("🤖 جاري توليد الرد...")

    response = client.chat(
        model=COHERE_MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "أنت مساعد عربي مفيد. أجب بالعربية بشكل واضح ومختصر، "
                    "ولا تستخدم الإنجليزية إلا عند الحاجة."
                ),
            },
            {"role": "user", "content": user_text},
        ],
    )

    content = response.message.content
    if not content:
        raise RuntimeError("لم يُرجع النموذج أي رد.")

    answer = content[0].text.strip()
    print(f"المساعد: {answer}")
    return answer


def text_to_speech(text: str, filename: Path) -> None:
    """Convert Arabic text to an MP3 file using gTTS."""
    print("🔊 جاري تحويل الرد إلى صوت...")
    tts = gTTS(text=text, lang="ar", slow=False)
    tts.save(str(filename))


def play_audio(filename: Path) -> None:
    """Play the generated MP3 file."""
    pygame.mixer.init()
    pygame.mixer.music.load(str(filename))
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.music.unload()
    pygame.mixer.quit()


def clean_temp_files() -> None:
    """Delete temporary audio files."""
    for file in (AUDIO_FILE, RESPONSE_FILE):
        try:
            if file.exists():
                file.unlink()
        except PermissionError:
            pass


def main() -> None:
    load_dotenv()

    api_key = os.getenv("COHERE_API_KEY")
    if not api_key:
        print(
            "❌ لم يتم العثور على COHERE_API_KEY.\n"
            "أنشئ ملف .env واكتب داخله:\n"
            "COHERE_API_KEY=ضع_المفتاح_هنا"
        )
        sys.exit(1)

    print("⏳ جاري تحميل نموذج Whisper لأول مرة...")
    whisper_model = whisper.load_model(WHISPER_MODEL)
    cohere_client = cohere.ClientV2(api_key=api_key)

    print("\n✅ المساعد الصوتي جاهز.")
    print("اضغط Enter لبدء التسجيل، أو اكتب q ثم Enter للخروج.")

    try:
        while True:
            command = input("\n> ").strip().lower()
            if command == "q":
                print("إلى اللقاء 👋")
                break

            try:
                record_audio(AUDIO_FILE)
                user_text = transcribe_audio(whisper_model, AUDIO_FILE)
                answer = generate_response(cohere_client, user_text)
                text_to_speech(answer, RESPONSE_FILE)
                play_audio(RESPONSE_FILE)

            except KeyboardInterrupt:
                print("\nتم إيقاف العملية.")
                break
            except Exception as error:
                print(f"❌ حدث خطأ: {error}")
            finally:
                clean_temp_files()

    finally:
        clean_temp_files()


if __name__ == "__main__":
    main()
