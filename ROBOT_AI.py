from tkinter import *
from gtts import gTTS
import playsound
import cv2
import pyttsx3
import datetime
import speech_recognition 
import webbrowser
import os
import subprocess
import requests, json
import imutils
import pyautogui

window = Tk()
global var
global var1

var = StringVar()
var1 = StringVar()
robot_brain=""
robot_ear = speech_recognition.Recognizer()


def listen():
    with speech_recognition.Microphone() as mic:
        var.set("..Đang nghe...")
        window.update()
        print("![0_0]!:..Đang nghe...")  
        audio =robot_ear.record(mic, duration=5)
    try:
        var.set("......")
        window.update()
        print(".....")
        you = robot_ear.recognize_google(audio,language="vi-VN")
    except:
        return "None"
    window.update()
    return you

def play():
    btn1.configure(bg = 'blue')
    btn2.configure(bg = 'blue')
    while True:
        btn1.configure(bg = 'blue')
        btn2.configure(bg = 'blue')
        you = listen().lower()
        
        if "hello" in you:
            robot_brain ="Anyoung Haseyo.Đó là xin chào trong tiếng hàn đấy.Tôi có thể giúp gì được cho bạn không?"
            print("Robot: " +robot_brain)
        
        elif "bạn có thể làm gì" in you:
            robot_brain=("""Bot có thể giúp bạn thực hiện các câu lệnh sau đây:
            1. Chào hỏi
            2. Hiển thị thời gian
            3. Dự báo thời tiết
            4. Mở trình duyệt
            5. Bật định vị
            6. Chụp màn hình
            7. Chụp ảnh
            8. Tắt và khởi động lại máy tính""")
            print("Robot: " +robot_brain)
            
        elif "hôm nay là" in you:
            now = datetime.datetime.now()
            robot_brain = "Hôm nay là ngày %d tháng %d năm %d" % (now.day, now.month, now.year) 
            print("Robot: " +robot_brain)
          
        elif "thời gian" in you:
            now = datetime.datetime.now()
            robot_brain ="Bây giờ là %d giờ %d phút" % (now.hour, now.minute)
            print("Robot: " +robot_brain)
            
        elif "dự báo thời tiết"in you:
            robot_brain="Và sau đây là kết quả"      
            api_address = "http://api.openweathermap.org/data/2.5/weather?q=Vinh&appid=ce2eb5a530d90362a642284c01916cc4"
            data_link = requests.get(api_address)
            api_data = data_link.json()

            temp_city = ((api_data['main']['temp']) - 273.15)
            print("Nhiệt độ hôm nay: {:.2f} Độ C".format(temp_city))
            weather_desc = api_data['weather'][0]['description']
            print("Mô tả thời tiết :",weather_desc)
            humidity = api_data['main']['humidity']
            print("Độ ẩm           :",humidity,'%')
            windspeed = api_data['wind']['speed']
            print("Tốc độ gió      :",windspeed,'m/s')
            pressure =api_data['main']['pressure']
            print("áp suất         :",pressure,'hPa')
            print("Robot: " +robot_brain)
          
        elif "mở trình duyệt" in you:
            robot_brain="Đang mở trình duyệt"
            print("Robot: " +robot_brain)
            you = you.replace("search","")
            webbrowser.open_new_tab(you)

        elif "bật định vị"in you:
            robot_brain = "Sau đây là kết quả định vị của bạn"
            print("Robot: " +robot_brain)
            res = requests.get('https://ipinfo.io/')
            data = res.json()
            city = data['city']
            location = data['loc'].split(',')
            latitude = location[0]
            longitude = location[1]

            print("Vĩ độ : ", latitude)
            print("Kinh độ : ", longitude)
            print("Thành phố : ", city)

        elif "chụp màn hình" in you:        
            pyautogui.screenshot("screenshot.png")
            image = cv2.imread("screenshot.png")
            cv2.imshow("Windows photo viewer", imutils.resize(image, width=900))        
            cv2.waitKey(0)
            robot_brain="Màn hình đã được chụp"
            print("Robot: " +robot_brain)
          
        elif "chụp ảnh"in you:
            camera = cv2.VideoCapture(0)
            for i in range(1):
                return_value, image = camera.read()
                cv2.imwrite('Image''.png', image)
                cv2.imshow("Windows photo viewer", imutils.resize(image, width=900))
                cv2.waitKey(0)  
            robot_brain="okay, ảnh đã được chụp"
            print("Robot: " +robot_brain)
            del(camera)
            
        elif "khởi động lại máy tính" in you:
            robot_brain= "Okay,máy tính của bạn sẽ khởi động lại "
            os.system("shutdown -r ")
            
        elif "tắt máy" in you:
            robot_brain = "Ok , máy tính của bạn sẽ tắt sau 10 giây" 
            print("Robot: " +robot_brain)
            subprocess.call(["shutdown", "-f", "-s", "-t", "10"]) 

        elif "bye" in you:
            robot_brain=("Hi vọng sẽ sớm gặp lại bạn")
            print("Robot: " +robot_brain)
            var.set("..Kết Thúc..")
            window.update()
            tts = gTTS(text = robot_brain, lang = 'vi' , slow= False)
            tts.save("ai.mp3")
            playsound.playsound("ai.mp3")
            os.remove("ai.mp3")
            break
        else:
            robot_brain="Tôi có thể giúp gì được cho bạn?"
            print("Robot: " +robot_brain)
               
        tts = gTTS(text = robot_brain, lang = 'vi' , slow= False)
        tts.save("ai.mp3")
        playsound.playsound("ai.mp3")
        os.remove("ai.mp3")

def speak():           
    tts = gTTS(text = robot_brain, lang = 'vi' , slow= False)
    tts.save("ai.mp3")
    playsound.playsound("ai.mp3")
    os.remove("ai.mp3")
           
def update(ind):
    frame = frames[(ind)%1]
    label.configure(image=frame)
    window.after(1, update, ind)

label1 = Label(window, textvariable = var, bg = '#ADD8E6')
label1.config(font=("Courier", 20))
var.set('LIAM')
label1.pack()

frames = [PhotoImage(file='e2.GIF',format = 'GIF -index %i' %(i)) for i in range(10)]
window.title('ROBOT THÔNG MINH')

label = Label(window, width = 340, height = 450)
label.pack()
window.after(0, update, 0)

btn1 = Button(text='START', width=30, command=play, bg='#5C85FB')
btn1.config(font=("Courier", 15))
btn1.pack()

btn2 = Button(text='EXIT', width=30, command=window.quit, bg='#5C85FB')
btn2.config(font=("Courier", 15))
btn2.pack()

window.mainloop()
