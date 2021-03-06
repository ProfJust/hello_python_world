#!/usr/bin/python3
# -*- coding: utf-8 -*-
# https://www.youtube.com/watch?v=Q-U9oqv2bTk
##pyqt_sw13_Senso.py
import sys
from PyQt5.QtCore import (Qt, QTimer)
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QLabel)
# sudo apt-get install python-pyqt5.qtmultimedia
from PyQt5.QtMultimedia import QSound

import random

global S 
S = 2 #Spalten
global R 
R = 2 #Reihen
global SIZE
SIZE = 150

class Ui(QWidget):
    def __init__(self): #Konstrukor
        #Konstruktor der Elternklasse aufrufen
        super(Ui, self).__init__()  
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)  
        self.timer.start(1000) 
        self.toggleFlag = True;  
        self.initUI()
        # Sounds aus http://codeperspectives.com/front-end/simon-says-sound/
        self.sound_red= "sounds/a_sharp.wav"
        self.sound_green= "sounds/c_sharp.wav"
        self.sound_yellow= "sounds/d_sharp.wav"
        self.sound_blue= "sounds/f_sharp.wav"
           
    
    def initUI(self): 
        self.btn = [[QPushButton(self)  for s in range(S)] for r in range(R)] 
        for r in range(R):
          for s in range(S): 
            #self.btn[r][s] = QPushButton(self) 
            self.btn[r][s].setStyleSheet("background-color: grey")
            self.btn[r][s].color = "grey" 
            self.btn[r][s].resize(SIZE,SIZE)
            self.btn[r][s].move(SIZE*r+20, SIZE*s+20)   
            
        #Fenster Konfigurieren
        self.setGeometry(20, 20, SIZE * S + 40, SIZE * R +40)
        self.setWindowTitle('Qt - Senso')
        self.show()
        
    def update(self): 
        if self.toggleFlag == True: # Ein Feld in Bunt 
            self.toggleFlag = False
            zf = random.randint(0,3) #Zufallszahl               
            if zf == 0:
                self.btn[0][0].setStyleSheet("background-color: green")
                self.btn[0][1].setStyleSheet("background-color: grey")
                self.btn[1][0].setStyleSheet("background-color: grey")
                self.btn[1][1].setStyleSheet("background-color: grey") 
                QSound.play(self.sound_green)
            elif zf == 1:            
                self.btn[0][0].setStyleSheet("background-color: grey")
                self.btn[0][1].setStyleSheet("background-color: red")
                self.btn[1][0].setStyleSheet("background-color: grey")
                self.btn[1][1].setStyleSheet("background-color: grey") 
                QSound.play(self.sound_red)
            elif zf== 2:            
                self.btn[0][0].setStyleSheet("background-color: grey")
                self.btn[0][1].setStyleSheet("background-color: grey")
                self.btn[1][0].setStyleSheet("background-color: yellow")
                self.btn[1][1].setStyleSheet("background-color: grey")
                QSound.play(self.sound_yellow)
            elif zf == 3:            
                self.btn[0][0].setStyleSheet("background-color: grey")
                self.btn[0][1].setStyleSheet("background-color: grey")
                self.btn[1][0].setStyleSheet("background-color: grey")
                self.btn[1][1].setStyleSheet("background-color: blue")
                QSound.play(self.sound_blue)
        else:
            self.toggleFlag = True # Alle Felder Grau
            self.btn[0][0].setStyleSheet("background-color: grey")
            self.btn[0][1].setStyleSheet("background-color: grey")
            self.btn[1][0].setStyleSheet("background-color: grey")
            self.btn[1][1].setStyleSheet("background-color: grey") 

    
if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ui = Ui()
    sys.exit(app.exec_())