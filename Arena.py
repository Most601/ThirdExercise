# -*- coding: utf-8 -*-
import random
import Robot
import tkinter as tk
import simulator
import numpy as np


class Arena:

    def __init__(self):
        self.NumOfRobots=0
        self.x = 1000
        self.y = 1000
        self.StaticBots = 30
        self.MoveBots = 40
        self.Matrix = np.zeros(shape = (self.x,self.y), dtype = np.int)
        self.start = False      
        self.ListMoveBot = []
        self.ListStaticBot = []
        self.ListAllBots=[]
        self.root = tk.Tk()
        self.CreateGui()

    def CreateGui(self):     
        self.canv = tk.Canvas(self.root,width=1000, height=1000,scrollregion=(0,0,1020,1020))
        self.root.title("Simulator")
        self.sbar = tk.Scrollbar(self.root,orient=tk.VERTICAL,command=self.canv.yview) 
        self.canv.configure(yscrollcommand=self.sbar.set)
        self.sbar.pack(side=tk.RIGHT, fill=tk.Y) 
        self.button = tk.Button(self.root,text="Start",anchor=tk.W, command=self.PlayArena)
        self.button.pack(side=tk.RIGHT)
        self.canv.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def BlackFrame(self):
        self.Matrix = np.zeros(shape = (self.x,self.y), dtype = np.int)
        for i in range(self.x):
            self.Matrix[i][self.y - 1] = 2
            self.Matrix[i][0] = 2
        for j in range(self.y):
            self.Matrix[self.x - 1][j] = 2
            self.Matrix[0][j] = 2

    def RandomArena(self):
        self.BlackFrame()
        for i in range(20):
            n1 = int((random.random() * (self.x)) + 1)
            n2 = int((random.random() * (self.x)) + 1)
            self.canv.create_rectangle(n1-100, n2-100, n1, n2, fill="gray", outline = 'gray')
            
            for i in range(n1-100, n1):
                for j in range(n2-100,n2):
                    self.Matrix[i][j] = 1
                                 
        for i in range(5):
            n1 = int((random.random() * (self.x)) + 1)
            n2 = int((random.random() * (self.x)) + 1)
            self.canv.create_rectangle(n1-50, n2-50, n1, n2, fill="black", outline = 'black')
            
            for i in range(n1-50, n1):
                for j in range(n2-50,n2):
                    self.Matrix[i][j] = 2
 
    def PlayArena(self):
        self.start = True
        simulator.moveRobot(self)
        
    def NewRobots(self, EmoutOfBots,IsStatic):
        for i in range(EmoutOfBots):
            self.NumOfRobots = self.NumOfRobots+1
            x1 = 0
            y1 = 0
            while(self.Matrix[x1][y1] == 2):
                x1 = int((random.random() * (self.x - 1)) + 1)
                y1 = int((random.random() * (self.y - 1)) + 1)
            if(IsStatic):
                rob = Robot.Robot(self.NumOfRobots+2,IsStatic,self.Matrix[x1][y1],x1,y1, self.MoveBots+self.StaticBots)
                rob.GussLocal=[x1,y1]
                my_oval = self.canv.create_oval(x1, y1, x1 + 10, y1 + 10, fill='red')
                newText = self.canv.create_text(x1,y1,anchor=tk.SW,font=("Purisa", 8),text=self.NumOfRobots)
                self.ListAllBots.append([my_oval,self.NumOfRobots+2])
                self.ListStaticBot.append([rob,x1,y1,my_oval])

            else:
                rob = Robot.Robot(self.NumOfRobots+2, IsStatic, self.Matrix[x1][y1], 0, 0,self.MoveBots+self.StaticBots)
                my_oval = self.canv.create_oval(x1, y1, x1 + 10, y1 + 10, fill='green')
                newText = self.canv.create_text(x1,y1,anchor=tk.SW,font=("Purisa", 8),text=self.NumOfRobots)
                self.ListAllBots.append([my_oval,self.NumOfRobots+2])
                self.ListMoveBot.append([rob,x1,y1,my_oval,newText])
            self.Matrix[x1][y1] = rob.Id