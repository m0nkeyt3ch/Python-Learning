import speech_recognition as speech
import py

recognation = speech.Recognizer()

with speech.Microphone() as source:
    print("Your command: ")
    audio = speech.listen(source)
    try:
        text = speech.recognize_google(audio)
        print("Your command: {}".format(text))
    except:
        print("Can't recognize")