import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit as kit
import os
import wikipedia
import datetime
import pyjokes
import requests
from bs4 import BeautifulSoup
import pyautogui
import json
import PyPDF2




'''
**********voice changes**********
'''

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices',"Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0") #"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")   #voices[1].id)  
Assistant.setProperty('rate',150)

'''
from here starts
'''

def Speak(audio):
    Assistant.say(audio)
    Assistant.runAndWait()


hour = int(datetime.datetime.now().hour)
if hour >= 0 and hour < 11:
    Speak("iinddrraya kaalai vanakkam Boss")
elif hour >= 11 and hour < 16:
    Speak("Good afternoon Boss")
elif hour >= 16 and hour < 19:
    Speak("Good evening Boss")
else:
    Speak("Good night Boss")


Speak("hello , Nanthan Alexa , Boss ungaluku enna vendum")

def takeCommand():
    r = sr.Recognizer()
    r.energy_threshold = 4000

    with sr.Microphone() as source:
        # print(sr.Microphone.list_microphone_names())
        print("Listening............")
        r.pause_threshold = 0.5
        audio = r.listen(source)
        # r.adjust_for_ambient_noise(source, duration=5)
        r.adjust_for_ambient_noise(source)

    try:
        print("Recognizing........")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
          # print(e)
         print("say again.....")
         Speak("say again.....")
         return "None"
    return query


def Takecommand():
    r = sr.Recognizer()
    r.energy_threshold = 4000

    with sr.Microphone() as source:
        # print(sr.Microphone.list_microphone_names())
        print("Listening............")
        r.pause_threshold = 0.5
        audio = r.listen(source)
        # r.adjust_for_ambient_noise(source, duration=5)
        r.adjust_for_ambient_noise(source)

    try:
        print("Recognizing........")
        query = r.recognize_google(audio, language='hi')
        print(f"user said: {query}\n")

    except Exception as e:
          # print(e)
         print("say again.....")
         Speak("say again.....")
         return "None"
    return query.lower()

if __name__ == '__main__':
    while True:
        query = takeCommand()

        if 'hello' in query:
            print("hello boss")
            Speak("Hello Boss!")

        elif "my profile" in query:
            webbrowser.open("https://jairam12.github.io/jairam/")

        elif "who made you" in query:
            print("Jairam,I am made by python")
            Speak('En Boss ennai , vungal Voice assisstant . Ennai python nil vuruvakinar')

        elif "thank you" in query:
            print('You are welcome Boss!')
            Speak('You are welcome Boss!')

        elif "tell me your powers" in query:#change
            Speak("i can help to do lot many things like..,"
                  "i can tell you the current time and date,"
                  "i can tell you the current weather,"
                  "i can tell you battery and cpu usage,"
                  "i can create the reminder list,"
                  "i can take screenshots,"
                  "i can send email to your boss or family or your friend,"
                  "i can shut down or logout or hibernate your system,"
                  "i can tell you non funny jokes,"
                  "i can open any website,"
                  "i can search the thing on wikipedia,"
                  "i can change my voice from male to female and vice-versa"
                  "And yes one more thing, My boss is working on this system to add more features...,"
                  "tell me what can i do for you??")

        elif "mail check" in query:
            print("which one you choose")
            Speak("which one you choose")
            a = takeCommand()
            if "send mail" in a:
                str = "You have chosen to send an email"
                Speak(str)
                rec = "jsjairam01@gmail.com"
                # rec = input()
                speak("Please speak the body of your mail")
                print("Please speak the body of your mail")
                msg = takeCommand()
                Speak("You have spoken the messaage")
                Speak(msg)
                print(msg)
                server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
                server.login("jsjairam02@gmail.com", "jai11.12.01")
                server.sendmail("jsjairam02@gmail.com", rec, msg)
                server.quit()
                str = "The email has been Sent"
                speak(str)
                print(str)
            elif "read mail" in a:
                str = "You have chosen to read email"
                Speak(str)
                server = e.connect("imap.gmail.com", "jsjairam02@gmail.com", "jai11.12.01")
                server.listids()
                Speak("Please say the Serial Number of the email you wanna read starting from latest")
                print("Please say the Serial Number of the email you wanna read starting from latest")
                b = int(input())
                # b=int(takeCommand())
                email = server.mail(server.listids()[b])
                str = "The email is from: "
                Speak(str)
                print(email.from_addr)
                Speak(email.from_addr)
                str = "The subject at the email is:"
                Speak(str)
                print(email.title)
                Speak(email.title)
                str = "The body of email is :"
                Speak(str)
                print(email.body)
                Speak(email.body)
            elif "exit" in a:
                str = "You have chosen to exit, bye bye"
                Speak(str)
                exit(1)


        elif "who are you" in query:
            print('I am Alexa. Your voice assistant')
            Speak('I am Alexa. Your voice assistant')

        elif "YouTube search" in query:
            #kit.playonyt("anna")
            Speak("what you search, Boss!")
            kit.playonyt(takeCommand())
            Speak("Done Boss!")

        elif "Google search" in query:
            Speak("what you search,Boss!")
            query = takeCommand()
            Speak("Ok Boss,This is what I found for your search")
            query = query.replace("Alexa", "")
            query = query.replace("search google", "")
            kit.search(query)
            Speak("Done Boss!")

        elif 'website' in query:
            Speak("Ok Boss , Lauching.........")
            query = query.replace("jarvis", "")
            query = query.replace("website", "")
            web1 = query.replace("open","")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            Speak("Launched!")

        elif 'IP address' in query:
            ip = requests.get('https://api.ipify.org').text 
            print(f"your IP address is {ip}")
            Speak(f"your IP address is {ip}")


        elif 'shut down system' in query:
            os.system('shutdown /s /t 5')

        elif 'restart system' in query:
            os.system('shutdown /r /t 5')

        elif 'read' in query:
            file = open("python.pdf", "rb")
            reader = PyPDF2.PdfFileReader(file)
            pages = reader.numPages
            print(pages)
            Speak("enter page number Boss")
            print("enter the page number:")
            p = int(input())#10
            page = reader.getPage(p)
            text = page.extractText()
            print(text)
            Speak(text)

        elif 'cook' in query: #activate how to do mod
            from pywikihow import search_wikihow
            Speak("how to do mode is activated ")
            while True:
                Speak("please tell me , how to do mode is closed")
                how = takeCommand()
                try:
                    if "exit" in how:
                        Speak("okay Boss,how to do mode is closed")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how,max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        Speak(how_to[0].summary)
                except Exception as e:
                    Speak("sorry Boss , i am not able to find this")


        elif 'launch' in query:
            Speak("Tell Me The Name of the Website Boss")
            name = takeCommand()
            web = ' https://www.' + name + '.com '
            webbrowser.open(web)
            Speak("Done Boss!")

        elif "repeat" in query:  # Repeat what you said
            Speak('repeating')
            print('thirumbavum..........')
            query = query.replace('repeat', "")
            print(query)
            Speak(query)

        elif 'wikipedia' in query:
            Speak("wikipedia searching.......")
            query = query.replace("jarvis", "")
            query = query.replace("wikipedia", "")
            wiki = wikipedia.summary(query,2)
            Speak(f"According To Wikipedia : {wiki}")

        elif "online music" in query:
            Speak("tell me the song name!")
            p = takeCommand()
            webbrowser.open(f"https://soundcloud.com/search?q={p}")


        elif 'newspaper' in query:
            url = "https://timesofindia.indiatimes.com/home/headlines"
            page_request = requests.get(url)
            data = page_request.content
            soup = BeautifulSoup(data, "html.parser")
            counter = 0
            for divtag in soup.find_all('div', {'class': 'headlines-list'}):
                for ultag in divtag.find_all('ul', {'class': 'clearfix'}):
                    if (counter <= 10):
                        for litag in ultag.find_all('li'):
                            counter = counter + 1
                            print(str(counter) + " - https://timesofindia.indiatimes.com" + litag.find('a')['href'])
                            # print(str(counter) + "." + litag.text + " - https://timesofindia.indiatimes.com" + litag.find('a')['href'])
            Speak("i gave Headlines link,get check it out Boss")

        elif 'WhatsApp message' in query:#don't no time and some mistake in dad
            Speak("whatsapp") #https://youtu.be/JT3Tuq8Ww7E
            Speak("Tell me the Name of the Person!, Boss")
            name = takeCommand()
            if "dad" in name:
                Speak('Tell me the Message!')
                msg = takeCommand()
                Speak('Tell me the Time Boss!')
                Speak('Time in Hour!')
                print("hours")
                hour = int(input())
                Speak('Time in Minutes!')
                print("min")
                min = int(input())
                kit.sendwhatmsg("+919444404759", msg,hour,min)
                Speak("Ok Boss , Sending Whatsapp Message!")
            else:
                Speak("number")
                phone = takeCommand()
                Speak('Tell me the Message!')
                msg = takeCommand()
                Speak('Tell me the Time Boss!')
                Speak('Time in Hour!')
                print("hours")
                hour = int(input())
                Speak('Time in Minutes!')
                print("min")
                min = int(input())
                kit.sendwhatmsg(f'+91{phone}', msg, hour, min)



        elif 'play music' in query:
            print("music")
            Speak("Tell me the Name of the song!, Boss")
            musicName = takeCommand()
            if "song name 1" in musicName:
                os.startfile('C:\\Users\\jairam\\Desktop\\music')

            elif "song name 2" in musicName:
                os.startfile('C:\\Users\\jairam\\Desktop\\music')
            Speak('Your Song has been Started!, Enjoy Boss')


        elif 'screenshot' in query:
            print('screenshot')
            screenshot = pyautogui.screenshot()
            screenshot.save(r'E:\project\Alexa voice assistant\screenshot1.png')
            Speak('Here your sreenshot')


        elif 'open whatsapp' in query:#command wrg
            print('whatsapp')
            Speak('opening whatsapp Boss!')
            os.startfile('Whatsapp:')

        elif 'open Telegram' in query:
            print('Telegram')
            Speak('opening Telegram Boss!')
            os.startfile('telegram:')

        elif "open google" in query:
            print('open google')
            webbrowser.open("google.com")

        elif 'time' in query:
            Time = datetime.datetime.now().strftime("%H: %M : %S")
            print(Time)
            Speak(Time)

        elif 'date' in query:
            date = datetime.datetime.now().strftime("%d: %m: %Y")
            print(date)
            Speak(date)

        elif 'joke' in query:
            get = pyjokes.get_joke()
            Speak(get)
            print(get)

        elif 'location' in query:
            Speak('What is the location?')
            location = takeCommand()
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.open(url)
            Speak('Here is the location ' + location)

        elif 'temperature' in query:
            Speak("which city temperature Do you want Boss!")
            search = takeCommand() #temperature in chennai
            url = "https://www.google.co.in/search?q=" + search
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            print("current " +search+ " is " +temp)
            Speak(f"current {search} is{temp} ")

        elif "thank you" in query:
            print('You are welcome Boss!')
            Speak('You are welcome Boss!')

        elif 'open CMD' in query:
            cmd_Path = "C:\\Windows\\system32\\Cmd.exe"                       #path of cmd.exe
            Speak("opening cmd")
            os.startfile(cmd_Path)

        elif 'bye' in query: #Here I am using break statement
            Speak("Good Bye Boss ! ")
            break

        elif 'power off' in query: #Here I am using break statement
            Speak("ok Boss ")
            break

        elif 'start game' in query:
            from tkinter import Tk, ttk, Button
            from tkinter import messagebox
            from random import randint

            ActivePlayer = 1
            p1 = []
            p2 = []
            mov = 0


            def SetLayout(id, player_symbol):
                if id == 1:
                    b1.config(text=player_symbol)
                    b1.state(['disabled'])
                elif id == 2:
                    b2.config(text=player_symbol)
                    b2.state(['disabled'])
                elif id == 3:
                    b3.config(text=player_symbol)
                    b3.state(['disabled'])
                elif id == 4:
                    b4.config(text=player_symbol)
                    b4.state(['disabled'])
                elif id == 5:
                    b5.config(text=player_symbol)
                    b5.state(['disabled'])
                elif id == 6:
                    b6.config(text=player_symbol)
                    b6.state(['disabled'])
                elif id == 7:
                    b7.config(text=player_symbol)
                    b7.state(['disabled'])
                elif id == 8:
                    b8.config(text=player_symbol)
                    b8.state(['disabled'])
                elif id == 9:
                    b9.config(text=player_symbol)
                    b9.state(['disabled'])


            def CheckWinner():
                global mov
                winner = -1

                if (1 in p1) and (2 in p1) and (3 in p1):
                    winner = 1
                if (1 in p2) and (2 in p2) and (3 in p2):
                    winner = 2

                if (4 in p1) and (5 in p1) and (6 in p1):
                    winner = 1
                if (4 in p2) and (5 in p2) and (6 in p2):
                    winner = 2

                if (7 in p1) and (8 in p1) and (9 in p1):
                    winner = 1
                if (7 in p2) and (8 in p2) and (9 in p2):
                    winner = 2

                if (1 in p1) and (4 in p1) and (7 in p1):
                    winner = 1
                if (1 in p2) and (4 in p2) and (7 in p2):
                    winner = 2

                if (2 in p1) and (5 in p1) and (8 in p1):
                    winner = 1
                if (2 in p2) and (5 in p2) and (8 in p2):
                    winner = 2

                if (3 in p1) and (6 in p1) and (9 in p1):
                    winner = 1
                if (3 in p2) and (6 in p2) and (9 in p2):
                    winner = 2

                if (1 in p1) and (5 in p1) and (9 in p1):
                    winner = 1
                if (1 in p2) and (5 in p2) and (9 in p2):
                    winner = 2

                if (3 in p1) and (5 in p1) and (7 in p1):
                    winner = 1
                if (3 in p2) and (5 in p2) and (7 in p2):
                    winner = 2

                if winner == 1:
                    messagebox.showinfo(title="Congratulations.",
                                        message="Player 1 is the winner")
                elif winner == 2:
                    messagebox.showinfo(title="Congratulations.",
                                        message="Player 2 is the winner")
                elif mov == 9:
                    messagebox.showinfo(title="Draw",
                                        message="It's a Draw!!")


            def ButtonClick(id):
                global ActivePlayer
                global p1, p2
                global mov

                if (ActivePlayer == 1):
                    SetLayout(id, "X")
                    p1.append(id)
                    mov += 1
                    root.title("Tic Tac Toe : Player 2")
                    ActivePlayer = 2

                elif (ActivePlayer == 2):
                    SetLayout(id, "O")
                    p2.append(id)
                    mov += 1
                    root.title("Tic Tac Toe : Player 1")
                    ActivePlayer = 1
                CheckWinner()


            def AutoPlay():
                global p1;
                global p2
                Empty = []
                for cell in range(9):
                    if (not ((cell + 1 in p1) or (cell + 1 in p2))):
                        Empty.append(cell + 1)
                try:
                    RandIndex = randint(0, len(Empty) - 1)
                    ButtonClick(Empty[RandIndex])
                except:
                    pass


            def EnableAll():
                b1.config(text=" ")
                b1.state(['!disabled'])
                b2.config(text=" ")
                b2.state(['!disabled'])
                b3.config(text=" ")
                b3.state(['!disabled'])
                b4.config(text=" ")
                b4.state(['!disabled'])
                b5.config(text=" ")
                b5.state(['!disabled'])
                b6.config(text=" ")
                b6.state(['!disabled'])
                b7.config(text=" ")
                b7.state(['!disabled'])
                b8.config(text=" ")
                b8.state(['!disabled'])
                b9.config(text=" ")
                b9.state(['!disabled'])


            def Restart():
                global p1, p2, mov, ActivePlayer
                p1.clear();
                p2.clear()
                mov, ActivePlayer = 0, 1
                root.title("Tic Tac Toe : Player 1")
                EnableAll()


            root = Tk()
            root.title("Tic Tac toe : Player 1")
            st = ttk.Style()
            st.configure("my.TButton", font=('Chiller', 24, 'bold'))

            b1 = ttk.Button(root, text=" ", style="my.TButton")
            b1.grid(row=1, column=0, sticky="nwse", ipadx=50, ipady=50)
            b1.config(command=lambda: ButtonClick(1))

            b2 = ttk.Button(root, text=" ", style="my.TButton")
            b2.grid(row=1, column=1, sticky="snew", ipadx=50, ipady=50)
            b2.config(command=lambda: ButtonClick(2))

            b3 = ttk.Button(root, text=" ", style="my.TButton")
            b3.grid(row=1, column=2, sticky="snew", ipadx=50,
                    ipady=50)
            b3.config(command=lambda: ButtonClick(3))

            b4 = ttk.Button(root, text=" ", style="my.TButton")
            b4.grid(row=2, column=0, sticky="snew", ipadx=50,
                    ipady=50)
            b4.config(command=lambda: ButtonClick(4))

            b5 = ttk.Button(root, text=" ", style="my.TButton")
            b5.grid(row=2, column=1, sticky="snew", ipadx=50,
                    ipady=50)
            b5.config(command=lambda: ButtonClick(5))

            b6 = ttk.Button(root, text=" ", style="my.TButton")
            b6.grid(row=2, column=2, sticky="snew", ipadx=50,
                    ipady=50)
            b6.config(command=lambda: ButtonClick(6))

            b7 = ttk.Button(root, text=" ", style="my.TButton")
            b7.grid(row=3, column=0, sticky="snew", ipadx=50,
                    ipady=50)
            b7.config(command=lambda: ButtonClick(7))

            b8 = ttk.Button(root, text=" ", style="my.TButton")
            b8.grid(row=3, column=1, sticky="snew", ipadx=50,
                    ipady=50)
            b8.config(command=lambda: ButtonClick(8))

            b9 = ttk.Button(root, text=" ", style="my.TButton")
            b9.grid(row=3, column=2, sticky="snew", ipadx=50,
                    ipady=50)
            b9.config(command=lambda: ButtonClick(9))

            Button(text="New Game..", font=('Courier new', 22, 'bold'), bg='blue', fg='white',
                   border=5, width=4, command=lambda: Restart()).grid(row=0, column=1, sticky="we")
            root.resizable(0, 0)
            root.mainloop()

        elif "mask on" in query:#os.system("Face-Mask-Detection.py")
            from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
            from tensorflow.keras.preprocessing.image import img_to_array
            from tensorflow.keras.models import load_model
            from imutils.video import VideoStream
            import numpy as np
            import imutils
            import time
            import cv2
            import os


            def detect_and_predict_mask(frame, faceNet, maskNet):
                # grab the dimensions of the frame and then construct a blob
                # from it
                (h, w) = frame.shape[:2]
                blob = cv2.dnn.blobFromImage(frame, 1.0, (224, 224),
                                             (104.0, 177.0, 123.0))

                # pass the blob through the network and obtain the face detections
                faceNet.setInput(blob)
                detections = faceNet.forward()
                print(detections.shape)

                # initialize our list of faces, their corresponding locations,
                # and the list of predictions from our face mask network
                faces = []
                locs = []
                preds = []

                # loop over the detections
                for i in range(0, detections.shape[2]):
                    # extract the confidence (i.e., probability) associated with
                    # the detection
                    confidence = detections[0, 0, i, 2]

                    # filter out weak detections by ensuring the confidence is
                    # greater than the minimum confidence
                    if confidence > 0.5:
                        # compute the (x, y)-coordinates of the bounding box for
                        # the object
                        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                        (startX, startY, endX, endY) = box.astype("int")

                        # ensure the bounding boxes fall within the dimensions of
                        # the frame
                        (startX, startY) = (max(0, startX), max(0, startY))
                        (endX, endY) = (min(w - 1, endX), min(h - 1, endY))

                        # extract the face ROI, convert it from BGR to RGB channel
                        # ordering, resize it to 224x224, and preprocess it
                        face = frame[startY:endY, startX:endX]
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
                        face = cv2.resize(face, (224, 224))
                        face = img_to_array(face)
                        face = preprocess_input(face)

                        # add the face and bounding boxes to their respective
                        # lists
                        faces.append(face)
                        locs.append((startX, startY, endX, endY))

                # only make a predictions if at least one face was detected
                if len(faces) > 0:
                    # for faster inference we'll make batch predictions on *all*
                    # faces at the same time rather than one-by-one predictions
                    # in the above `for` loop
                    faces = np.array(faces, dtype="float32")
                    preds = maskNet.predict(faces, batch_size=32)

                # return a 2-tuple of the face locations and their corresponding
                # locations
                return (locs, preds)


            # load our serialized face detector model from disk
            prototxtPath = r"face_detector\deploy.prototxt"
            weightsPath = r"face_detector\res10_300x300_ssd_iter_140000.caffemodel"
            faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)

            # load the face mask detector model from disk
            maskNet = load_model("mask_detector.model")

            # initialize the video stream
            print("[INFO] starting video stream...")
            vs = VideoStream(src=0).start()

            # loop over the frames from the video stream
            while True:
                # grab the frame from the threaded video stream and resize it
                # to have a maximum width of 400 pixels
                frame = vs.read()
                frame = imutils.resize(frame, width=400)

                # detect faces in the frame and determine if they are wearing a
                # face mask or not
                (locs, preds) = detect_and_predict_mask(frame, faceNet, maskNet)

                # loop over the detected face locations and their corresponding
                # locations
                for (box, pred) in zip(locs, preds):
                    # unpack the bounding box and predictions
                    (startX, startY, endX, endY) = box
                    (mask, withoutMask) = pred

                    # determine the class label and color we'll use to draw
                    # the bounding box and text
                    label = "Mask" if mask > withoutMask else "No Mask"
                    color = (0, 255, 0) if label == "Mask" else (0, 0, 255)

                    # include the probability in the label
                    label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)

                    # display the label and bounding box rectangle on the output
                    # frame
                    cv2.putText(frame, label, (startX, startY - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
                    cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)

                # show the output frame
                cv2.imshow("Frame", frame)
                key = cv2.waitKey(1) & 0xFF

                # if the `q` key was pressed, break from the loop
                if key == ord("q"):
                    break

            # do a bit of cleanup
            cv2.destroyAllWindows()
            vs.stop()

        elif 'draw' in query:
            Speak("name Boss!")
            name = takeCommand()
            if "Pikachu" in name:
                import turtle


                def getPosition(x, y):
                    turtle.setx(x)
                    turtle.sety(y)
                    print(x, y)


                class Pikachu:

                    def __init__(self):
                        self.t = turtle.Turtle()
                        t = self.t
                        t.pensize(3)
                        t.speed(9)
                        t.ondrag(getPosition)

                    def noTrace_goto(self, x, y):
                        self.t.penup()
                        self.t.goto(x, y)
                        self.t.pendown()

                    def leftEye(self, x, y):
                        self.noTrace_goto(x, y)
                        t = self.t
                        t.seth(0)
                        t.fillcolor('#333333')
                        t.begin_fill()
                        t.circle(22)
                        t.end_fill()

                        self.noTrace_goto(x, y + 10)
                        t.fillcolor('#000000')
                        t.begin_fill()
                        t.circle(10)
                        t.end_fill()

                        self.noTrace_goto(x + 6, y + 22)
                        t.fillcolor('#ffffff')
                        t.begin_fill()
                        t.circle(10)
                        t.end_fill()

                    def rightEye(self, x, y):
                        self.noTrace_goto(x, y)
                        t = self.t
                        t.seth(0)
                        t.fillcolor('#333333')
                        t.begin_fill()
                        t.circle(22)
                        t.end_fill()

                        self.noTrace_goto(x, y + 10)
                        t.fillcolor('#000000')
                        t.begin_fill()
                        t.circle(10)
                        t.end_fill()

                        self.noTrace_goto(x - 6, y + 22)
                        t.fillcolor('#ffffff')
                        t.begin_fill()
                        t.circle(10)
                        t.end_fill()

                    def mouth(self, x, y):
                        self.noTrace_goto(x, y)
                        t = self.t

                        t.fillcolor('#88141D')
                        t.begin_fill()
                        # 下嘴唇
                        l1 = []
                        l2 = []
                        t.seth(190)
                        a = 0.7
                        for i in range(28):
                            a += 0.1
                            t.right(3)
                            t.fd(a)
                            l1.append(t.position())

                        self.noTrace_goto(x, y)

                        t.seth(10)
                        a = 0.7
                        for i in range(28):
                            a += 0.1
                            t.left(3)
                            t.fd(a)
                            l2.append(t.position())

                        # 上嘴唇

                        t.seth(10)
                        t.circle(50, 15)
                        t.left(180)
                        t.circle(-50, 15)

                        t.circle(-50, 40)
                        t.seth(233)
                        t.circle(-50, 55)
                        t.left(180)
                        t.circle(50, 12.1)
                        t.end_fill()

                        # 舌头
                        self.noTrace_goto(17, 54)
                        t.fillcolor('#DD716F')
                        t.begin_fill()
                        t.seth(145)
                        t.circle(40, 86)
                        t.penup()
                        for pos in reversed(l1[:20]):
                            t.goto(pos[0], pos[1] + 1.5)
                        for pos in l2[:20]:
                            t.goto(pos[0], pos[1] + 1.5)
                        t.pendown()
                        t.end_fill()

                        # 鼻子
                        self.noTrace_goto(-17, 94)
                        t.seth(8)
                        t.fd(4)
                        t.back(8)

                    # 红脸颊
                    def leftCheek(self, x, y):
                        turtle.tracer(False)
                        t = self.t
                        self.noTrace_goto(x, y)
                        t.seth(300)
                        t.fillcolor('#DD4D28')
                        t.begin_fill()
                        a = 2.3
                        for i in range(120):
                            if 0 <= i < 30 or 60 <= i < 90:
                                a -= 0.05
                                t.lt(3)
                                t.fd(a)
                            else:
                                a += 0.05
                                t.lt(3)
                                t.fd(a)
                        t.end_fill()
                        turtle.tracer(True)

                    def rightCheek(self, x, y):
                        t = self.t
                        turtle.tracer(False)
                        self.noTrace_goto(x, y)
                        t.seth(60)
                        t.fillcolor('#DD4D28')
                        t.begin_fill()
                        a = 2.3
                        for i in range(120):
                            if 0 <= i < 30 or 60 <= i < 90:
                                a -= 0.05
                                t.lt(3)
                                t.fd(a)
                            else:
                                a += 0.05
                                t.lt(3)
                                t.fd(a)
                        t.end_fill()
                        turtle.tracer(True)

                    def colorLeftEar(self, x, y):
                        t = self.t
                        self.noTrace_goto(x, y)
                        t.fillcolor('#000000')
                        t.begin_fill()
                        t.seth(330)
                        t.circle(100, 35)
                        t.seth(219)
                        t.circle(-300, 19)
                        t.seth(110)
                        t.circle(-30, 50)
                        t.circle(-300, 10)
                        t.end_fill()

                    def colorRightEar(self, x, y):
                        t = self.t
                        self.noTrace_goto(x, y)
                        t.fillcolor('#000000')
                        t.begin_fill()
                        t.seth(300)
                        t.circle(-100, 30)
                        t.seth(35)
                        t.circle(300, 15)
                        t.circle(30, 50)
                        t.seth(190)
                        t.circle(300, 17)
                        t.end_fill()

                    def body(self):
                        t = self.t

                        t.fillcolor('#F6D02F')
                        t.begin_fill()
                        # 右脸轮廓
                        t.penup()
                        t.circle(130, 40)
                        t.pendown()
                        t.circle(100, 105)
                        t.left(180)
                        t.circle(-100, 5)

                        # 右耳朵
                        t.seth(20)
                        t.circle(300, 30)
                        t.circle(30, 50)
                        t.seth(190)
                        t.circle(300, 36)

                        # 上轮廓
                        t.seth(150)
                        t.circle(150, 70)

                        # 左耳朵
                        t.seth(200)
                        t.circle(300, 40)
                        t.circle(30, 50)
                        t.seth(20)
                        t.circle(300, 35)
                        # print(t.pos())

                        # 左脸轮廓
                        t.seth(240)
                        t.circle(105, 95)
                        t.left(180)
                        t.circle(-105, 5)

                        # 左手
                        t.seth(210)
                        t.circle(500, 18)
                        t.seth(200)
                        t.fd(10)
                        t.seth(280)
                        t.fd(7)
                        t.seth(210)
                        t.fd(10)
                        t.seth(300)
                        t.circle(10, 80)
                        t.seth(220)
                        t.fd(10)
                        t.seth(300)
                        t.circle(10, 80)
                        t.seth(240)
                        t.fd(12)
                        t.seth(0)
                        t.fd(13)
                        t.seth(240)
                        t.circle(10, 70)
                        t.seth(10)
                        t.circle(10, 70)
                        t.seth(10)
                        t.circle(300, 18)

                        t.seth(75)
                        t.circle(500, 8)
                        t.left(180)
                        t.circle(-500, 15)
                        t.seth(250)
                        t.circle(100, 65)

                        # 左脚
                        t.seth(320)
                        t.circle(100, 5)
                        t.left(180)
                        t.circle(-100, 5)
                        t.seth(220)
                        t.circle(200, 20)
                        t.circle(20, 70)

                        t.seth(60)
                        t.circle(-100, 20)
                        t.left(180)
                        t.circle(100, 20)
                        t.seth(300)
                        t.circle(10, 70)

                        t.seth(60)
                        t.circle(-100, 20)
                        t.left(180)
                        t.circle(100, 20)
                        t.seth(10)
                        t.circle(100, 60)

                        # 横向
                        t.seth(180)
                        t.circle(-100, 10)
                        t.left(180)
                        t.circle(100, 10)
                        t.seth(5)
                        t.circle(100, 10)
                        t.circle(-100, 40)
                        t.circle(100, 35)
                        t.left(180)
                        t.circle(-100, 10)

                        # 右脚
                        t.seth(290)
                        t.circle(100, 55)
                        t.circle(10, 50)

                        t.seth(120)
                        t.circle(100, 20)
                        t.left(180)
                        t.circle(-100, 20)

                        t.seth(0)
                        t.circle(10, 50)

                        t.seth(110)
                        t.circle(100, 20)
                        t.left(180)
                        t.circle(-100, 20)

                        t.seth(30)
                        t.circle(20, 50)

                        t.seth(100)
                        t.circle(100, 40)

                        # 右侧身体轮廓
                        t.seth(200)
                        t.circle(-100, 5)
                        t.left(180)
                        t.circle(100, 5)
                        t.left(30)
                        t.circle(100, 75)
                        t.right(15)
                        t.circle(-300, 21)
                        t.left(180)
                        t.circle(300, 3)

                        # 右手
                        t.seth(43)
                        t.circle(200, 60)

                        t.right(10)
                        t.fd(10)

                        t.circle(5, 160)
                        t.seth(90)
                        t.circle(5, 160)
                        t.seth(90)

                        t.fd(10)
                        t.seth(90)
                        t.circle(5, 180)
                        t.fd(10)

                        t.left(180)
                        t.left(20)
                        t.fd(10)
                        t.circle(5, 170)
                        t.fd(10)
                        t.seth(240)
                        t.circle(50, 30)

                        t.end_fill()
                        self.noTrace_goto(130, 125)
                        t.seth(-20)
                        t.fd(5)
                        t.circle(-5, 160)
                        t.fd(5)

                        # 手指纹
                        self.noTrace_goto(166, 130)
                        t.seth(-90)
                        t.fd(3)
                        t.circle(-4, 180)
                        t.fd(3)
                        t.seth(-90)
                        t.fd(3)
                        t.circle(-4, 180)
                        t.fd(3)

                        # 尾巴
                        self.noTrace_goto(168, 134)
                        t.fillcolor('#F6D02F')
                        t.begin_fill()
                        t.seth(40)
                        t.fd(200)
                        t.seth(-80)
                        t.fd(150)
                        t.seth(210)
                        t.fd(150)
                        t.left(90)
                        t.fd(100)
                        t.right(95)
                        t.fd(100)
                        t.left(110)
                        t.fd(70)
                        t.right(110)
                        t.fd(80)
                        t.left(110)
                        t.fd(30)
                        t.right(110)
                        t.fd(32)

                        t.right(106)
                        t.circle(100, 25)
                        t.right(15)
                        t.circle(-300, 2)
                        ##############
                        # print(t.pos())
                        t.seth(30)
                        t.fd(40)
                        t.left(100)
                        t.fd(70)
                        t.right(100)
                        t.fd(80)
                        t.left(100)
                        t.fd(46)
                        t.seth(66)
                        t.circle(200, 38)
                        t.right(10)
                        t.fd(10)
                        t.end_fill()

                        # 尾巴花纹
                        t.fillcolor('#923E24')
                        self.noTrace_goto(126.82, -156.84)
                        t.begin_fill()

                        t.seth(30)
                        t.fd(40)
                        t.left(100)
                        t.fd(40)
                        t.pencolor('#923e24')
                        t.seth(-30)
                        t.fd(30)
                        t.left(140)
                        t.fd(20)
                        t.right(150)
                        t.fd(20)
                        t.left(150)
                        t.fd(20)
                        t.right(150)
                        t.fd(20)
                        t.left(130)
                        t.fd(18)
                        t.pencolor('#000000')
                        t.seth(-45)
                        t.fd(67)
                        t.right(110)
                        t.fd(80)
                        t.left(110)
                        t.fd(30)
                        t.right(110)
                        t.fd(32)
                        t.right(106)
                        t.circle(100, 25)
                        t.right(15)
                        t.circle(-300, 2)
                        t.end_fill()

                        # 帽子、眼睛、嘴巴、脸颊
                        self.cap(-134.07, 147.81)
                        self.mouth(-5, 25)
                        self.leftCheek(-126, 32)
                        self.rightCheek(107, 63)
                        self.colorLeftEar(-250, 100)
                        self.colorRightEar(140, 270)
                        self.leftEye(-85, 90)
                        self.rightEye(50, 110)
                        t.hideturtle()

                    def cap(self, x, y):
                        self.noTrace_goto(x, y)
                        t = self.t
                        t.fillcolor('#CD0000')
                        t.begin_fill()
                        t.seth(200)
                        t.circle(400, 7)
                        t.left(180)
                        t.circle(-400, 30)
                        t.circle(30, 60)
                        t.fd(50)
                        t.circle(30, 45)
                        t.fd(60)
                        t.left(5)
                        t.circle(30, 70)
                        t.right(20)
                        t.circle(200, 70)
                        t.circle(30, 60)
                        t.fd(70)
                        # print(t.pos())
                        t.right(35)
                        t.fd(50)
                        t.circle(8, 100)
                        t.end_fill()
                        self.noTrace_goto(-168.47, 185.52)
                        t.seth(36)
                        t.circle(-270, 54)
                        t.left(180)
                        t.circle(270, 27)
                        t.circle(-80, 98)

                        t.fillcolor('#444444')
                        t.begin_fill()
                        t.left(180)
                        t.circle(80, 197)
                        t.left(58)
                        t.circle(200, 45)
                        t.end_fill()

                        self.noTrace_goto(-58, 270)
                        t.pencolor('#228B22')
                        t.dot(35)

                        self.noTrace_goto(-30, 280)
                        t.fillcolor('#228B22')
                        t.begin_fill()
                        t.seth(100)
                        t.circle(30, 180)
                        t.seth(190)
                        t.fd(15)
                        t.seth(100)
                        t.circle(-45, 180)
                        t.right(90)
                        t.fd(15)
                        t.end_fill()
                        t.pencolor('#000000')

                    def start(self):
                        self.body()


                def main():
                    print('Painting the Pikachu... ')
                    turtle.screensize(800, 600)
                    turtle.title('Pikachu')
                    pikachu = Pikachu()
                    pikachu.start()
                    turtle.mainloop()


                if __name__ == '__main__':
                    main()

            elif "Doraemon" in name:
                from turtle import *


                # Doraemon with Python Turtle
                def ankur(x, y):
                    penup()
                    goto(x, y)
                    pendown()


                def aankha():
                    fillcolor("#ffffff")
                    begin_fill()

                    tracer(False)
                    a = 2.5
                    for i in range(120):
                        if 0 <= i < 30 or 60 <= i < 90:
                            a -= 0.05
                            lt(3)
                            fd(a)
                        else:
                            a += 0.05
                            lt(3)
                            fd(a)
                    tracer(True)
                    end_fill()


                def daari():
                    ankur(-32, 135)
                    seth(165)
                    fd(60)

                    ankur(-32, 125)
                    seth(180)
                    fd(60)

                    ankur(-32, 115)
                    seth(193)
                    fd(60)

                    ankur(37, 135)
                    seth(15)
                    fd(60)

                    ankur(37, 125)
                    seth(0)
                    fd(60)

                    ankur(37, 115)
                    seth(-13)
                    fd(60)


                def mukh():
                    ankur(5, 148)
                    seth(270)
                    fd(100)
                    seth(0)
                    circle(120, 50)
                    seth(230)
                    circle(-120, 100)


                def muflar():
                    fillcolor('#e70010')
                    begin_fill()
                    seth(0)
                    fd(200)
                    circle(-5, 90)
                    fd(10)
                    circle(-5, 90)
                    fd(207)
                    circle(-5, 90)
                    fd(10)
                    circle(-5, 90)
                    end_fill()


                def nak():
                    ankur(-10, 158)
                    seth(315)
                    fillcolor('#e70010')
                    begin_fill()
                    circle(20)
                    end_fill()


                def black_aankha():
                    seth(0)
                    ankur(-20, 195)
                    fillcolor('#000000')
                    begin_fill()
                    circle(13)
                    end_fill()

                    pensize(6)
                    ankur(20, 205)
                    seth(75)
                    circle(-10, 150)
                    pensize(3)

                    ankur(-17, 200)
                    seth(0)
                    fillcolor('#ffffff')
                    begin_fill()
                    circle(5)
                    end_fill()
                    ankur(0, 0)


                def face():
                    fd(183)
                    lt(45)
                    fillcolor('#ffffff')
                    begin_fill()
                    circle(120, 100)
                    seth(180)
                    # print(pos())
                    fd(121)
                    pendown()
                    seth(215)
                    circle(120, 100)
                    end_fill()
                    ankur(63.56, 218.24)
                    seth(90)
                    aankha()
                    seth(180)
                    penup()
                    fd(60)
                    pendown()
                    seth(90)
                    aankha()
                    penup()
                    seth(180)
                    fd(64)


                def taauko():
                    penup()
                    circle(150, 40)
                    pendown()
                    fillcolor('#00a0de')
                    begin_fill()
                    circle(150, 280)
                    end_fill()


                def Doraemon():
                    taauko()

                    muflar()

                    face()

                    nak()

                    mukh()

                    daari()

                    ankur(0, 0)

                    seth(0)
                    penup()
                    circle(150, 50)
                    pendown()
                    seth(30)
                    fd(40)
                    seth(70)
                    circle(-30, 270)

                    fillcolor('#00a0de')
                    begin_fill()

                    seth(230)
                    fd(80)
                    seth(90)
                    circle(1000, 1)
                    seth(-89)
                    circle(-1000, 10)

                    # print(pos())

                    seth(180)
                    fd(70)
                    seth(90)
                    circle(30, 180)
                    seth(180)
                    fd(70)

                    # print(pos())
                    seth(100)
                    circle(-1000, 9)

                    seth(-86)
                    circle(1000, 2)
                    seth(230)
                    fd(40)

                    # print(pos())

                    circle(-30, 230)
                    seth(45)
                    fd(81)
                    seth(0)
                    fd(203)
                    circle(5, 90)
                    fd(10)
                    circle(5, 90)
                    fd(7)
                    seth(40)
                    circle(150, 10)
                    seth(30)
                    fd(40)
                    end_fill()

                    seth(70)
                    fillcolor('#ffffff')
                    begin_fill()
                    circle(-30)
                    end_fill()

                    ankur(103.74, -182.59)
                    seth(0)
                    fillcolor('#ffffff')
                    begin_fill()
                    fd(15)
                    circle(-15, 180)
                    fd(90)
                    circle(-15, 180)
                    fd(10)
                    end_fill()

                    ankur(-96.26, -182.59)
                    seth(180)
                    fillcolor('#ffffff')
                    begin_fill()
                    fd(15)
                    circle(15, 180)
                    fd(90)
                    circle(15, 180)
                    fd(10)
                    end_fill()

                    ankur(-133.97, -91.81)
                    seth(50)
                    fillcolor('#ffffff')
                    begin_fill()
                    circle(30)
                    end_fill()
                    # Doraemon with Python Turtle

                    ankur(-103.42, 15.09)
                    seth(0)
                    fd(38)
                    seth(230)
                    begin_fill()
                    circle(90, 260)
                    end_fill()

                    ankur(5, -40)
                    seth(0)
                    fd(70)
                    seth(-90)
                    circle(-70, 180)
                    seth(0)
                    fd(70)

                    ankur(-103.42, 15.09)
                    fd(90)
                    seth(70)
                    fillcolor('#ffd200')
                    # print(pos())
                    begin_fill()
                    circle(-20)
                    end_fill()
                    seth(170)
                    fillcolor('#ffd200')
                    begin_fill()
                    circle(-2, 180)
                    seth(10)
                    circle(-100, 22)
                    circle(-2, 180)
                    seth(180 - 10)
                    circle(100, 22)
                    end_fill()
                    goto(-13.42, 15.09)
                    seth(250)
                    circle(20, 110)
                    seth(90)
                    fd(15)
                    dot(10)
                    ankur(0, -150)

                    black_aankha()


                if __name__ == '__main__':
                    screensize(800, 600, "#f0f0f0")
                    pensize(3)
                    speed(9)
                    Doraemon()
                    ankur(100, -300)
                    write('by Jairam J S', font=("Bradley Hand ITC", 30, "bold"))
                    mainloop()

        elif "news" in query:
            r = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=407929257fef4d01be9c219540689ef3')
            data = json.loads(r.content)
            for i in range(10):
                News = data['articles'][i]['title']
                print("News", i + 1, ":", News)
                j = i + 1

                Speak('news')
                Speak(j)
                Speak(News)

