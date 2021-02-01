import speech_recognition as sr
import pyaudio
import time
import requests
import json
import webbrowser
def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
 
 
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
 
        try:
            said = r.recognize_google(audio)
            print(said)
 
        except Exception as e:
            print("Expection:"+str(e))
    return said
 
 
text = get_audio()
 
if "DC" in text:
    print("https://discord.gg/RjnpzX3")
 
 
if "how are you" in text:
    speak("I am fine ")