import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as sources:
    print("Say something")
    audio = r.listen(sources)
    voice_data = r.recognize_google(audio)
    print(voice_data)