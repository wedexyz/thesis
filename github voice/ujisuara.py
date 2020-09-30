import pyttsx3
import webbrowser
import random
import speech_recognition as sr
import datetime
from playsound import playsound
import os
import sys
import pyautogui

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    print(currentH)
    if currentH >= 0 and currentH < 12:
        playsound('SP.mp3')

    if currentH >= 12 and currentH < 18:
        playsound('SS.mp3')

    if currentH >= 18 and currentH !=0:
        playsound('SM.mp3')

greetMe()
playsound('Hallo.mp3')

def myCommand():
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("mendengarkan...?")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='id-ID')
        print('asistan: ' + query + '\n')
    except sr.UnknownValueError:
        print('menunggu')
        query = myCommand()
    return query
        

if __name__ == '__main__':

    while True:
        query = myCommand()
        query = query.lower()
        
        if 'tes buka youtube' in query:
            playsound('ok.mp3')
            webbrowser.open('www.youtube.com')
        elif 'tes buka google' in query:
            playsound('ok.mp3')
            webbrowser.open('www.google.co.in')
        elif 'aktifkan mode 1' in query:
            #Point(x=185, y=352)
            x=185
            y=352
            pyautogui.moveTo(x,y)
            pyautogui.click(button='left',clicks=2,interval =0.1)

        elif 'aktifkan mode 2' in query:
            #Point(x=189, y=262)
            x=189
            y=262
            pyautogui.moveTo(x,y)
            pyautogui.click(button='left',clicks=2,interval =0.1)
        elif 'matikan mode' in query :
            x=1837
            y=100
            pyautogui.moveTo(x,y)
            pyautogui.click(button='left',clicks=2,interval =0.1)
            pyautogui.press('q') 
        elif 'tes buka gmail' in query:
            playsound('ok.mp3')
            webbrowser.open('www.gmail.com')

        elif 'tidak ada' in query or 'stop' in query:
            playsound('ok.mp3')
            playsound('bye.mp3')
            sys.exit()
           
        elif 'halo' in query:
            playsound('iya.mp3')
        else:
            query = query
            playsound('mencari.mp3')
        playsound('bps.mp3')
    
        
