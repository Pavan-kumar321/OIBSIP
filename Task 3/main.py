import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pyaudio

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    speak("Hello Pavan, I am your voice assistant. Let me know how can i help you Today.")
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"you said {query}\n")
        except Exception:
            print("Sorry, I did not understand that. can you please repeat thet.")
            return "none"
        return query.lower()
def run_assistent():
    wishme()
    while True:
        query = take_command()
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to query.")
            speak(results)
        elif 'open youtube' in query:
            speak("opening youtube..")
            webbrowser.open("https://www.youtube.com")
        elif 'open google' in query:
            speak("opening google..") 
            webbrowser.open("https://www.google.com")       
        elif 'time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"time is {time} ")
        elif 'date' in query:
            date = datetime.datetime.now().strftime("%d/%m/%y")
            speak(f"Today is {date}.")
        elif 'exit' in query or 'stop' in query:
            speak("I will always be here if you need my help, Feel free to ask me . Goodbye!")
        else:
            speak("sorry, I cant help you with that. please try something else.")
run_assistent()