import Arena
import random
import math


def main():
    a = Arena.Arena()
    a.RandomArena()
    a.NewRobots(a.StaticBots, True)
    a.NewRobots(a.MoveBots, False)
    moveRobot(a)
    a.root.mainloop()


def moveRobot(arena):
    while(arena.start):
        for i in arena.ListMoveBot:
            Step = i[0].Move()
            if (Step == 0):
                if (arena.Matrix[i[1] + 1][i[2]] != 2):
                    arena.Matrix[i[1]][i[2]] = i[0].IsChargable
                    i[0].IsChargable = arena.Matrix[i[1] + 1][i[2]]
                    arena.Matrix[i[1] + 1][i[2]] = i[0].Id
                    i[1] = i[1] + 1
                    i[0].x = i[0].x + 1
                    arena.canv.move(i[3], 1, 0)
                    arena.canv.move(i[4], 1, 0)
                    arena.canv.update()
            elif (Step == 1):
                if (arena.Matrix[i[1] - 1][i[2]] != 2):
                    arena.Matrix[i[1]][i[2]] = i[0].IsChargable
                    i[0].IsChargable = arena.Matrix[i[1] - 1][i[2]]
                    arena.Matrix[i[1] - 1][i[2]] = i[0].Id
                    i[1] = i[1] - 1
                    i[0].x = i[0].x - 1
                    arena.canv.move(i[3], -1, 0)
                    arena.canv.move(i[4], -1, 0)
                    arena.canv.update()
            elif (Step == 2):
                if (arena.Matrix[i[1]][i[2] + 1] != 2):
                    arena.Matrix[i[1]][i[2]] = i[0].IsChargable
                    i[0].IsChargable = arena.Matrix[i[1]][i[2] + 1]
                    arena.Matrix[i[1]][i[2] + 1] = i[0].Id
                    i[2] = i[2] + 1
                    i[0].y = i[0].y - 1
                    arena.canv.move(i[3], 0, 1)
                    arena.canv.move(i[4], 0, 1)
                    arena.canv.update()
            elif (Step == 3):  # step down
                if (arena.Matrix[i[1]][i[2] - 1] != 2):
                    arena.Matrix[i[1]][i[2]] = i[0].IsChargable
                    i[0].IsChargable = arena.Matrix[i[1]][i[2] - 1]
                    arena.Matrix[i[1]][i[2] - 1] = i[0].Id
                    i[2] = i[2] - 1
                    i[0].y = i[0].y + 1
                    arena.canv.move(i[3], 0, -1)
                    arena.canv.move(i[4], 0, -1)
                    arena.canv.update()

            if (i[0].Battery == 0):
                arena.canv.itemconfig(i[3], fill="black")
            elif ((i[0].Battery < 50) and (i[0].Battery > 0)):
                arena.canv.itemconfig(i[3], fill="yellow")

def SendMSG(arena): #bot - get or send mesage.
    for i in arena.StaticBots:
        rand = random.randint(0,1)
        if(rand == 0):
            i[0].GetMessage()
        else:
            i[0].SendMessage()
    for rob in arena.MoveBots:
        rand = random.randint(0,1)
        if (rand ==0):
            i[0].GetMessage()
        else:
            i[0].GetMessage()
    MyAir(arena)

def MyAir(arena): #Check bot recived messages.
    SendBots = []
    ReciveBots = []
    
    for i in arena.StaticBots:
        if i[0].SendMessage:
            SendBots.append(i)
        else:
            ReciveBots.append(i)

    for rob in arena.MoveBots:
        if i[0].SendMessage:
            SendBots.append(i)
        else:
            ReciveBots.append(i)

    for i in ReciveBots:
        if (len(SendBots) != 0):
            MBot = SendBots[0]
            minDis = RDistance(i,MBot)
    
            for j in SendBots:
                dis = RDistance(i,j)
                if(dis < minDis):
                    MBot = j
                    minDis = dis
            if (minDis < 500):
                i[0].AllMessages[MBot[0].id] = ([MBot[0].Message ,minDis])#update id 
                if(MBot[0].id not in i[0].indexOfNeighbors):
                    i[0].indexOfNeighbors.append(MBot[0].id)#add to neighbors
                if not(i[0].IsStatic):
                    i[0].Guess()


def RDistance(i,j):#distance between the robots.
    x1 = i[1]
    x2 = j[1]
    y1 = i[2]
    y2 = j[2]
    dis = math.sqrt(math.pow(x1-x2,2)+ math.pow(y1-y2,2))
    return dis * random.unifrom(0.8,1.2)
                  
if __name__ == "__main__":
    main()


