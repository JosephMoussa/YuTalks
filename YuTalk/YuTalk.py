from msilib.schema import Font
from tkinter import *
from tkinter import font
from tkinter.messagebox import showinfo
from gtts import gTTS
import speech_recognition as sr
import os

mainwindow = Tk()
mainwindow.title('Text-To-Speech and Speech-To-Text Converter')
mainwindow.geometry('500x500')
mainwindow.resizable(0, 0)
mainwindow.configure(bg='yellow')


def say(text1):
    language = 'en'
    speech = gTTS(text=text1, lang=language, slow=False)
    speech.save("text.mp3")
    os.system("start text.mp3")


def recordvoice():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                text1 = r.recognize_google(audio, language="en-IN")
            except:
                pass
            return text1


def TextToSpeech():
    texttospeechwindow = Toplevel(mainwindow)
    texttospeechwindow.title('Text-to-Speech Converter by')
    texttospeechwindow.geometry("500x500")
    texttospeechwindow.configure(bg='Blue')

    Label(texttospeechwindow, text='Text-to-Speech Converter',
          font=("Times New Roman", 15), bg='Blue').place(x=50)

    text = Text(texttospeechwindow, height=5, width=30, font=12)
    text.place(x=7, y=60)

    speakbutton = Button(texttospeechwindow, text='listen',
                         bg='coral', command=lambda: say(str(text.get(1.0, END))))
    speakbutton.place(x=140, y=200)


def SpeechToText():
    speechtotextwindow = Toplevel(mainwindow)
    speechtotextwindow.title('You Talk I Speak')
    speechtotextwindow.geometry("600x900")
    speechtotextwindow.configure(bg='#495C83')

    Label(speechtotextwindow, text='You Talk I Speak',
          font=("Anurati", 15), bg='#495C83').place(x=230)

    text = Text(speechtotextwindow, font=('Otto', 26), height=30, width=56)
    text.place(x=20, y=100)

    recordbutton = Button(speechtotextwindow, text='Start', width=79,
                          bg='Sienna', command=lambda: text.insert(END, recordvoice()))
    recordbutton.place(x=20, y=50)


Label(mainwindow, text='Text-To-Speech and Speech-To-Text Converter',
      font=('Times New Roman', 16), bg='red', wrap=True, wraplength=450).place(x=50, y=0)

texttospeechbutton = Button(mainwindow, text='Text-To-Speech Conversion',
                            font=('Times New Roman', 16), bg='Purple', command=TextToSpeech)
texttospeechbutton.place(x=100, y=150)

speechtotextbutton = Button(mainwindow, text='Speech-To-Text Conversion',
                            font=('Times New Roman', 16), bg='Purple', command=SpeechToText)
speechtotextbutton.place(x=100, y=250)

mainwindow.update()
mainwindow.mainloop()
