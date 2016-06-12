import Robot
import random
import tkinter as tk
import Simulator
import numpy as np

class Arena:

    def __init__(self):
        self.x = 1000
        self.y = 1000        
        self.Matrix = np.zeros(shape = (self.x,self.y), dtype = np.int) #Matrix represents the arena
        self.StaticBots = 60 #number of static robots
        self.MoveBots = 80 #number of moving robots
        self.AllBots = 0 #number of all robots
        self.ListStaticBot = [] #list of static robots    
        self.ListMoveBot = [] #list of moving robots
        self.ListAllBots=[] #list of all robots
        self.start = False #True - running arena        
        self.root = tk.Tk()
        self.CreateGui() #creating the arena - GUI

    def CreateGui(self):  
        #creating the arena - GUI
        self.canv = tk.Canvas(self.root,width=1000, height=1000,scrollregion=(0,0,1020,1020))
        self.root.title("Simulator")
        self.sbar = tk.Scrollbar(self.root,orient=tk.VERTICAL,command=self.canv.yview) 
        self.canv.configure(yscrollcommand=self.sbar.set)
        self.sbar.pack(side=tk.RIGHT, fill=tk.Y) 
        self.button = tk.Button(self.root,text="Start",anchor=tk.W, command=self.PlayArena)
        self.button.pack(side=tk.RIGHT)
        self.canv.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def BlackFrame(self):
        #creating a black frame around arena - robots did not leave the arena
        self.Matrix = np.zeros(shape = (self.x,self.y), dtype = np.int)
        for i in range(self.x):
            self.Matrix[i][self.y - 1] = 2
            self.Matrix[i][0] = 2
        for j in range(self.y):
            self.Matrix[self.x - 1][j] = 2
            self.Matrix[0][j] = 2

    def Arena(self):
        #creating Arena.
        self.BlackFrame()

        self.canv.create_rectangle(543, 42, 743, 242, fill="gray", outline = 'gray')
        self.canv.create_rectangle(787, 85, 987, 315, fill="gray", outline = 'gray')
        self.canv.create_rectangle(85, 234, 285, 688, fill="gray", outline = 'gray')
        self.canv.create_rectangle(600, 392, 980, 500, fill="black", outline = 'black')
        
        for i in range(543,743):
            for j in range(42,242):
                self.Matrix[i][j] = 1
                
        for i in range(787,987):
            for j in range(85,315):
                self.Matrix[i][j] = 1
                
        for i in range(85,285):
            for j in range(234,688):
                self.Matrix[i][j] = 1
                
        for i in range(600,980):
            for j in range(392,500):
                self.Matrix[i][j] = 2
         
    def PlayArena(self):
        #running arena  
        self.start = True
        Simulator.startmoving(self)
        
    def NewRobots(self, EmoutOfBots, IsStatic):
        #put robots on arena
        for i in range(EmoutOfBots):
            self.AllBots = self.AllBots + 1
            x1 = 0
            y1 = 0
            while(self.Matrix[x1][y1] == 2):
                x1 = int((random.random() * (self.x - 1)) + 1)
                y1 = int((random.random() * (self.y - 1)) + 1)
            if(IsStatic):
                rob = Robot.Robot(self.AllBots+2,IsStatic,self.Matrix[x1][y1], x1, y1, self.MoveBots+self.StaticBots)
                rob.GussLocal=[x1,y1]
                my_oval = self.canv.create_oval(x1, y1, x1 + 10, y1 + 10, fill='red')
                newText = self.canv.create_text(x1,y1,anchor=tk.SW,font=("Purisa", 8),text=self.AllBots)
                self.ListAllBots.append([my_oval,self.AllBots+2])
                self.ListStaticBot.append([rob,x1,y1,my_oval,newText])

            else:
                rob = Robot.Robot(self.AllBots+2, IsStatic, self.Matrix[x1][y1], 0, 0, self.MoveBots+self.StaticBots)
                my_oval = self.canv.create_oval(x1, y1, x1 + 10, y1 + 10, fill='green')
                newText = self.canv.create_text(x1,y1,anchor=tk.SW,font=("Purisa", 8),text=self.AllBots)
                self.ListAllBots.append([my_oval,self.AllBots+2])
                self.ListMoveBot.append([rob,x1,y1,my_oval,newText])
            self.Matrix[x1][y1] = rob.Id
