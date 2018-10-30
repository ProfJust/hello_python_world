#!/usr/bin/python
# Start mit python3 gui_sw04.py
from tkinter import *

# Klasse definieren 
class Application(Frame):
    #--- Konstruktor ---
    def __init__(self,master=None):
        Frame.__init__(self, master)  #vErerbung von Frame
 	   #--- 3 Label Vorname, Nachname und Ausgabe ---
        Label(master,text="Nachname").grid(row=0)
        Label(master,text="Vorname").grid(row=1)
        Label(master,text="Die Eingabe").grid(row=2)

      #--- Label mit Bezeichner lbl1 für Ausgabe ---
        self.lbl1=Label(master, bg="yellow", fg="blue")
        self.lbl1.grid(row=2, column=1)

      #--- Eingabefelder ---
        self.nname = Entry(master)
        self.vname = Entry(master)
        self.nname.grid(row=0, column=1)
        self.vname.grid(row=1, column=1)
      
       #--- 2 Buttons OK und Abbrechen ---
        #      Beschriftung, Event-Funktion, Position im Grid
        Button(master,text='OK',width=20,command=self.action).grid(row=3, column=0)
        Button(master,text='Abbrechen',width=20,command=root.destroy).grid(row=3, column=1)
       
    
    #--- Die Event-Handler-Funktion --
    def action(self):
        self.lbl1.config(text = self.vname.get() +  self.nname.get() )

  
#Tk Objekt instanzieren
root=Tk()
#Application Objekt instanzieren
app=Application(master=root)
#Mainloop starten
app.mainloop()
