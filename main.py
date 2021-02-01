import speech_recognition as sr
import pyaudio
import time
import requests
import json
import webbrowser

hear = sr.Recognizer()
#print(sr.Microphone.list_microphone_names())

mic = sr.Microphone(device_index=1)

url = 'http://api.openweathermap.org/data/2.5/weather?q={YourCity}&appid={YourAPIKey}&units=metric'
obtain = requests.get(url)
data = obtain.json()
temp =  data['main']['temp']


hear = sr.Recognizer()
#print(sr.Microphone.list_microphone_names())

mic = sr.Microphone(device_index=1)


engine = pyttsx3.init()


while True:
    with mic as source:
        audio = hear.listen(source)
        
        text = hear.recognize_google(audio)
            
        if(text) == "hello":
            print("Hello User")
            engine.say("Hello User")
            engine.runAndWait()
            
        elif(text) == "help":
            print("Commands for voice assistant include\n1. Hello --> Hello User\n2. Help --> provide commands for assistant\n3. What time is it --> provides local time and date\n4. What's the tempature --> provides tempature in selected city\n5. Tell me a joke --> Returns a joke\n6. How are you --> provides a response\n7. Open browser --> Opens Google\n8. Open video --> Opens Youtube\n9. Exit --> Exits assistant")
            engine.say("Commands for voice assistant include\n1. Hello --> Hello User\n2. Help --> provide commands for assistant\n3. What time is it --> provides local time and date\n4. What's the tempature --> provides tempature in selected city\n5. Tell me a joke --> Returns a joke\n6. How are you --> provides a response\n7. Open browser --> Opens Google\n8. Open video --> Opens Youtube\n9. Exit --> Exits assistant")
            engine.runAndWait()
        
        elif(text) == "what time is it":
            print("The current date/time is " + time.ctime())
            engine.say("The current date/time is " + time.ctime())
            engine.runAndWait()
        
        elif(text) == "what's the temperature":
            print("The current temperature in your city is " + str(temp) + " degrees celsius")
            engine.say("The current temperature in your city is " + str(temp) + " degrees celsius")
            engine.runAndWait()


        elif(text) == "tell me a joke":
            print("Yesterday I saw a guy spill all his Scrabble letters on the road, So I asked him, “What’s the word on the street?”")
            engine.say("Yesterday I saw a guy spill all his Scrabble letters on the road, So I asked him, “What’s the word on the street?”")
            engine.runAndWait()


        elif(text) == "how are you":
            print("I do not know because I am a computer. I do not have emotions.")
            engine.say("I do not know because I am a computer. I do not have emotions.")
            engine.runAndWait()


        elif(text) == "open browser":
            webbrowser.open('www.google.com')
            engine.say("Browser opened")
            engine.runAndWait()


        elif(text) == "open video":
            webbrowser.open('www.youtube.com')
            engine.say("Youtube opened")
            engine.runAndWait()


        elif(text) == "exit":
            engine.say("Exiting")
            engine.runAndWait()
            exit()

        
        