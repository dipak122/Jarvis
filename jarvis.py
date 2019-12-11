import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
#import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait() 

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("i am Jarvis Sir, Please tell me how may I help you ")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query





if __name__ == "__main__":
    wishMe()
    print("hello----------------")
    while True:    
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching in wikipedia..")
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia..")
            speak(results)

    speak("dipak is a good boy")