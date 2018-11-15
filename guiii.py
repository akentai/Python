#!/usr/bin/env
from tkinter import *
import tkinter as tk


class Go(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
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

        ##Buttons
        self.button1 = Button(self, text="No", command=lambda: lock("Lock Screen"))
        self.button1.config(height = 30, width = 60)
        self.button1.pack(side = LEFT)
        
        self.button2 = Button(self, text="Yes",
                  command=lambda: master.switch_frame(StartPage))
        self.button2.config(height = 30, width = 60)
        self.button2.pack(side = RIGHT)
    
if __name__ == "__main__":
    app = Go()
    app.mainloop()

