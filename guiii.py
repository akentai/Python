#!/usr/bin/env
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import speech_recognition as sr
sr.__version__
from fruits import *



class Go(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.iconbitmap("@index.xbm")
        self.resizable(0,0)
        self.title("Menu")

        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


def lock(text):
    print(text)
    
class StartPage(tk.Frame):
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        img1 = ImageTk.PhotoImage( Image.open("kinder.jpg") ) 
        self.label = tk.Label(self, image = img1, text="Καλημέρα σας", font=('TimesNewRoman','30', 'italic'), compound = TOP,
                              bg = 'white')
        self.label.image = img1
        self.label.pack(side="top")
        
        ##Buttons
        img2 = ImageTk.PhotoImage( Image.open("kinder3.jpg") ) 
        self.button1 = Button(self, image = img2, command=lambda: lock("Lock Screen"), bg='white', compound = LEFT)
        self.button1.image = img2
        self.button1.pack(side = LEFT, ipadx = 60)

        img3 = ImageTk.PhotoImage( Image.open("kinder4.jpg") ) 
        self.button2 = Button(self, image = img3, command=lambda: master.switch_frame(PageOne), bg='white', compound = LEFT)
        self.button2.image = img3
        self.button2.pack(side = RIGHT, expand = 1, fill = BOTH)

class PageOne(tk.Frame):
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        temp = ImageTk.PhotoImage( Image.open("kinder2.jpg") ) 
        self.label = tk.Label(self, image = temp, text="   Έτοιμοι να ξεκινήσουμε;   ", font=('TimesNewRoman','30', 'italic'), compound = RIGHT,
                              bg = 'white')
        self.label.image = temp
        self.label.pack(side="top", fill=BOTH)
        
        ##Buttons
        self.button1 = Button(self, command=lambda: master.switch_frame(StartPage), bg = 'indian red', text = "Όχι", font=('TimesNewRoman','30', 'italic'))
        self.button1.config( height = 8, width = 24)
        self.button1.pack(side = LEFT)
        
        self.button2 = Button(self, bg = 'pale green', text = "Ναι", font=('TimesNewRoman','30', 'italic'),
                  command=lambda: master.switch_frame(CategoryPage))
        self.button2.config(height = 8, width = 24)
        self.button2.pack(side = RIGHT)

class CategoryPage(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        temp = ImageTk.PhotoImage( Image.open("kinder5.jpg") ) 
        self.label = tk.Label(self, text="Θα παίξουμε με τα...", font=('TimesNewRoman','20', 'bold', 'italic'), bg='white',  image = temp, compound = TOP)
        self.label.image = temp
        
        self.label.pack(side="top", fill=BOTH)

        self.button1 = Button(self, text = category_string, command=lambda: master.switch_frame(GamePage), bg = category_color, font=('TimesNewRoman','30', 'italic'))
        self.button1.config( height = 8, width = 48)
        self.button1.pack(side = RIGHT, expand = 1, fill=BOTH)
        
        self.button1 = Button(self, text="Πίσω", command=lambda: master.switch_frame(PageOne), bg = 'white')
        self.button1.config( height = 8, width = 8)
        self.button1.pack(side = LEFT, fill = BOTH)

def func(index):
    r = sr.Recognizer()
    r.energy_threshold = 2000
    r.pause_threshold = 2
    print(category[index])

    with sr.Microphone() as source:
        print('Say Something')
        audio = r.listen(source)
        print('Done')

    try:
        text = r.recognize_google(audio, language = "el-GR")
        print(text)
        if(text == category[index]):
            print('Correct\n')
        else:
            print('Try Again\n')

    except Exception as e:
        print(e)

    return

class GamePage(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        self.counter = 0
        temp = ImageTk.PhotoImage( Image.open( category_images[ self.counter ] ) )
        
        self.label = tk.Label(self, text = category[ self.counter ], font=('TimesNewRoman','20', 'bold', 'italic'), image =  temp)
        self.label.pack(side="top", fill="x", pady=10)
        self.label.image = temp
        self.after(1000, self.refresh)

    def refresh(self):

        self.counter += 1
        if(self.counter < length):

            temp = ImageTk.PhotoImage( Image.open( category_images[ self.counter ] ) )
            
            self.label.config( image = temp )
            self.label.image = temp

            func(self.counter)
            
            self.after(1000, self.refresh)
            
        else:
            self.master.switch_frame(CategoryPage)

            
if __name__ == "__main__":

    app = Go()
    app.mainloop()

