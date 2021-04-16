from tkinter import *
from time import * 
import datetime 

root = Tk()
root.title('ANTİN SAAT')


def clock():
    text = strftime('%H:%M:%S')
    label.config(text=text)
    label.after(1000,clock)


label = Label(root,font=("ds-digital",100), background=("black"), foreground="white")
label.pack(anchor="center")


clock ()


mainloop()