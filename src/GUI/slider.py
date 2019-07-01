from tkinter import *

class Slider:  
    def __init__(self, filter_, master):
        self.scale = Scale(master, resolution=1, from_=67, to=0, width=60, activebackground="black", showvalue=0, command=self.onChange)
        self.scale.set('33')
        self.label = Label(master, text=0, font=("Helvetica", 12), height=5, justify="center", anchor="c", bg="#40E0D0")
        self.name = Label(master, text=0, font=("Helvetica", 12), justify="center", anchor="c")
        self.filter = filter_
        
    def onChange(self, value):
        step = 3
        if int(value) > 33:
            value = int(value) - 32      
        elif int(value) < 33:
            value = (100 - (33 - int(value)) * step) / 100
        else:
            value = 1
        self.label['text'] = str(value)
        self.filter.set_gain(value)


    def setName(self, name):
        self.name['text'] = name
