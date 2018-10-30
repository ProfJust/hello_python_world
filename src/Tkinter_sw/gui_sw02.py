#!/usr/bin/python
# Start mit python3 gui_sw02.py
from tkinter import *

# Klasse definieren 
class Application(Frame):
    #--- Konstruktor ---
    def __init__(self,master=None):
        Frame.__init__(self, master)  #vErerbung von Frame


#Tk Objekt instanzieren
root=Tk()

#Application Objekt instanzieren
app=Application(master=root)
app.mainloop()