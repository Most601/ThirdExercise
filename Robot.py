import random
from numpy import *

class Robot():
    
    def __init__(self, Id, x, y, IsChargable, IsStatic, NumOfRobots):
        self.Id = Id
        self.x = x
        self.y = y
        self.IsChargable = IsChargable #current: 0,1
        self.IsStatic = IsStatic
        self.NumOfRobots = NumOfRobots
        self.Battery = 100.0

    
    def Move(self):
        if(self.Battery == 0):
            return 5
        elif(self.Battery > 0):                                        
            self.BatteryStatus() 
        rand = random.randint(0,4)
        return rand
                    
    def BatteryStatus(self):
        if(self.IsChargable == 0): #in light
            self.Battery = min(100, self.Battery+0.5)  
        else:
            self.Battery = max(0, self.Battery-0.5)