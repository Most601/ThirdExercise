import random
import Robot
import tkinter as tk
import simulator
import tkinter.messagebox
import numpy as np


class Arena:

    def __init__(self):
        self.NumOfRobots=0
        self.id = id
        self.x = 1000
        self.y = 1000
        self.StaticBots = 60
        self.MoveBots = 40
        self.Matrix = np.zeros(shape = (self.x,self.y), dtype = np.int)
        self.start = False
        self.ListMoveBot = []
        self.ListStaticBot = []
        self.ListAllBots=[]
        #self.recRob = []
        self.root = tk.Tk()
        self.CreateGui()
        #self.root.state('zoomed')

    def CreateGui(self):     
        self.canv = tk.Canvas(self.root,width=1000, height=1000,scrollregion=(0,0,1020,1020))
        self.root.title("Simulator")
        self.sbar = tk.Scrollbar(self.root,orient=tk.VERTICAL,command=self.canv.yview) 
        self.canv.configure(yscrollcommand=self.sbar.set)
        self.sbar.pack(side=tk.RIGHT, fill=tk.Y) 
        self.button = tk.Button(self.root,text="Start",anchor=tk.W, command=self.PlayArena)
        self.button.pack(side=tk.RIGHT)
        self.canv.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    def RandomArena(self):
        self.BlackFrame()
        for i in range(20):
            n1 = random.randint(100,1000)
            n2 = random.randint(100,1000)
            self.canv.create_rectangle(n1-100, n2-100, n1, n2, fill="gray", outline = 'gray')
            
            for i in range(n1-100, n1):
                for j in range(n2-100,n2):
                    self.Matrix[i][j] = 1
                                 
        for i in range(5):
            n1 = random.randint(50,1000)
            n2 = random.randint(50,1000)
            self.canv.create_rectangle(n1-50, n2-50, n1, n2, fill="black", outline = 'black')
            
            for i in range(n1-50, n1):
                for j in range(n2-50,n2):
                    self.Matrix[i][j] = 2
            
            for i in range(n1-70, n1):
                for j in range(n2-70,n2):
                    self.Matrix[i][j] = 2
        
    def PlayArena(self):
        self.start = True
        simulator.moveRobot(self)
        
    def BlackFrame(self):
        for i in range(1000):
            self.Matrix[0][i] = 2
            self.Matrix[999][i] = 2
            self.Matrix[i][0] = 2
            self.Matrix[i][999]
            
    def NewRobots(self, EmoutOfBots,IsStatic):
        for i in range(EmoutOfBots):
            self.NumOfRobots = self.NumOfRobots+1
            randX=0
            randY=0
            while(self.Matrix[randX][randY] == 2):
                randX = random.randint(1,990)
                randY = random.randint(1,990)
            if(IsStatic):
                r = Robot.Robot(self.NumOfRobots+2,IsStatic,self.Matrix[randX][randY],randX,randY, self.MoveBots+self.StaticBots)
                my_oval=self.canv.create_oval(randX, randY, randX + 10, randY + 10, fill='red')
                newText = self.canv.create_text(randX,randY,anchor=tk.SW,font=("Purisa", 8),text=self.NumOfRobots)
                self.ListAllBots.append([my_oval,self.NumOfRobots+2])
                self.ListStaticBot.append([r,randX,randY,my_oval])

            else:
                r = Robot.Robot(self.NumOfRobots+2, IsStatic, self.Matrix[randX][randY], 0, 0,self.MoveBots+self.StaticBots)
                my_oval = self.canv.create_oval(randX, randY, randX + 10, randY + 10, fill='green')
                newText = self.canv.create_text(randX,randY,anchor=tk.SW,font=("Purisa", 8),text=self.NumOfRobots)
                self.ListAllBots.append([my_oval,self.NumOfRobots+2])
                self.ListMoveBot.append([r,randX,randY,my_oval,newText])
            self.Matrix[randX][randY] = r.Id