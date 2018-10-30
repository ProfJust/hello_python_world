#!/usr/bin/python
# Start mit python3 gui_sw03.py
from tkinter import *

# Klasse definieren 
class Application(Frame):
    #--- Konstruktor ---
    def __init__(self,master=None):
        Frame.__init__(self, master)  #vErerbung von Frame

        #--- Einfügen eines Labels ---
        meinLbl=Label(master,text=" Hello Python World")
        meinLbl.place(x=10,y=10)

          #--- Einfügen eines Labels ---
        meinLbl=Label(master,text="WHS - Robotik Bocholt")
        meinLbl.place(x=10,y=40)


#Tk Objekt instanzieren
root=Tk()

#Application Objekt instanzieren
app=Application(master=root)
app.mainloop()