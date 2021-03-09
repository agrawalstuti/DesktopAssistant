import pyttsx3 #pip install pyttsx3
import speech_recognition as sr  #pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib

MASTER = "Master"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

# speak function will pronounce the string
def speak(text):
    engine.say(text)
    engine.runAndWait()

# this function will greet you
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if (hour>=0 and hour<12):
        speak("Good Morning " + MASTER)
    elif (hour>=12 and hour<17):
        speak("Good Afternoon " + MASTER)
    else:
        speak("Good Evening " + MASTER)
    #speak("I am jarvis. How may I help you?")


# this function will take command from user
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:    #pip install pipwin; pip install pyaudio
        print("Listening..")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said :{query}\n")

    except:
        print("Say that again please")
        query = None
    return query

# this function will send mail
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('mail@gmail.com', 'password')
    server.sendmail('sa.stutiagrawal@gmail.com',to, content)
    server.close()


# main program
def main():
    speak("Initializing Jarvis...")
    wishMe()
    query = takeCommand()


    # logic for executing query
    if 'wikipedia' in query.lower():
        speak('Searching wikipedia')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)

    elif 'open youtube' in query.lower():
        url = "youtube.com"
        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(url,new=2)

    elif 'open reddit' in query.lower():
        url = "reddit.com"
        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(url,new=2)

    elif 'open geeks for geeks' in query.lower():
        url = "geeksforgeeks.com"
        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        webbrowser.get(chrome_path).open(url,new=2)

    elif 'play music' in query.lower():
        songs_dir = "C:\\Users\\Stuti\\Music"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak( MASTER+"the time is "+strTime)

    elif 'open code' in query.lower():
        codePath = "C:\\Users\\Stuti\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    elif 'email to stuti' in query.lower():
        try:
            speak("What should I send")
            content = takeCommand()
            to = "sa.stutiagrawal@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent successfully")

        except Exception as e:
            print(e)

main()
