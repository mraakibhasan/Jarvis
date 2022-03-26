import pyttsx3
import datetime
import speech_recognition as sr
from bs4 import BeautifulSoup
import webbrowser
import pyautogui
import wikipedia
import os
import sys
import psutil
import speedtest
import subprocess
import requests
import pywhatkit
import wolframalpha
from time import sleep

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 178)


def Pass(pass_inp):
    password = '0956'
    passss = str(password)

    if passss == str(pass_inp):
        greeting()

    else:
        speak('Matching Data....')
        speak('Sorry, access not granted. Please try again.')
        sys.exit()


def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()


def click():
    pyautogui.click()


def username():
    username = psutil.users()
    for user_name in username:
        first_name = user_name[0]
        speak(f"Sir, this computer is signed to RA K IB as a username.")


def screenshot():
    pyautogui.screenshot(f"C://Users//RA K IB//Desktop//screenshot.png")


def shutDown():
    speak(f'Ok Sir   ')
    speak('Initializing shutdown protocol ')
    click()
    pyautogui.keyDown('alt')
    pyautogui.press('f4')
    pyautogui.keyUp('alt')
    pyautogui.press('enter')
    sleep(3)
    pyautogui.press('enter')


def restart():
    speak("Ok Sir    ")
    speak("Restarting your computer")
    click()
    pyautogui.keyDown('alt')
    pyautogui.press('f4')
    pyautogui.keyUp('enter')
    sleep(3)
    pyautogui.press('r')
    pyautogui.press('enter')


def Sleep():
    sys.exit()


def weather():
    speak("Checking the details for weather...")
    URL = "https://weather.com/weather/today/l/26.62,87.36?par=google&temp=c"
    header = {"User-Agent": 'your user agent'}
    page = requests.get(URL, headers=header)
    soup = BeautifulSoup(page.content, 'html.parser')
    temperature = soup.find(class_="CurrentConditions--tempValue--3KcTQ").get_text()
    description = soup.find(class_="CurrentConditions--phraseValue--2xXSr").get_text()
    temp = "Sir, the temperature is " + temperature + " celcius." + ' and it is ' + description + ' outside.'
    speak(temp)
    if temperature < '20°':
        speak("It will be better if you wear woolen clothes, sir.")
    elif temperature <= '14°':
        speak("Sir, it is very cold outside. If you want to go outside, wear woolen clothes.")
    elif temperature >= '25°':
        speak("Sir, you donot need to wear woolen clothes to go outside.")


def time():
    time = datetime.datetime.now().strftime('%I:%M:%S')
    speak(f"Sir, the current time is {time}.")


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(f"Sir, the current year is {year}, current month is {month} and the current date is {date}")


def google_search(audio_data):
    url = "https://www.google.com/search?q=" + audio_data
    webbrowser.open(url)
    speak(f"Sir, getting the result for {audio_data} from google")


def youtube_search(audio_data):
    url = "https:www.youtube.com/search?query=" + audio_data
    webbrowser.open(url)
    speak(f"Sir, getting the result for {audio_data} from youtube")


def calculate(audio_data):
    app_id = '8REQUG-YQ7JGY96T8'
    client = wolframalpha.Client(app_id)
    res = client.query(audio_data)
    answer = next(res.results).text
    speak(answer)


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 400
        r.dynamic_energy_threshold = True
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio)
        print(query)
        # basic commands
        if 'Jarvis' in query:
            speak("Yes sir. Always here for you.")
        elif 'how are you' in query or 'tell me date' in query:
            speak("I am fine sir. What about you?")
        elif 'I am fine' in query or 'tell me date' in query:
            speak("Feeling good to see you sir. How can I help you")
        elif 'I am not fine' in query or 'tell me date' in query:
            speak("I am feeling sad for you sir. What can I do for you to feel you good again? "
                  "Can I play anything for you? , Can I tell you a joke? Sir please tell me what you want?")
        elif 'I am sick' in query or 'tell me date' in query:
            speak("Sir, please take your medicines. I pray to Allah to heal you soon. Please don't forget to take"
                  "medicines. Who would I talk to if you were sick? I have no one without you sir")
        elif 'what you think about me' in query:
            speak('Sir, I think you are a good person. Some time you afraid for some reason. But you are a gentle'
                  'person in my eye. I love all of your work.')
        elif 'tell me the date' in query or 'tell me date' in query:
            date()
        elif 'tell me the time' in query or 'what time is it' in query or 'tell time' in query:
            time()
        elif 'thank you' in query:
            speak('No problem sir')
        elif 'wake up' in query:
            now = datetime.datetime.now()
            hour = now.hour
            tim = datetime.datetime.now().strftime('%I %M %p')
            if hour < 12:
                greeting = "Good Morning sir. I am online now. Importing all preferences from home interface. " \
                           "System is now fully operational"
            elif hour < 18:
                greeting = "Good afternoon sir. I am online now. Importing all preferences from home interface. " \
                           "System is now fully operational"
            else:
                greeting = "Good night sir. I am online now. Importing all preferences from home interface. " \
                           "System is now fully operational"
            speak("{}!".format(greeting) + 'its' + tim)

        # links opeing commands
        elif 'open Google' in query:
            webbrowser.open("https://www.google.com")
            speak("Okay sir. Opening google...")
        elif 'Google search' in query:
            speak('Sir. What do you want to search?')
            audio_data = command()
            google_search(audio_data)
        elif 'open YouTube' in query:
            webbrowser.open("https://www.youtube.com")
            speak("Okay sir. Opening Youtube....")
        elif 'YouTube search' in query:
            speak('Sir, What do you want to search?')
            audio_data = command()
            youtube_search(audio_data)
        elif 'fibre' in query:
            webbrowser.open('https://www.fiverr.com/raakibhasaan?up_rollout=true')
            speak('okay sir, opening fiverr')
        elif 'router' in query:
            webbrowser.open('http://192.168.0.1')
            speak('okay sir, opening your tp link router control panel')
        elif 'instagram' in query:
            webbrowser.open('https://www.instagram.com')
            speak('okay sir, opening instagram')
        elif 'Code' in query or 'grammar' in query or 'the court grammar' in query:
            webbrowser.open('https://www.google.com/search?client=firefox-b-d&q=the+codegrammer')
            speak('The CodeGrammer is a Web & Application development company. '
                  'They providing this services proudly from three years. Founded by Seeaam Hossain and Rakib Hasan')
        elif 'coders' in query:
            webbrowser.open(
                'https://www.google.com/search?q=coders+horizen&sxsrf=APq-'
                'WBsAOEd61KUVgGBVfzasSQmSC9Evrw%3A1647745013749&source=hp&ei=9Zc2YvO8K62A1e8PsfatOA&iflsig='
                'AHkkrS4AAAAAYjamBb5brjSyEe07dWvfMFcSfXpgWGac&oq=coder&gs_lcp='
                'Cgdnd3Mtd2l6EAMYADIECCMQJzIECCMQJzIECCMQJzIICAAQgAQQsQMyBQgAEIAEMgsILhCABBDHARCvATILCAAQgAQQsQMQgw'
                'EyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgjEOoCECc6EQguEIAEELEDEIMBEMcBENEDOgsILhCABBCxAxCDATo'
                'ICAAQsQMQgwE6CAguELEDEIMBOg4ILhCABBCxAxCDARDUAlCYBVj3CGCPE2gBcAB4AIABgQGIAecEkgEDMC41mAEA'
                'oAEBsAEK&sclient'
                '=gws-wiz')
            speak('Coders Horizen is a Web & Application development company. '
                  'They Are The Finest Team Of Web Designer Developer & Free Lancers. Founded by azim hossen tuhin')
        elif 'sillage' in query:
            webbrowser.open('https://mobile.sillage.site/#/')
            speak('okay sir, opening sillage')
        elif 'open Facebook' in query:
            webbrowser.open_new_tab("https://www.facebook.com")
            speak("Okay sir. Opening Facebook")
        elif 'open Gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            speak("Okay sir. Opening Gmail..")
        elif 'open maps' in query or 'show my location' in query:
            webbrowser.open("https://www.google.com/maps/@26.6235458,87.3614451,16z")
            speak("Okay sir. Opening Maps...")

        # Application opening commands
        elif 'Firefox' in query:
            subprocess.call('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
            speak('okay sir, Opening firefox browser')
        elif 'Chrome' in query:
            webbrowser.open('https://www.google.com')
            speak('okay sir, opening Chrome browser')
        elif 'Brave' in query:
            speak('okay sir, Opening brave browser')
            subprocess.call('C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe')
        elif 'Microsoft' in query:
            speak('okay sir, Opening microsoft edge browser')
            subprocess.Popen('C:\\Program Files (x86)\\\Microsoft\\Edge\\Application\\msedge.exe')
        elif 'pycharm' in query:
            speak('okay sir, Opening py charm')
            subprocess.Popen('C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.3.2\\bin\\pycharm64.exe')
        elif 'memo' in query:
            speak('okay sir, Opening memu')
            subprocess.Popen('D:\\Program Files\\Microvirt\MEmu\\MEmu.exe')
        elif 'IMO' in query:
            speak('okay sir, Opening imo')
            subprocess.Popen('C:\\Users\\RA K IB\\AppData\\Roaming\\Imo Messenger\\ImoDesktopApp.exe')
        elif 'VLC' in query:
            speak('okay sir opening vlc media player')
            subprocess.Popen('C:\\Program Files\\VideoLAN\\VLC\\vlc.exe')
        elif 'zoom' in query:
            speak('okay sir opening zoom')
            subprocess.call('C:\\Users\\RA K IB\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')
        elif 'spotify' in query:
            speak('okay sir opening spotify')
            subprocess.Popen('Spotify.exe')
        elif 'notepad' in query:
            speak('okay sir opening notepad')
            subprocess.Popen('Notepad.exe')
        elif 'activate' in query:
            os.startfile('C:\\Users\\RA K IB\\Desktop\\JARVIS\\intro.mp3')

        # advance commands
        elif 'play' in query:
            song = query.replace('play', '')
            speak('Okay sir, playing ' + song)
            pywhatkit.playonyt(song)
        elif 'calculate' in query:
            speak('Tell me sir what you want to calculate?')
            audio_data = command()
            calculate(audio_data)
        elif 'can you search' in query:
            speak('okay sir, tell me what you want to search?')
            print('okay sir, tell me what you want to search?')
            search = command()
            url = f'https://www.google.com/search?q={search}'
            ur = requests.get(url)
            data = BeautifulSoup(ur.text, 'html.parser')
            result = data.find('div', class_='BNeawe').text
            print(f'sir,{result}')
            speak(f'sir,{result}')
        elif "what's the weather" in query or 'tell me the temperature' in query or "what's the temperature" in query:
            search = 'temperature in dhaka'
            url = f'https://www.google.com/search?q={search}'
            r = requests.get(url)
            data = BeautifulSoup(r.text, 'html.parser')
            temp = data.find('div', class_='BNeawe').text
            print(f'sir, current {search} is {temp}')
            speak(f'sir, current {search} is {temp}')
        elif "weather condition" in query or 'outside weather' in query or "what's the condition of outside" in query:
            search = 'temperature in dhaka'
            url = f'https://www.google.com/search?q={search}'
            r = requests.get(url)
            data = BeautifulSoup(r.text, 'html.parser')
            temp = data.find('div', class_='BNeawe').text
            print(f'sir, current temperature in outside of your home is {temp}')
            speak(f'sir, current temperature in outside of your home is {temp}')
            if temp < '20°':
                speak("It will be better if you wear woolen clothes, sir.")
            elif temp <= '14°':
                speak("Sir, it is very cold outside. If you want to go outside, wear woolen clothes.")
            elif temp >= '25°':
                speak("Sir, the weather is sunny. you do not need to wear woolen clothes to go outside.")

        elif 'click the mouse' in query or 'click mouse' in query or 'click' in query:
            click()
        elif 'take a screenshot' in query or 'take screenshot' in query:
            screenshot()
            speak('Sir, Screenshot taken')
        elif 'internet' in query:
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f'Sir, we have {dl} bit per second downloading speed and {up} bit per second uploading speed')
        elif 'who is' in query:
            person = query.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            speak(info)
        elif 'close current window' in query:
            pyautogui.keyDown('alt')
            pyautogui.press('f4')
            pyautogui.keyUp('alt')
            speak('Current window is closed.')
        elif 'start recording' in query or 'stop recording' in query or 'screen' in query:
            pyautogui.keyDown('win')
            pyautogui.keyDown('alt')
            pyautogui.press('r')
            pyautogui.keyUp('win')
            pyautogui.keyUp('alt')
            if 'start recording' in query:
                speak('Recording started')
            elif 'stop recording' in query:
                speak('Recording stopped')
        elif 'open password field' in query:
            pyautogui.press('enter')
            speak('Sir, enter your pin')
        elif 'shutdown' in query or 'shut down' in query or 'close my PC' in query:
            sec = 5
            os.system(f'shutdown /s /t {sec}')
            speak(f'Okay sir. I will shut down this computer in next {sec} seconds')
        elif 'restart' in query:
            restart()
        elif 'username' in query or 'user' in query or 'user name' in query:
            username()
        elif 'sleep now' in query:
            speak('okay sir, I am going to sleep. Call me anytime')
            sys.exit()


    except:
        return None
    return query


def greeting():
    speak('Matching Data....')
    speak('Access Granted')
    speak('Welcome back Sir. Feeling good to see you.')


if __name__ == '__main__':
    speak('Please enter your credential')
    Pass(input())
    while True:
        command()
