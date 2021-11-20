import pyttsx3 # Module ie text-to-speech conversion library in Python
import speech_recognition as sr #  it will help to recognise our voice and take actions accordingly
import webbrowser
import os
import pywhatkit
import time
import pytz
import wikipedia
import pyautogui
import keyboard
import pyjokes
import datetime
from googletrans import Translator
from playsound import playsound
from PyDictionary import PyDictionary 

Assistant  = pyttsx3.init('sapi5')# init is a costructor which helps to initialize the attributes of a class ans sapi5 is speech recognition api given by microsoft
voices = Assistant.getProperty('voices')
#print(voices) # It will tell number of  voices present in the system
Assistant.setProperty('voices', voices[0].id)
Assistant.setProperty('rate', 130)
def speak(audio):
    print("    ")
    Assistant.say(audio)# it will send the speech to say which will be spoken by the voice at id 0. 
    print(f": {audio}")
    print('    ')
    Assistant.runAndWait() # this function helps us to make the speech audible in this system if we won't write this commmand the speech will not be audible to us.
def takecommand() :
    command  = sr.Recognizer() # this will recognize our voice which we gave and save to command
    with sr.Microphone() as source:  # will take our audio through microphone as audio source
        print ("Listening......")
        command.pause_threshold = 0.8 # pause threshold helps us to make understand our assistant that how much time it should listen us.
        audio = command.listen(source) # Listen helps our assistant to listen our voice which we have spoken from source.

        try: # This will help our assistant to recognise our voice which we spoke iff spoken something which doesn't recognisable to our asssitant then try will stop
            print("Recognising....")
            query = command.recognize_google(audio, language = 'en-in' )
            print(f"You Said : {query} ")
        except Exception as Error: # if our assistant doesn't recognize our voice then this function will run 
            speak("Not able to recognize. Please Say again")
            return "None"
        return query.lower()
def TaskExe():
    
    def Music():
        speak("Tell me the name of the music or Song you want to  hear!")
        music = takecommand()
        if ' from internet' in music:
            music = music.replace('from Internet' , "")
            pywhatkit.playonyt(music)
            speak("Your Song Has Been Started! , Enjoy Sir!")
        else:
            speak('Shall I play on Internet Sir!')
            answer = takecommand()
            if 'yes play' in answer:
                pywhatkit.playonyt(music)
                speak("Your Song Has Been Started! , Enjoy Sir!")     
            else:
                speak("Sorry Sir . Song Not found in the Device.")
    def Whatsapp():
        speak("Do you have logged into the whatsapp web into your device sir.")
        a = takecommand()
        if 'yes'in a:
            speak("Enter the contact number Sir")
            num = input(": Enter the contact Number: ")
            number = '+91' + num 
            speak('Tell me the message you want to send just now sir!')        
            msg = takecommand()
            pywhatkit.sendwhatmsg_instantly(number , msg)
            speak(f"Ok Sir sending whatsapp message to {name}")
            keyboard.press('enter')
            speak('Message send sir')
        else:
            speak('Please Log into your account so that I can send message to the person')
            speak('When you logged in. You can call me again sir. ThankYou')
    def openapps():
        speak('Wait a Second Sir!')
        if ' vs code ' in query:
            os.startfile('C:\\Users\\akhil\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe')
        elif 'opera' in query:
            os.startfile('C:\\Program Files\\Opera\\launcher.exe')
        elif 'firefox' in query:
            os.startfile("C:\\Program Files\\Mozilla Firefox\\firefox.exe")    
        elif 'chrome' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        elif 'my class lpu' in query:
            webbrowser.open('https://myclass.lpu.in')
        elif 'lpu live' in query:
            webbrowser.open('https://www.lpulive.lpu.in')
        elif 'facebook' in query:
            webbrowser.open('https://www.facebook.com/')
        elif 'youtube' in query:
            webbrowser.open('https://www.youtube.com')
        elif 'google maps' in query:
            webbrowser.open('https://www.google.com/maps/')
        speak('Your app or site has been opened successfully')
    def closeapps():
        speak('Wait a Second Sir!')
        if ' v s code ' in query:
            os.system('TASKKILL /F /im Code.exe')
        elif 'opera' in query:
            os.system('TASKKILL /F /im launcher.exe')
        elif 'firefox' in query:
            os.system("TASKKILL /F /im firefox.exe")    
        elif 'chrome' in query:
            os.system("TASKKILL /F /im chrome.exe")
        elif 'my class lpu' in query:
            os.system('TASKKILL /F /im chrome.exe')
        elif 'lpu live' in query:
            os.system('TASKKILL /F /im chrome.exe')
        elif 'youtube' in query:
            os.system('TASKKILL /F /im chrome.exe')
        elif 'facebook' in query:
            os.system('TASKKILL /F /im chrome.exe')
        elif 'google maps' in query:
            os.system('TASKKILL /F /im chrome.exe')
        speak('Your app or site has been closed successfully')
    def  YoutubeAuto():
        speak('''What's your command sir ?''' ) 
        com = takecommand()
        
        if 'pause' in com:
            keyboard.press('k')
        elif 'restart' in com:
            keyboard.press('0')  
        elif 'mute' in com:
            keyboard.press('m')   
        elif 'skip' in com:
            keyboard.press('l')
        elif 'back' in com:
            keyboard.press('j')
        elif 'full screen' in com:
            keyboard.press('f')
        elif 'film mode' in com:
            keyboard.press('t')
        elif 'Mini player' in com:
            keyboard.press('i')
        elif 'Default view' in com:
            keyboard.press('t')
        speak("Done sir")
    def ChromeAuto():
        speak("Chrome Automation Started")
        speak('Sir. Please tell the operation you want to perform?')
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
    def Dict():
       ddict = PyDictionary()
       speak('Dictionary Activated sir!')
       speak('Tell me the word sir whose meaning you want to know')
       problm = takecommand()
       problm = problm.replace('what is the' ,'')
       problm = problm.replace('meaning of' , '')
       result = ddict.meaning(problm)
       speak(f'The meaning of {problm} is {result}')
    def screenshot():
        speak('Ok Sir , what should I name the screenshot')
        nme = takecommand()
        pth = nme + '.jpeg'
        pth1 = 'Screenshots\\'+pth
        ss = pyautogui.screenshot()
        ss.save(pth1)
    def TakeHindi():
        command  = sr.Recognizer() # this will recognize our voice which we gave and save to command
        with sr.Microphone() as source:  # will take our audio through microphone as audio source
            print ("Listening......")
            command.pause_threshold = 1 # pause threshold helps us to make understand our assistant that how much time it should listen us.
            audio = command.listen(source) # Listen helps our assistant to listen our voice which we have spoken from source.

            try: # This will help our assistant to recognise our voice which we spoke iff spoken something which doesn't recognisable to our asssitant then try will stop
                print("Recognising....")
                query = command.recognize_google(audio, language = 'hi' )
            except: # if our assistant doesn't recognize our voice then this function will run 
                return 'none'
            
            return query.lower()
    def Trans():
        speak("Tell Me the line Sir!")
        line = TakeHindi()
        print(f"You Said : {line} ")
        
        speak('translation going on')
        translate = Translator()
        result = translate.translate(line)
        T = result.text
        speak(T)
    def SpeedTest():
        import speedtest
        speak('Please Wait while I check the current Internet speed')  
        speed = speedtest.Speedtest() 
        downloading = speed.download()
        cdown = int(downloading/800000)
        uploading = speed.upload()
        cup = int(uploading/800000)
        if 'uploading' in query:
            speak('The uploading speed is :'+ cup +'mbps')
        if 'downloading' in query:
            speak('The downloading speed is :'+ cdown + 'mbps')
        else:
            speak(f'The Downloading and uploading speed is {cdown} mbps and {cup} mbps respectively.')

    while True:
        query = takecommand()
        if 'hello' in query:
            speak(" Hello Sir , I am your virtual AI assistant.")
            speak("How may I help you .")
        elif 'what is your name' in query:
            speak('My name is Robert')
        elif 'how are you' in query:
            speak("I am Fine !")
            speak("What About You?")
        elif 'you need a break' in query:
            speak('Ok Sir! , You can call me back if needed again...')
            break
        elif 'search on youtube' in query:
            speak('Ok sir , Searching Please wait!')
            query = query.replace('Robert' , "")
            query = query.replace ('search on youtube' , "")
            url = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(url)
            speak('This is what I have searched for you. Is it okay sir?')
        elif 'website' in query:
            speak('Ok Sir , Launching Your site , Please wait!')
            query = query.replace('open website',"")
            query = query.replace(' ','')
            web1 = query
            url = 'https://www.'+ web1 + '.com'
            webbrowser.open(url)
            speak('Done sir.')
        elif 'launch'in query:
            speak("Tell me the name  of the website!")
            name = takecommand()
            url = 'https://www.'+ name + '.com'
            webbrowser.open(url)
            speak('Done sir')
        elif 'play music'in query:
            Music()
        elif 'wikipedia'in query:
            speak("Searching in Wikipedia....")
            query = query.replace('search on wikipedia' ,"")
            wiki = wikipedia.summary(query,2)
            speak(f"According to wikipedia : {wiki}")
            speak('This much ok Sir')
        elif 'send a whatsapp message' in query:
            Whatsapp()
        elif 'screenshot' in query:
            screenshot()
        elif 'open facebook' in query:
            openapps()
            speak('Done Sir')
        elif 'open opera' in query:
            openapps()
            speak('Done Sir')
        elif 'open firefox' in query:
            openapps()
            speak('Done Sir')
        elif 'open google maps' in query:
            openapps()
            speak('Done Sir')
        elif 'open vs code' in query:
            openapps()
            speak('Done Sir')
        elif 'open youtube' in query:
            openapps()
            speak('Done Sir')        
        elif 'open my class lpu' in query:
            openapps() 
            speak('Done Sir')   
        elif 'open lpu live' in query:
            openapps()
            speak('Done Sir')
        elif 'open chrome' in query:
            openapps()
            speak('Done Sir')
        elif 'close chrome' in query:
            closeapps()
            speak('Done Sir')
        elif 'close opera' in query:
            closeapps()
            speak('Done Sir')
        elif 'close firefox' in query:
            closeapps()
            speak('Done Sir')
        elif 'close facebook' in query:
            closeapps()
            speak('Done Sir')
        elif 'close youtube' in query:
            closeapps()
            speak('Done Sir')
        elif 'close myclass lpu' in query:
            closeapps()
            speak('Done Sir')
        elif 'close lpulive' in query:
            closeapps()
            speak('Done Sir')
        elif 'close google maps' in query:
            closeapps()
            speak('Done Sir')
        elif 'close vs code' in query:
            closeapps()
            speak('Done Sir')
        elif 'pause' in query:
            keyboard.press('k')
        elif 'restart' in query:
            keyboard.press('0')  
        elif 'mute' in query:
            keyboard.press('m')   
        elif 'skip' in query:
            keyboard.press('l')
        elif 'back' in query:
            keyboard.press('j')
        elif 'full screen' in query:
            keyboard.press('f')
        elif 'film mode' in query:
            keyboard.press('t')
        elif 'mini player' in query:
            keyboard.press('i')
        elif 'Default view' in query:
            keyboard.press('t')
        elif 'Youtube tools' in query:
            YoutubeAuto()
        elif 'close this tab' in query:
            keyboard.press_and_release('ctrl + w')
            speak('Done Sir')
        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')
            speak('Done Sir')
        elif 'open new window ' in query:
            keyboard.press_and_release('ctrl + n')
            speak('Done Sir')
        elif 'history' in query:
            keyboard.press_and_release('ctrl + h')
            speak('Done Sir')
        elif 'open incognito mode tab' in query:
            keyboard.press_and_release('ctrl + shift + n')
            speak('Done Sir')
        elif 'downloads tab' in query:
            keyboard.press_and_release('ctrl + j')
            speak('Done Sir')
        elif 'reopen closed tab' in query:
            keyboard.press_and_release('ctrl + shift + t')
            speak('Done Sir')
        elif 'open next page in browsing history' in query:
            keyboard.press_and_release('alt + right_arrow')
            speak('Done Sir')
        elif 'chrome automation' in query:
            ChromeAuto()
        elif 'have some jokes' in query:
            while True:
                joke = pyjokes.get_joke()
                speak(joke)
                speak('One more sir')
                ans = takecommand()
                if 'no' in ans:
                    break
        elif 'repeat my words' in query:
            speak('Speak Sir...')
            rpt = takecommand()
            speak(f'You said {rpt}  sir ')
        elif 'my location' in query:
            webbrowser.open('https://www.google.com/maps/@27.5634302,80.6106629,12z')
            speak('You are currently at this location Sir.. ')
        elif  'open dictionary' in query:
            Dict()
        elif 'set the alarm' in query:
            speak('Enter the time Sir!')
            time = input(': Enter the time here : ')
            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime('%H:%M:%S')

                if now == time:
                    speak('Its the time of your Alarm Sir. Time to wake up if you are sleaping Sir..')
                    while True:
                        if now == time:
                            playsound('Alarm.mp3')
                            speak('''Please Wake Up . Don't be too lazy sir''')
                            anss = takecommand()
                            if 'ok fine getting up' in anss:
                                speak('Very Good Sir . You are a very energetic guy.')
                                break
                            elif 'want to sleep more stop the alarm' in anss:
                                speak('Ok sir as your wish')
                                break
                            elif 'after sometime' or 'stop the alarm' or '''Don't want to wake up now''' in anss:
                                speak('ok sir as your wish')
                                break
                            
                    speak('Alarm Closed! sir')
                elif now >time:
                    break
        elif 'remember that' in query:
            remember = query.replace('remember that','')
            speak('You have told me to remember that :' + remember)
            rem = open('data.txt' , 'w')
            rem.write(remember)
            rem.close()
        elif 'something i have told you to remember' in query:
            rem = open('data.txt' , 'r')
            speak('Yes Sir I had remembered')
            speak('You told me that ' + rem.read())         
        elif 'search on google ' in query:
            import wikipedia as googlekit
            query = query.replace('search on google about','')
            query = query.replace('google','')
            #pywhatkit.search(query)
            speak('Ok sir . Please wait for approx 10 seconds')
            try:
                res = googlekit.summary(query , 5)
                speak('This is what i found on the web!')
                speak(res)
                speak('Is that ok Sir')
            except:
                speak('Sorry Sir!. The data is either not readable or too big to read')
        elif 'open translator' in query:
            Trans() 
        elif 'ok fine' in query:
            speak('ok ThankYou Sir')
        elif 'internet speed' in query:
            SpeedTest()

speak("Hello Sir . ")
TaskExe()
