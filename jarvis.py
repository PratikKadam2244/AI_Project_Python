import pyttsx3
import json
from typing import Text
from urllib.request import urlopen
from pywhatkit import exceptions 
import speech_recognition as sr 
import datetime
import wikipedia  
import webbrowser
import os
import pywhatkit 
import pyautogui  
import keyboard
import pyjokes
import psutil  
import cv2  
import requests 
import playsound



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 200)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

os.startfile("C:\\Users\\DELL\\Desktop\\adv Ai project\\gui photo\\7LP8.gif")
playsound.playsound("power up.mp3")


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Hello sir, Good Morning")
        print("Good Morning!")
        print(" ")

    elif hour>=12 and hour<18:
        speak("Hello sir, Good Afternoon")
        print("Good Afternoon!")
        print(" ")

    else:
        speak("Good Evening sir")
        print("Good Evening!")
        print(" ")

    print("I am jarvis artificial inteligent. sir please tell me how may I help you")
    speak("I am jarvis artificial inteligent, 64 terabyte machine, sir please tell me how may I help you")
    
    


def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f":Your Command: {query}\n")

    except Exception as e:
        print("Say that again please...")
        speak("sir please Say that again please...")
        print(" ")
        return "None"
    return query

def TaskExecution():                     

    def YoutubeAuto():
        speak("Ok sir, Tell me the command")
        comm = takeCommand()
        
        if 'stop' in comm:
            keyboard.press('k')

        elif 'play' in comm:
            keyboard.press('k')

        elif 'restart' in comm:
            keyboard.press('0')

        elif 'mute' in comm:
            keyboard.press('m')

        elif 'unmute' in comm:
            keyboard.press('m')

        elif 'skip' in comm:
            keyboard.press('l')

        elif 'back' in comm:
            keyboard.press('j')

        elif 'film mode' in query:
            keyboard.press('t')

        elif 'full screen' in comm:
            keyboard.press('f')

        elif 'small screen' in comm:
            keyboard.press('esc')

        elif 'next' in comm:
            keyboard.press_and_release('SHIFT + n')

        elif 'previous' in comm:
            keyboard.press_and_release('SHIFT + p')

        speak("Ok sir")
   
    while True:

        query = takeCommand().lower()

    
    # wikipedia function       
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


    # open notepad function
        elif 'open notepad' in query:
            npath = 'C:\\Windows\\system32\\notepad.exe'
            os.startfile(npath)
            speak("Ok sir, I am open the notepad")

        elif 'close notepad' in query:
            os.system("taskkill /f /im Notepad.exe")
            speak("Ok sir, close the notepad")


    # open youtube function
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Ok sir, I am opening youtube")

        elif 'close youtube' in query:
            os.system("taskkill /f /im chrome.exe")
            speak("Ok sir, close youtube")
 

    # youtube search function
        elif 'youtube search' in query:
            speak("Ok sir. This is what i found for your search!")
            query = query.replace("jarvis","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            speak("Done sir, I am searching")


    # open website function      
        elif 'open website' in query:
            speak("Ok sir")
            query = query.replace("jarvis","")
            query = query.replace("website","")
            web1 = query.replace("open","")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            speak("Done sir, open your website")


    # open google function
        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")
            speak("Ok sir, I am opening google")

        elif 'close google' in query:
            os.system("TASKKILL /f /im chrome.exe")
            speak("Ok sir, close google")


    # google search function   
        elif 'google search' in query:
            import wikipedia as googleScrap
            query = query.replace("jarvis","")
            query = query.replace("google search","")
            speak("Ok sir. This is what i found for your search")
            pywhatkit.search(query)

            try:
                result = googleScrap.summary(query,1)
                speak(result)
                print(result)                

            except:
                speak("No Speakable Data Available!")


    # open chrome function
        elif 'open chrome' in query:
            webbrowser.open("https://www.chrome.com/")
            speak("Ok sir, I am opening google chrome")

        elif 'close chrome' in query:
            os.system("TASKKILL /f /im chrome.exe")
            speak("Ok sir, close chrome")


    # open stackoverflow function
        elif 'open stackoverflow' in query:
            webbrowser.open("https://www.stackoverflow.com/")
            speak("Ok sir, I am open stackoverflow site")

        elif 'close stackoverflow' in query:
            os.system("TASKKILL /f /im chrome.exe")
            speak("Ok sir, close stackoverflow")
  
  
    # open facebook function
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com/")
            speak("Ok sir, I am open facebook")

        elif 'close facebook' in query:
            os.system("TASKKILL /f /im chrome.exe")
            speak("Ok sir, close facebook")
 

    # Open whatsapp function
        elif 'open whatsapp' in query:
            codepath = 'C:\\Users\\HP\\AppData\\Local\\WhatsApp\\WhatsApp.exe'
            os.startfile(codepath)
            speak("Ok sir, I am open whatsapp")

        elif 'close whatsapp' in query:
            os.system("taskkill /f /im WhatsApp.exe")
            speak("Ok sir, close whatsapp")

 
    # open instagram function
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/")
            speak("Ok sir, I am open instagram page")

        elif 'close instagram' in query:
            os.system("TASKKILL /f /im chrome.exe")
            speak("Ok sir, close instagram")


    # open twitter function
        elif 'open twitter' in query:
            webbrowser.open("https://www.twitter.com/")
            speak("Ok sir, I am open twitter")

        elif 'close twitter' in query:
            os.system("TASKKILL /f /im chrome.exe")
            speak("Ok sir, close twitter")
  
  
    # open telegram function
        elif 'open telegram' in query:
            webbrowser.open("https://www.telegram.com/")
            speak("Ok sir, I am open telegram app")

        elif 'close telegram' in query:
            os.system("TASKKILL /f /im chrome.exe")
            speak("Ok sir, close telegram")
 
 
    # open command function
        elif 'open command' in query or 'open cmd' in query:
            os.system("start cmd")
            speak("Ok sir, open command prompt")

        elif 'close command' in query or 'close cmd' in query:
            os.system("taskkill /f /im cmd.exe")
            speak("Ok sir, close command prompt")
 
 
    # open code function
        elif 'open code' in query:
            codepath = '"C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"'
            os.startfile(codepath)
            speak("Ok sir, I am open code")

        elif 'close code' in query:
            os.system("taskkill /f /im Code.exe")
            speak("Ok sir, close vs code")


    # play music function    
        elif 'play music' in query:
            music_dir ='E:\\songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
            speak("Ok sir, I am play music. Sir Enjoy song")


    # Time function     
        elif 'the time' in query or 'times' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(strTime)

        elif 'the date' in query or 'date' in query:
            year=int(datetime.datetime.now().year)
            month=int(datetime.datetime.now().month)
            date=int(datetime.datetime.now().day)
            speak("Sir The current date is")
            speak(date)
            speak(month)
            speak(year)

    # jarvis information function
        elif 'hello jarvis' in query or 'hi jarvis' in query:
            speak("Hello sir, nice to meet you,")

        elif 'how are you' in query:
            speak("I am always fine sir, Whats about you")

        elif 'who are you' in query:
            speak("I am jarvis, Your personal Assistant")

        elif 'what is your name' in query:
            speak("My name is jarvis, Artificial Inteligent 64 terabyte. Your personal assistant")


    # shutdown function
        elif 'shutdown' in query:
            speak("Ok sir. I am shutdown your pc. Wait a few minute")
            os.system("shutdown -s")


    # play song youtube function
        elif 'play song on youtube' in query:
            pywhatkit.playonyt("mast magan")
            speak("Ok I am play any song on youtube")


    # screenshot function
        elif 'screenshot' in query:
            speak("Ok sir, sir please Hold the screen, I am take a screenshot")
            kk = pyautogui.screenshot()
            speak("sir your screenshot is save. file name is screenshot.png")


    # Youtube Automation function   
        elif 'stop' in query:
            keyboard.press('k')

        elif 'play' in query:
            keyboard.press('k')

        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'unmute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'film mode' in query:
            keyboard.press('T')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'small screen' in query:
            keyboard.press('esc')

        elif 'next' in query:
            keyboard.press_and_release('SHIFT + n')

        elif 'previous' in query:
            keyboard.press_and_release('SHIFT + p')

        elif 'youtube function' in query:
            YoutubeAuto()
        

    # joke function 
        elif 'joke' in query:
            get = pyjokes.get_joke()
            speak(get)
    

    # repeat words function
        elif 'repeat my words' in query:
            speak("Ok. Speak sir")
            jj = takeCommand()
            speak(f"You Said : {jj}")
  

    # volume function
        elif 'volume up' in query:
            pyautogui.press("volumeup")
            speak("Ok volume increase")

        elif 'volume down' in query:
            pyautogui.press("volumedown")
            speak("Ok volume decrease")

        elif 'sound mute' in query:
            pyautogui.press("volumemute")
            speak("Ok volume mute")


    # camera function
        elif 'open camera' in query or 'open the camera' in query or 'open a camera' in query:
            speak("Ok sir I am open camera, Wait a few second")
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
            speak("sir your camera is close")


    # whatsapp function
        elif 'send whatsapp message to pratik' in query:
            speak("what should i say to pratik?")
            say = takeCommand()
            speak("set the time to deliever the message")
            pywhatkit.sendwhatmsg('+918975623356', f"{say}", int(input()),int(input()))
            speak("message sent sir!")

        elif 'send whatsapp message to sudhir' in query:
            speak("what should i say to sudhir?")
            say = takeCommand()
            speak("set the time to deliever the message")
            pywhatkit.sendwhatmsg('+919011279321', f"{say}", int(input()),int(input()))
            speak("message sent sir!")

        elif 'send whatsapp message' in query:
            speak("Sir Enter the phone number")
            phone = int(input("Enter phone number: "))
            print(" ")
            speak("Tell me the message")
            msg = takeCommand()
            speak("Sir tell me the time in hour")
            hour = int(input("Time in Hour:"))
            speak("Sir tell me the time in minute")
            min = int(input("Time in Minute: "))
            speak("Ok sir sending whatsapp message")


    
    # Location Function
        elif 'my location' in query or 'home location' in query:
                speak("Ok sir, open your locaton")
                webbrowser.open("https://www.google.com/maps/place/Shree+Yellayya+Apartment/@19.2750703,73.0389201,17z/data=!4m8!1m2!2m1!1sA5-204,+yellaya+aapartment,+charni+pada,+anjurphata,+bhiwandi,+thane!3m4!1s0x3be7bd91ad0b7759:0xc920588087fd2b0!8m2!3d19.2749756!4d73.0361324")
        
        elif 'close location' in query:
            os.system("TASKKILL /f /im chrome.exe")
            speak("Ok sir, close location")

        elif 'open maps' in query:
                speak("Ok sir, open maps")
                webbrowser.open("https://www.google.com/maps/@19.2752064,73.0381763,17.46z")

        elif 'close maps' in query:
            os.system("TASKKILL /f /im chrome.exe")
            speak("Ok sir, close maps")


    # News Function
        elif 'news' in query:
            try:
                jsonObj = urlopen('https://newsapi.org/v2/everything?q=tesla&from=2021-07-16&sortBy=publishedAt&apiKey=5e62cab45b6d4c23906fb9c37f01058c')
                data = json.load(jsonObj)
                i = 1
                speak("Here are some Top news from times of india")
                print('''===============================TIMES OF INDIA============================'''+ '\n')

                for item in data['articles']:
                    print(str(i) + '- ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '- ' + item['title'] + '\n')
                    i +=1

            except Exception as e:
                print(str(e))


    #  Alarm Function
        elif 'alarm' in query:
            speak("sir Enter the Time for set alarm")
            speak("sir you enter time in 24 hour format")
            time = input(":Enter The Time : ")
            speak("Sir your alarm is set")

            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M")

                if now == time:
                    speak("Wake up sir")
                    print("Wake up sir")
                    music_dir ='C:\\Users\\DELL\\Desktop\\Ai project\\alarm'
                    songs = os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))
                    speak("sir your alarm time")                   

                elif now>time:
                    speak("Alarm Closed!")
                    break


    # Remember Function
        elif 'remember that' in query:
            rememberMsg = query.replace("jarvis remember that"," ")
            speak("You Tell Me Remind You That : "+rememberMsg)
            print(":You Tell Me Remind You That : "+rememberMsg)
            print(" ")
            remeber = open('data.txt','w')
            remeber.write(rememberMsg)
            remeber.close()

        elif 'show that remember' in query or 'show the remember' in query or 'what do you remember' in query:
            remeber = open('data.txt','r')
            speak("You Tell Me That" + remeber.read())

            print(" ")


    # any type
        elif 'type' in query or "jarvis write" in query:
            query = query.replace("jarvis"," ")
            query = query.replace("type"," ")
            query = query.replace("write"," ")
            pyautogui.typewrite(f"{query}", 0.1)
            speak("Ok sir")


    # Exit Function
        elif "exit" in query or "quit" in query or "goodby" in query or "by" in query:
            speak("I am exit sir, thanks for using me")
            playsound.playsound("power down.mp3")
            quit()


    # Sleep Function
        elif 'sleep now' in query or 'sleep' in query:
            speak("Ok sir, I am sleep now, you can call me any time")
            break
        


if __name__ == "__main__":
    wishMe()
    while True:
        takeCommand()
        TaskExecution()
        

    

    
    
    
                
        



    