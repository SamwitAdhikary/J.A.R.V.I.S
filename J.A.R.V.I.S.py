import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
MASTER = 'Master'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f"Good Morning {MASTER}!!!!!")
    elif hour >=12 and hour < 18:
        speak(f"Good Afternoon {MASTER}!!!")
    else:
        speak(f"Good Evening {MASTER}!!!")

    speak(f"I am Jarvis {MASTER}... How may i help you??")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.adjust_for_ambient_noise(source,duration=3)
        r.pause_threshold = 5
        audio = r.record(source,duration=2)
        # audio = r.listen(source)

        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language='en-in')
            print(f"User Said: {query}\n")

        except Exception as e :
            print("Please Say That Again...!!")

    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak(f"Searching Wikipedia for you {MASTER}...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According To Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak(f"Opening Youtube for you sir {MASTER}")
            url = "youtube.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open google' in query:
            speak(f"Opening Google for you {MASTER}")
            url = "google.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        elif 'open amazon' in query:
            speak(f"Opening amazon for you {MASTER}")
            url = "amazon.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

