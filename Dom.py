import speech_recognition as ear # thư viện chuyển giọng nói thành văn bản
import pyttsx3 as mount # thư viện chuyển văn bản thành giọng nói
from datetime import date
from selenium import webdriver
# from splinter import browser
# import requests

DOM_ear = ear.Recognizer() #khai báo tai
DOM_mount = mount.init() #khai báo miệng
DOM_brain = "" #khai báo não
today = date.today()
driver = webdriver.Chrome()

#DOM nghe
while True:
    with ear.Microphone() as mic:
        # Đọc dữ liệu âm thanh từ micrô mặc định
        print("I'm listening...")
        audio_data = DOM_ear.record(mic, duration=5)
        # Dịch ra văn bản
        # you = DOM_ear.recognize_google(audio_data)
        # print(you)
        try:
            you = DOM_ear.recognize_google(audio_data)
        except:
            you = "I can't hear"
        # print(you)

        # print("Dom: ...")
    #you = input()    
    print("You: " + you)

#DOM hiểu
    if you == "":
        DOM_brain = "I can't hear you"
    if "hello" in you:
        DOM_brain = "hello Boss, I'm hear"
    if you == "who are you":
        DOM_brain = "I'm Dom, slave of you"
    if "know me" in you:
        DOM_brain = "You is Thai Tuong Minh, my master, you so handsome and smart. I'm very very happy"
    if "love" in you:
        DOM_brain = "Nooooo, I'm very very hate her"
    if "today" in you:
        DOM_brain = today.strftime("%B %d, %Y")
    if "YouTube" in you:
        driver.get ('https://www.youtube.com/?feature=youtu.be')
        DOM_brain = "Opened YouTube"
    if "Wiki" in you:
        driver.get ('https://vi.wikipedia.org/wiki')
        DOM_brain = "Opened Wikipedia"
    if "Facebook" in you:
        driver.get ('https://www.facebook.com/')
        DOM_brain = "Opened Facebook"      
    if "bye" in you:
        DOM_brain = "Goodbye sir"

#DOM nói
        print("Dom: " + DOM_brain)
        DOM_mount.say(DOM_brain) #kích hoạt nói
        DOM_mount.runAndWait()
        break

    # print (driver.current_url)
    print("Dom: " + DOM_brain)
    DOM_mount.say(DOM_brain) #kích hoạt nói
    DOM_mount.runAndWait()

