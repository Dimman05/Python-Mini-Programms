# Imports
import datetime
import calendar
import wikipedia
import socket
from requests import get
import pyttsx3
import pyjokes
import speech_recognition as sr
import webbrowser
import PyPDF2
import subprocess
import time 
import os
import winshell
import ctypes


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greeting():
    time = int(datetime.datetime.now().time().hour)

    if time > 0 and time < 12:
        speak("Good  Morning ")
    if time >= 12 and time < 18:
        speak("Good afternoon")
    if time >= 18 and time <= 23:
        speak("Good  evening")

def listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-US')
        print(f'User: {query}')

    except Exception as e :
        print(e)
        print("Unable to recognize")
        return  "None"

    return query

# command = listen.lower()

def current_time():
    time = datetime.datetime.now()
    current_time = time.time()
    result = f'It is {current_time.strftime("%H:%M")}'
    if result[0] == '0':
        result[0].replace('0', '')
    if result[3] == '0':
        result[3].replace('0', '')
    speak(result)

def today():

    date = datetime.datetime.today()
    print(date.strftime("%Y-%m-%d"))
    date = date.strftime("%Y-%m-%d").replace('-', '', 3)
    speak(date)

def show_calendar():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    speak("This is the month's calendar: ")
    print(calendar.month(year, month))

def random_wiki():
    page = wikipedia.random()
    result = wikipedia.summary(page)
    print (result)

def my_ip():
    host = socket.gethostname()
    local_ip = socket.gethostbyname(host)
    public_ip = get('https://api.ipify.org').text

    speak("Here is your host name and your ip")
    print(f"Host: {host}")
    print(f"Local IP: {local_ip}")
    print(f'Public IP: {public_ip}')

def joke():
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)

def open_google():
    speak('Here you go to google \n')
    webbrowser.open(url='https://www.google.com')

def open_wikipedia():
    speak('Here you go to wikipedia \n')
    webbrowser.open(url='https://www.wikipedia.org/')

def open_stackoverflow():
    speak('Here you go to Stack Overflow \n')
    speak('Happy Coding')
    webbrowser.open(url='https://stackoverflow.com/')

def open_gmail():
    speak('Here you go to your emails \n')
    webbrowser.open(url='https://mail.google.com/')

def open_youtube():
    speak('Here you go to Youtube \n')
    webbrowser.open(url='https://youtube.com')

def close():
    speak('Ok sir. Bye Bye')
    exit()

def open_oneNote():
    speak('Here you go to One Note \n')
    webbrowser.open(url='https://www.onenote.com')

def open_youtubeMusic():
    speak('Here you go to Youtube Music')
    webbrowser.open(url='https://music.youtube.com/')

def open_github():
    speak('Here you go to Github \n')
    webbrowser.open(url='https://www.github.com')

def open_degoo():
    speak('Here you go to Degoo \n')
    webbrowser.open(url='https://www.degoo.com')

def open_googleDrive():
    speak('Here you go to Google Drive \n')
    webbrowser.open(url='https://drive.google.com/')

def open_spotify():
    speak('Here you go to Spotify \n')
    webbrowser.open(url='https://www.spotify.com')

def audiobook():

    # Make it stop with keyboard interruoption 
    speak('Enter the path of the pdf file and i will read it for you')
    file = input('Enter the path of the pdf file: ')
    pdf_file = open(file, 'rb')

    pdfReader = PyPDF2.PdfFileReader(pdf_file)
    
    speak('Do you want to start reading from a specific page?')
    speak('If yes enter the page here')

    pages = pdfReader.numPages
    start = int(input('>> '))
    
    try:
        if start != " ":
            for num in range(start, pages):
                try:
                    page = pdfReader.getPage(start)
                    text = page.extractText()
                    speak(text)
                except Exception as e:
                    speak(e)
    except Exception as e:
        speak(e)

def open_calc():
    try:
        print('Opening Calculator ...')
        speak('Opening Calculator')
        subprocess.Popen('C:\\Windows\\System32\\calc.exe')
    except FileNotFoundError:
        print('The application does not exists')
        speak('Sorry the application does not exist')

def open_notepad():
    try:
        print('Opening Notepad ...')
        speak('Opening Notepad')
        subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
    except FileNotFoundError:
        print('The application does not exists')
        speak('Sorry the application does not exist')

def open_wordpad():
    try:
        print('Opening Wordpad...')
        speak('Opening Wordpad')
        subprocess.Popen('C:\\Windows\\System32\\write.exe')
    except FileNotFoundError:
        print('The application does not exists')
        speak('Sorry the application does not exist')

def create_txt():
    speak('How do you like to name it?')
    name = input('>>')
    file = open(f'{name}.txt', "w+")
    print('Creating the file...')

def open_airconsole():
    speak('Here you go to airconsole \n')
    webbrowser.open(url='https://airconsole.com')

def lock():
    speak('Locking Desktop')
    ctypes.windll.user32.LockWorkStation()

def shutdown():
    speak('Shutting down Computer')
    subprocess.call('shutdown / p/f')

def restart():
    speak('Restarting Computer')
    subprocess.call(["shutdown", "/r"])

def hibernate():
    speak('Hibernate Computer')
    subprocess.call("shutdown / h")

def log_out():
    speak('Logging out')
    time.sleep(5)
    subprocess.call(["shutdown", "/l"])

def empty_bin():
    winshell.recycle_bin().empty(confirm=True, show_progress=True, sound=False)
    speak('Bin is empty now')

def make_note():
    speak("What should i write, sir")
    note = listen()
    file = open('jarvis.txt', 'w')
    file.write(note)

def show_notes():
    speak("Showing notes")
    file = open('jarvis.txt', 'r')
    print(file.read())
    speak(file.read())

