import pyttsx3
import speech_recognition as sr
import datetime
import time
from datetime import datetime
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 180)             # speed
engine.setProperty("volume", 1)           # volume

def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()
    engine.stop()

def pns(text):
    print(text)
    speak(text)



def wishMe():
    hour = datetime.now().hour
    if hour>=0 and hour<12:
        pns("Good Morning!")

    elif hour>=12 and hour<18:
        pns("Good Afternoon!")

    else:
        pns("Good Evening!")

    pns("Hello Ma'am. I'm your Personal Voice Assistant. Please tell me how may I help you")
r = sr.Recognizer()
def actual_date():
    now = datetime.now()
    mname = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
             7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    pns(f"The date is {now.day}th of {mname[now.month]} of year {now.year}")

def takecommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...") 
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"    
    return query

def Menu():
    pns("""These are some functions which I can perform:
            Respond to Hello,
            Tell you the Time,
            Tell you the Date,
            Google Search for you,
            Open Selected Websites for you,
            To exit, say quit or thanks,
            Thank you for your time""")

def main():
    wishMe()

    while True:
        query = takecommand().lower()

        
    #Logic for executing tasks based on query
        if "hello" in query:
            pns("Hello Ma'am, I'm your Personal Voice Assistant!\nHow would you like me to help you?")
        if 'wikipedia' in query:
            pns('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            pns("According to Wikipedia")
            pns(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")  

        elif 'open google' in query:
            webbrowser.open("google.com")   
  

        elif 'play music' in query: 
            music_dir = "D:\\Desktop\\songs"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))


        elif 'the time' in query:
            strTime = datetime.now().strftime("%H:%M:%S")
            pns(f"Mam, the time is {strTime}")   

        elif "what is the date" in query:
            actual_date()


        elif 'open code'  in query:
            codepath = "C:\\Users\\lovely\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"   
            os.startfile(codepath)

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")

        elif 'quit' in query or 'thanks' in query:
            exit()
        else:
            pns("Please try again.")
        time.sleep(0.1)
        pns("Any other queries, ma'am?")


if __name__ == "__main__":
    main()  

    