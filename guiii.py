#!/usr/bin/env
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import time

fruits = ["μήλο", "πορτοκαλί", "μπανάνα", "μανταρίνι", "φράουλα", "πεπόνι", "καρπούζι", "ρόδι"]
f_images = ["apple.jpg", "orange.jpg", "banana.jpg", "madarin.jpg", "strawberry.jpg", "melon.jpg", "watermelon.jpg", "rodi.jpg"]
length = len(f_images)


class Go(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

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

        label = tk.Label(self, text="Καλημέρα σας", font=('TimesNewRoman','20', 'bold', 'italic'))
        label.pack(side="top", fill="x", pady=10)
        ##Buttons
        self.button1 = Button(self, text="Google TTS", command=lambda: lock("Lock Screen"))
        self.button1.config(height = 30, width = 60)
        self.button1.pack(side = LEFT)
        
        self.button2 = Button(self, text="Return to start page", 
                  command=lambda: master.switch_frame(PageOne))
        self.button2.config(height = 30, width = 60)
        self.button2.pack(side = LEFT)
        

class PageOne(tk.Frame):
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        label = tk.Label(self, text="Είσαστε έτοιμοι παιδιά;", font=('TimesNewRoman','20', 'bold', 'italic'))
        label.pack(side="top", fill="x", pady=10)
        ##Buttons
        self.button1 = Button(self, text="No", command=lambda: master.switch_frame(StartPage))
        self.button1.config( height = 30, width = 60)
        self.button1.pack(side = LEFT)
        
        self.button2 = Button(self, text="Yes",
                  command=lambda: master.switch_frame(CategoryPage))
        self.button2.config(height = 30, width = 60)
        self.button2.pack(side = RIGHT)

class CategoryPage(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        label = tk.Label(self, text="Διαλέξτε κατηγορία", font=('TimesNewRoman','20', 'bold', 'italic'))
        label.pack(side="top", fill="x", pady=10)

        self.button1 = Button(self, text="Φρούτα", command=lambda: master.switch_frame(GamePage))
        self.button1.config( height = 15, width = 30)
        self.button1.pack(side = LEFT)
        
        self.button2 = Button(self, text="Σχήματα",
                  command=lambda: master.switch_frame(GamePage))
        self.button2.config(height = 15, width = 30)
        self.button2.pack(side = RIGHT)

class GamePage(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        self.counter = 0
        temp = ImageTk.PhotoImage( Image.open(f_images[ self.counter ]) )
        
        self.label = tk.Label(self, text = fruits[ self.counter ], font=('TimesNewRoman','20', 'bold', 'italic'), image =  temp)
        self.label.pack(side="top", fill="x", pady=10)
        self.label.image = temp
        self.after(1000, self.refresh)

    def refresh(self):
        
        self.counter += 1
        if(self.counter < length):
            print( self.counter )
            temp = ImageTk.PhotoImage( Image.open(f_images[ self.counter ]) )

            self.label.config( image = temp )
            self.label.image = temp
            self.after(1000, self.refresh)
            
        else:
            self.master.switch_frame(CategoryPage)

            
if __name__ == "__main__":

    app = Go()
    app.mainloop()

