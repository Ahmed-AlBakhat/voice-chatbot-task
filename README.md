# Arabic Voice Chatbot

مشروع يحول كلام المستخدم إلى نص، ثم يولّد ردًا باستخدام نموذج لغوي، وبعد ذلك يحول الرد إلى صوت.

## فكرة المشروع

يمر البرنامج بثلاث مراحل:

1. تسجيل صوت المستخدم من الميكروفون.
2. تحويل الصوت إلى نص باستخدام Whisper.
3. إرسال النص إلى Cohere لتوليد رد.
4. تحويل الرد النصي إلى صوت عربي باستخدام gTTS.
5. تشغيل الرد الصوتي للمستخدم.

## الأدوات المستخدمة

- Python
- OpenAI Whisper
- Cohere Chat API
- gTTS
- SoundDevice
- Pygame

## ملفات المشروع

```text
voice_chatbot_task/
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## 1. تثبيت Python

يفضل استخدام Python 3.11 لتقليل مشكلات التوافق.

تأكد من التثبيت:

```powershell
py -3.11 --version
```

## 2. فتح مجلد المشروع

```powershell
cd "مسار\voice_chatbot_task"
```

مثال:

```powershell
cd "$HOME\Downloads\voice_chatbot_task"
```

## 3. إنشاء بيئة افتراضية

```powershell
py -3.11 -m venv .venv
```

تشغيل البيئة:

```powershell
.venv\Scripts\activate
```

## 4. تثبيت FFmpeg

Whisper يحتاج إلى FFmpeg لمعالجة ملفات الصوت.

بعد تثبيته، أغلق PowerShell وافتحه من جديد، ثم تحقق:

```powershell
ffmpeg -version
```

## 5. تثبيت المكتبات

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 6. إنشاء مفتاح Cohere

أنشئ حسابًا في Cohere، ثم أنشئ API Key.

انسخ ملف المثال:

```powershell
copy .env.example .env
```

افتح ملف `.env` واكتب:

```env
COHERE_API_KEY=ضع_المفتاح_الحقيقي_هنا
```

لا ترفع ملف `.env` إلى GitHub، لأنه يحتوي على المفتاح السري.

## 7. تشغيل المشروع

```powershell
python main.py
```

عند ظهور الرسالة:

```text
اضغط Enter لبدء التسجيل، أو اكتب q ثم Enter للخروج.
```

اضغط Enter وتكلم لمدة 8 ثوانٍ. سيقوم البرنامج بعرض كلامك نصيًا، ثم يعرض رد النموذج ويشغله صوتيًا.

## تعديل مدة التسجيل

في ملف `main.py` غيّر:

```python
RECORD_SECONDS = 8
```

مثلاً إلى:

```python
RECORD_SECONDS = 12
```

## تعديل نموذج Whisper

النموذج الحالي:

```python
WHISPER_MODEL = "base"
```

يمكن استخدام `tiny` لتشغيل أسرع، أو `small` لدقة أعلى، لكن النموذج الأكبر يحتاج وقتًا وذاكرة أكثر.

## طريقة رفع المشروع على GitHub

بعد إنشاء مستودع جديد وفارغ في GitHub، نفّذ:

```powershell
git init
git add .
git commit -m "Add Arabic voice chatbot project"
git branch -M main
git remote add origin رابط_المستودع
git push -u origin main
```

## سير عمل البرنامج

```text
Microphone
   ↓
WAV audio
   ↓
Whisper (Speech to Text)
   ↓
Cohere LLM (Generate Response)
   ↓
gTTS (Text to Speech)
   ↓
MP3 spoken response
```

## ملاحظات

- يحتاج Cohere وgTTS إلى اتصال بالإنترنت.
- يعمل Whisper محليًا بعد تنزيل النموذج أول مرة.
- يجب السماح لـ Python باستخدام الميكروفون من إعدادات Windows.
- لا تشارك مفتاح API ولا تضعه مباشرة داخل `main.py`.

## Author

Ahmed AlBakhat
