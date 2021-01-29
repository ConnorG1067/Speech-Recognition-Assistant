import speech_recognition as sr
import pyaudio
import time
import requests
import json
import webbrowser

hear = sr.Recognizer()
#print(sr.Microphone.list_microphone_names())

mic = sr.Microphone(device_index=1)

url = 'http://api.openweathermap.org/data/2.5/weather?q=Ottawa&appid=afd36b72a1089a148c582bc930a4267d&units=metric'
obtain = requests.get(url)
data = obtain.json()
#print(data)
temp =  data['main']['temp']



while True:
    with mic as source:
        audio = hear.listen(source)
        
        text = hear.recognize_google(audio)
       
        if(text) == "hello":
            print("Hello User")
        
        elif(text) == "help":
            print("Commands for voice assistant include\n1. Hello --> Hello User\n2. Help --> provide commands for assistant\n3. What time is it --> provides local time and date\n4. What's the tempature --> provides tempature in selected city\n5. Tell me a joke --> Returns a joke\n6. How are you --> provides a response\n7. Open browser --> Opens Google\n8. Open video --> Opens Youtube\n9. Exit --> Exits assistant")
        
        elif(text) == "what time is it":
            print("The current date/time is " + time.ctime())
        
        elif(text) == "what's the temperature":
            print("The current temperature in Ottawa is " + str(temp) + " degrees celsius")
        
        elif(text) == "tell me a joke":
            print("Yesterday I saw a guy spill all his Scrabble letters on the road, So I asked him, “What’s the word on the street?”")
        
        elif(text) == "how are you":
            print("I do not know how I feel because I am a computer.")
        
        elif(text) == "open browser":
            webbrowser.open('www.google.com')
       
        elif(text) == "open video":
            webbrowser.open('www.youtube.com')
        
        elif(text) == "exit":
            exit()
        
        
        