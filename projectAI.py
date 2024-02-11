import os
import pyttsx3
import datetime
import pyautogui
import keyboard
import webbrowser
import pywhatkit
import speech_recognition as sr
from PyDictionary import PyDictionary 
from playsound import playsound


Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty("voices",voices[1].id)


def speak(audio):
    Assistant.say(audio)
    print(f":{audio}")
    Assistant.runAndWait()


def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        command.pause_threshold = 1 
        audio = command.listen(source)
        
        query=""
        try:
            print("Recognizing......")
            query = command.recognize_google(audio,language='en-in') 
            print(f"You Said : {query}")
            
        except Exception as Error:
            print("say that again.....")
            return "None"
        return query.lower()


def greeting():
    speak("Hello sir!, how may I assist you today.")

def Dict(query):
    ddict = PyDictionary()
    speak('Dictionary Activated sir!')
    query = query.replace('what is the' ,'')
    query = query.replace('meaning of' , '')
    result = ddict.meaning(query)
    speak(f'The meaning of {query} is {result}')
    speak('Dictionary Deactivated sir!')


def screenshot():
    speak('Ok Sir , what should I name the screenshot')
    nme = takecommand()
    pth = nme + '.jpeg'
    pth1 = ".\\screenshots\\" + pth
    ss = pyautogui.screenshot()
    ss.save(pth1)
    os.startfile('.\\screenshots')
    speak('Here is your screenshot sir!')

def ChromeAuto():
    speak("Chrome Automation Started")
    speak('Sir. Please tell if you are on chrome')
    response = takecommand()

    if 'no' in response:
        url = 'https://www.google.com/'
        webbrowser.open(url)        
    
    speak('What task you want me to perform')
    task = takecommand()
        
    if 'close this tab' in task:
        keyboard.press_and_release('ctrl + w')
    elif 'open new tab' in task:
        keyboard.press_and_release('ctrl + t')
    elif 'open new window ' in task:
        keyboard.press_and_release('ctrl + n')
    elif 'history' in task:
        keyboard.press_and_release('ctrl + h')
    elif 'open incognito mode tab' in task:
        keyboard.press_and_release('ctrl + shift + n')
    elif 'downloads tab' in task:
        keyboard.press_and_release('ctrl + j')
    elif 'reopen closed tab' in task:
        keyboard.press_and_release('ctrl + shift + t')
    elif 'open next page in browsing history' in task:
        keyboard.press_and_release('alt + right_arrow')
    elif 'search' in task:
        query = query.replace ('search' , "")
        speak("These are the results that I found")
        url = 'https://www.google.com/search?q='+query
        webbrowser.open(url)
    else:
        speak("Could not understand the task.")
        speak("Please say Chrome Automation if you want me to restart automation")
        os.system('TASKKILL /F /im chrome.exe')


def setAlarm():
    speak("Please enter the time 12 hour format: ")
    alarmHour = int(input("Enter Hour: "))
    alarmMin = int(input("Enter Minutes: "))
    alarmAm = input("am / pm: ")

    if alarmAm.lower() =="pm":
        alarmHour+=12
    
    while True:
        if(alarmHour == datetime.datetime.now().hour and alarmMin == datetime.datetime.now().minute):
            playsound("Alarm.mp3")
            break

def takeNote():
    speak("what do you want me to remember?")
    remember = takecommand()
    speak('You have told me to remember that :' + remember)
    rem = open('data.txt' , 'w')
    rem.write(remember)
    rem.close()

def readNote():
    rem = open('data.txt' , 'r')
    speak('Yes Sir I do remember')
    speak('You told me that ' + rem.read())

def playSong():
    speak("What song you want to hear: ")
    song = takecommand()
    song = song.replace("play","")
    pywhatkit.playonyt(song)


def taskExe():
    greeting()
    while True:
        query = takecommand()
        if 'screenshot' in query:
            screenshot()
        elif 'youtube' in query:
            speak('Ok sir , Searching Please wait!')
            query = query.replace('Robert' , "")
            query = query.replace ('search on youtube' , "")
            url = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(url)
            speak('This is what I have searched for you. Is it okay sir?')
        elif "chrome automation" in query:
            ChromeAuto()
        elif "meaning" in query:
            Dict(query)
        elif "alarm" in query:
            setAlarm()
        elif 'remember that' in query:
            takeNote()
        elif 'something i have told you to remember' in query:
            readNote()
        elif 'song' in query:
            playSong()
        elif query!="None":
            speak("These are the results that I found")
            url = 'https://www.google.com/search?q='+query
            webbrowser.open(url)
        else:
            speak("No command found. Ending the execution.")
            break    
        

taskExe()
