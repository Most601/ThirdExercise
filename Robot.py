# -*- coding: utf-8 -*-
import random
import sys
import math
from numpy import *
#new
class Robot():

    def __init__(self, Id, IsStatic, IsChargable, x, y, NumOfRobots):
        self.Id = Id
        self.x = x
        self.y = y
        self.IsChargable = IsChargable 
        self.NumOfRobots = NumOfRobots
        self.IsStatic = IsStatic
        self.Battery = 100.0
        self.NextStep = -1
        self.Step = 7
        self.LastStepWhite = False
        self.MyNeighbor = -1
        self.GussLocal = [500,500]
        self.AllMessage = [None]*(self.NumOfRobots+3)
        self.indexOfNeighbors=[]
        self.sendMessage = False                               
        self.message = [self.Id, self.IsStatic, self.IsChargable, self.x, self.y]
        self.SendMessage = False
    
    def BatteryStatus(self):
        if(self.IsChargable == 0): #in light
            self.Battery = min(self.Battery+0.5, 100)  
        else:
            self.Battery = max(self.Battery-0.5, 0)
    
    def Move(self):
        if(self.Battery == 0):#dead
            return 5
        self.BatteryStatus() #update battery
        if(self.IsChargable == 0):
            self.NextStep = -1
            self.LastStepWhite = True
            Rand = int(random.random()*100)+1
            if(Rand < 60):
                self.Step = self.GoToClosestNeighbor()
                return self.Step
            else:
                self.Step = int(random.random()*4)
                return self.Step
        else:
            if(self.LastStepWhite):
                return self.GoBack()
            else:
                self.Step = self.GoToClosestNeighbor()
                return self.Step

    def GoToClosestNeighbor(self): #white area.
        MinimumI = -1
        minDist = sys.maxsize
        for i in self.indexOfNeighbors:
            LastMessage = self.AllMessage[i]
            if((LastMessage[0][2] == 0) and (LastMessage[1] < minDist)):
                minDist = LastMessage[1]
                MinimumI = i

        if (MinimumI == -1 ):#no neighbors in the light
            rand = int(random.random()*4)
            if(self.NextStep == -1):
                self.NextStep = rand
                return rand
            else:
                return self.NextStep

        else:#neighbors in light - go to him
            ClosestNeighbor = self.AllMessage[MinimumI]
            NewX = self.x - ClosestNeighbor[0][3]
            NewY = self.y - ClosestNeighbor[0][4]
            self.MyNeighbor = ClosestNeighbor
            if (NewX < 0):
                return 0
            elif (NewX > 0):
                return 1
            elif (NewY < 0):
                return 2
            elif (NewY > 0):
                return 3

    def GoBack(self):
        if(self.Step == 0):#now in right go to left
            return 1
        elif(self.Step == 1):#now in left go to right
            return 0
        elif (self.Step == 2):#now up go to down
            return 3
        elif (self.Step == 3):#now down go to up
            return 2

    def SendMessage(self):
        if(self.Battery > 0):
            self.Message = [self.id, self.IsStatic, self.IsChargable, self.x, self.y]
            if(self.IsStatic):
                self.SendMessage = True
            elif(len(self.indexOfNeighbors) > 3): #moving bot sends to neighbors if knows its location
                self.SendMessage = True

    def GetMessage(self):
        self.SendMessage = False
    
    def Guess(self):#guess robot location
        self.Radius = 500
        self.GussLocal = [1000,1000]
        while (self.Radius > 1):
            GuessPointsAround = self.PointsAround()#4 new guesses around the current guess location
            errors = []
            for g in GuessPointsAround:
                errors.append(self.RMS(g)) #calculation RMS save in list errors
            i = errors.index(min(errors)) #error min = best guess location
            self.GussLocal = GuessPointsAround[i] #save the best guess
            self.x = abs(self.GussLocal[0])
            self.y = abs(self.GussLocal[1])
            self.Radius = self.Radius / 2

    def RMS(self, g):#Formula for calculating the approximate point  
        ListOfDist =[]
        for i in self.indexOfNeighbors:
            LastMessage = self.AllMessage[i]
            Dist = self.Distance(LastMessage[0][3], LastMessage[0][4], g[0], g[1])
            realDist = LastMessage[1]
            Dist = math.pow((Dist-realDist),2)
            ListOfDist.append(Dist)
        return math.sqrt(sum(ListOfDist)/len(ListOfDist))

    def PointsAround(self):#4 guesses around the current guess
        G_x = self.GussLocal[0]
        G_y = self.GussLocal[1]
        return [self.GussLocal, [G_x + self.Radius, G_y], [G_x, G_y + self.Radius],[G_x - self.Radius, G_y], [G_x, G_y - self.Radius]]
    
    def Distance(self, x1, y1, x2, y2):
        return math.sqrt(math.pow(x1-x2,2)+ math.pow(y1-y2,2))