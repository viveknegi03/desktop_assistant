import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os

# taking voice from my system
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',150)

# speak function
def speak(text):
    """this function converts text to speech

    Args:
        text (_type_): string
    """
    engine.say(text)
    engine.runAndWait()

# speak("hello my name is jarvis, good morning master!")


# speech recognition function
def takeCommand():
    """this functionwill recoganize voice & return text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language = 'en-in')
            # print(f"user said: {query}\n")


        except Exception as e:
            print("say that again plss")
            return "None"
        return query

def wish_me():
    hour = (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning vivek sir. How are you doing")
    
    elif hour>=12 and hour<18:
        speak("Good afternoon vivek sir. How are you doing")

    else:
        speak("Good evening Vivek sir. How are you doing")
    
    speak("I am JARVIS. Tell me sir how can i help you")


if __name__ =="__main__":
    
    wish_me()
    while True:
        query = takeCommand().lower()


        if "wikipedia" in query:
            speak("searching in wikipedia")
            query = query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences = 2)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif "youtube" in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        
        elif"google" in query:
            speak("opening google")
            webbrowser.open("google.com")

        elif"github" in query:
            speak("opening github")
            webbrowser.open("github.com")
        
        elif'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
       
        elif 'goodbye' in query:
            speak("goodbye sir")
            exit()

