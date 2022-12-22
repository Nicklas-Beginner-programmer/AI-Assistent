import speech_recognition as sr
import pyttsx3 
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess 
import ecapture as ec
import wolframalpha 
import json
import requests

print("loading main")

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setproperty('voice', 'voices[0].id')




def speak(text):
    engine.say(text)
    engine.runAndWait

def wishMe():
    hour=daytime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>= 12 and hour<18:
        speak("Good afternoon!")
    else: 
        speak("Good Evening!")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}/n")

        except exception as e: 
            speak("I didnt hear you, please say that again")
            return "none"
        return statement

speak("loading main")
wishMe()

# when the name is heared (main) it will respond with what can i do for you? and when it heres
# good bye og de others mentioned below, it will say see you later!

if __name__=='__main__':

    while True: 
        speak("What can I do for you?")
        statement = takeCommand().lower()
        if statement==0:
            continue
        if "good bye" in statement or "ok bye" in statement or "turn off" in statement: 
            speak ('see you later!')
            break
            
            # this command tell the AI that, if wikipedia is mentioned, it will search up and find
            # what you are looking for 

        if 'wikipedia' in statement: 
            speak('Searching the wiki')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to the wiki")
            speak(results)

# the code needed to make a statement to tell it to open youtube and gmail, here included other stuff.

elif 'open youtube' in statement: 
    webbrowser.open_new_tab("https://www.youtube.com")
    speak("Youtube is open now")
    time.sleep(5)

elif 'open gmail' in statement: 
    webbrowser.open_new_tab("gmail.com")
    speak("Google mail open now")
    time.sleep(5)