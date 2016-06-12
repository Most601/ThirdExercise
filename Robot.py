import random
import sys
import math

class Robot():

    def __init__(self, Id, IsStatic, IsChargable, x, y, NumOfBots):
        self.Id = Id #the robot ID
        self.x = x #coordinate x of the robot(location)
        self.y = y #coordinate y of the robot(location)
        self.IsChargable = IsChargable #True - robot on gray or white
        self.NumOfBots = NumOfBots #number of all robots
        self.Battery = 100.0 #robot's battery full
        self.IsStatic = IsStatic #True - static robot  
        self.NextStep = -1 #the next step of the robot
        self.Step = 7 #the last step of the robot
        self.LastStepWhite = False #the last step on white of the robot 
        self.MyNeighbor = -1 #current nearest robot
        self.GussLocal = [500,500] #guess location
        self.TotalMessages = [None]*(self.NumOfBots+3) #all messages sent that were sent
        self.IndexSent=[] #the robot from which the message was sent
        self.Sender = False #thr robots that sends a message                              
        self.MSG = [self.Id, self.IsStatic, self.IsChargable, self.x, self.y] #contents of the message
        
    
    def BatteryStatus(self):
        #rechargeable battery - robot in light
        #battery running low - robot in gray
        if(self.IsChargable == 0):
            self.Battery = min(self.Battery+1, 100)  
        else:
            self.Battery = max(self.Battery-1, 0)
    
    def StartMoving(self):
        #the function returns a number between 0-3 or 5
        # 0 - step right
        # 1 - step left
        # 2 - step up
        # 3 - step down
        # 5 - robot dead
        if(self.Battery == 0):#dead
            return 5
        self.BatteryStatus() #update battery
        if(self.IsChargable == 0):
            #robot in light do random move.
            self.NextStep = -1
            self.LastStepWhite = True
            Rand = int(random.random()*100)+1
            if(Rand < 60):
                #looking for light at neighbors
                self.Step = self.GoToClosestNeighbor()
                return self.Step
            else:
                #do random move
                self.Step = int(random.random()*4)
                return self.Step
        else:
            #robot is not in light - look if last step was light
            if(self.LastStepWhite):
                return self.GoBack()
            else:
                #looking for light at neighbors
                self.Step = self.GoToClosestNeighbor()
                return self.Step

    def GoToClosestNeighbor(self):
        #looking for light at neighbors
        index = -1
        dist = sys.maxsize
        for i in self.IndexSent:
            LastMessage = self.TotalMessages[i]
            if((LastMessage[0][2] == 0) and (LastMessage[1] < dist)):
                dist = LastMessage[1]
                index = i

        if (index == -1 ):
            #no neighbors in the light do random move
            Rand = int(random.random()*4)
            if(self.NextStep == -1):
                self.NextStep = Rand
                return Rand
            else:
                return self.NextStep

        else:
            #neighbors in light - go to him
            ClosestNeighbor = self.TotalMessages[index]
            NewX = self.x - ClosestNeighbor[0][3]
            NewY = self.y - ClosestNeighbor[0][4]
            self.MyNeighbor = ClosestNeighbor
            if (NewY > 0):
                return 3
            elif (NewY < 0):
                return 2
            elif (NewX > 0):
                return 1
            elif (NewX < 0):
                return 0

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
            #check if robot have battery
            self.MSG = [self.Id, self.IsStatic, self.IsChargable, self.x, self.y]
            if(self.IsStatic):
                #if static robot - can send message
                self.Sender = True
                #if not static - can send only if knows location - have more than 3 neighbors
            elif(len(self.IndexSent) > 3):
                self.Sender = True

    def GetMessage(self):
        #robot that receives a message can not send a message
        self.Sender = False
    
    def Guess(self):
        #guess robot location
        self.Radius = 500
        self.GussLocal = [1000,1000]
        while (self.Radius > 1):
            #4 new guesses around the current guess location
            GuessPointsAround = self.PointsAround()
            errors = []
            for g in GuessPointsAround:
                #calculation RMS save in list errors
                errors.append(self.RMS(g))
            #error min = best guess location
            i = errors.index(min(errors))
            #save the best guess
            self.GussLocal = GuessPointsAround[i] 
            self.x = abs(self.GussLocal[0])
            self.y = abs(self.GussLocal[1])
            self.Radius = self.Radius / 2

    def RMS(self, gus):
        #formula for calculating the approximate point  
        ListOfDist =[]
        for i in self.IndexSent:
            LastMessage = self.TotalMessages[i]
            Dist = self.Distance(LastMessage[0][3], LastMessage[0][4], gus[0], gus[1])
            realD = LastMessage[1]
            Dist = math.pow((Dist-realD),2)
            ListOfDist.append(Dist)
        return math.sqrt(sum(ListOfDist)/len(ListOfDist))

    def PointsAround(self):
        #4 guesses around the current guess
        G_x = self.GussLocal[0]
        G_y = self.GussLocal[1]
        return [self.GussLocal, [G_x + self.Radius, G_y], [G_x, G_y + self.Radius],[G_x - self.Radius, G_y], [G_x, G_y - self.Radius]]
    
    def Distance(self, x1, y1, x2, y2):
        return math.sqrt(math.pow(x1-x2,2)+ math.pow(y1-y2,2))
