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
mainwindow.configure(bg='#855347')


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
    texttospeechwindow.geometry("600x900")
    texttospeechwindow.configure(bg='#495C83')

    Label(texttospeechwindow, text='Text-to-Speech Converter',
          font=("Anurati", 15), bg='#495C83').place(x=190)

    text = Text(texttospeechwindow, font=('Otto', 26), height=30, width=56)
    text.place(x=20, y=100)

    speakbutton = Button(texttospeechwindow, text='listen', width=79,
                         bg='coral', command=lambda: say(str(text.get(1.0, END))))
    speakbutton.place(x=20, y=50)


def SpeechToText():
    speechtotextwindow = Toplevel(mainwindow)
    speechtotextwindow.title('Speech-To-Text Converter')
    speechtotextwindow.geometry("600x900")
    speechtotextwindow.configure(bg='#495C83')

    Label(speechtotextwindow, text='Speech-To-Text Converter',
          font=("Anurati", 15), bg='#495C83').place(x=190)

    text = Text(speechtotextwindow, font=('Otto', 26), height=30, width=56)
    text.place(x=20, y=100)

    recordbutton = Button(speechtotextwindow, text='Start', width=79,
                          bg='Sienna', command=lambda: text.insert(END, recordvoice()))
    recordbutton.place(x=20, y=50)


Label(mainwindow, text='Text-To-Speech and Speech-To-Text Converter',
      font=("Anurati", 20), bg='#855347', wrap=True, wraplength=450).place(x=90, y=0)

texttospeechbutton = Button(mainwindow, text='Text-To-Speech Conversion',
                            font=('Anurati', 16), bg='#0aaac2', command=TextToSpeech)
texttospeechbutton.place(x=110, y=150)

speechtotextbutton = Button(mainwindow, text='Speech-To-Text Conversion',
                            font=('Anurati', 16), bg='#0aaac2', command=SpeechToText)
speechtotextbutton.place(x=110, y=250)

mainwindow.update()
mainwindow.mainloop()
