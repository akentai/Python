#!/usr/bin/env
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import time
import speech_recognition as sr
sr.__version__
from frt import fruits, sports, seasons

category = []
category_images = []

r = sr.Recognizer()
r.energy_threshold = 2000
r.pause_threshold = 2

class Go(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.iconbitmap("@index.xbm")
        self.resizable(0,0)
        self.geometry("600x440")
        self.config( bg = 'white' )
        self.title("Menu")

        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


def select(index):

    category.clear()
    category_images.clear()
        
    if(index == 1):
        fruits(category, category_images)
        print(category)
        
    elif(index == 2):
        sports(category, category_images)
        print(category)
        
    elif(index == 3):
        seasons(category, category_images)
        print(category)
  
    return


def lock(text):

    print(text);
    return
    
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
        self.button1.pack(side = LEFT, ipadx = 30)

        img3 = ImageTk.PhotoImage( Image.open("kinder4.jpg") ) 
        self.button2 = Button(self, image = img3, command=lambda: master.switch_frame(PageOne), bg='white', compound = LEFT)
        self.button2.image = img3
        self.button2.pack(side = RIGHT, expand = 1, fill = BOTH)

class PageOne(tk.Frame):
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        temp = ImageTk.PhotoImage( Image.open("kinder2.jpg") ) 
        self.label = tk.Label(self, image = temp, text="Διαλέξτε κατηγορία\n και πατήστε επόμενο", font=('Century','16', 'bold','italic'), compound = LEFT,
                              bg = 'white')
        self.label.image = temp
        self.label.pack(side="top", fill=BOTH)
        
        ##Buttons
        self.button1 = Button(self, command=lambda: select(1), bg = 'pale green', text = "Φρούτα", font=('Georgia','15', 'italic'))
        self.button1.pack(side = LEFT)
        
        self.button2 = Button(self, command=lambda: select(2), bg = 'blue', text = "Αθλήματα", font=('Georgia','15', 'italic'))
        self.button2.pack(side = LEFT)

        self.button3 = Button(self, command=lambda: select(3), bg = 'pink', text = "4 Εποχές", font=('Georgia','15', 'italic'))
        self.button3.pack(side = LEFT)

        self.button4 = Button(self, command=lambda: master.switch_frame(ReadyPage), text = "Επόμενο", font=('Georgia','15', 'italic'))
        self.button4.pack(side = BOTTOM, fill = BOTH)

class ReadyPage(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        temp = ImageTk.PhotoImage( Image.open("kinder5.jpg") ) 
        self.label = tk.Label(self, image = temp, text="Έτοιμοι να ξεκινήσουμε;", font=('Centrury','20', 'bold'), compound = TOP,
                              bg = 'white')
        self.label.image = temp
        self.label.pack(side="top", fill=BOTH)
        
        ##Buttons
        self.button1 = Button(self, command=lambda: master.switch_frame(StartPage), bg = 'indian red', text = "Όχι", font=('Century','25', 'italic'))
        self.button1.config( height = 8, width = 14)
        self.button1.pack(side = LEFT)
        
        self.button2 = Button(self, bg = 'pale green', text = "Ναι", font=('Century','30', 'italic'), command=lambda: master.switch_frame(GamePage))
        self.button2.config(height = 8, width = 34)
        self.button2.pack(side = RIGHT)



def unc(index):

    time.sleep(2)
    return

class GamePage(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        self.counter = 0
        temp = ImageTk.PhotoImage( Image.open( category_images[ self.counter ] ) )
        
        self.label = tk.Label(self, text = category[ self.counter ], font=('Centrury','20', 'bold'), image =  temp, compound = TOP, bg='white')
        self.label.pack(side="top")
        self.label.image = temp
        self.after(1000, self.refresh)

    def refresh(self):

        unc(self.counter)
        self.counter += 1
        length = len(category)
        if(self.counter < length):

            temp = ImageTk.PhotoImage( Image.open( category_images[ self.counter ] ) )
            
            self.label.config( image = temp )
            self.label.config( text = category[ self.counter ], font=('Centruty','20', 'bold') )
            
            self.label.image = temp
            
            self.after(1000, self.refresh)
            
        else:
            self.master.switch_frame(StartPage)

            
if __name__ == "__main__":

    app = Go()
    app.mainloop()

