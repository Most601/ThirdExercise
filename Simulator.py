import Arena
import random
import math

def main():
    New_Arena = Arena.Arena()
    New_Arena.Arena()
    New_Arena.NewRobots(New_Arena.StaticBots, True)
    New_Arena.NewRobots(New_Arena.MoveBots, False)
    startmoving(New_Arena)
    New_Arena.root.mainloop()

def startmoving(arena):
    #move the robot in the GUI and update the location of robot in Matrix.
    while(arena.start):
        for i in arena.ListMoveBot:
            Step = i[0].StartMoving()
            if (Step == 0):
                if (arena.Matrix[i[1] + 1][i[2]] == 0 or arena.Matrix[i[1] + 1][i[2]] == 1):
                    arena.Matrix[i[1]][i[2]] = i[0].IsChargable
                    i[0].IsChargable = arena.Matrix[i[1] + 1][i[2]]
                    arena.Matrix[i[1] + 1][i[2]] = i[0].Id
                    i[1] = i[1] + 1
                    i[0].x = i[0].x + 1
                    arena.canv.move(i[3], 1, 0)
                    arena.canv.move(i[4], 1, 0)
                    arena.canv.update()
            elif (Step == 1):
                if (arena.Matrix[i[1] - 1][i[2]] == 0 or arena.Matrix[i[1] - 1][i[2]] == 1):
                    arena.Matrix[i[1]][i[2]] = i[0].IsChargable
                    i[0].IsChargable = arena.Matrix[i[1] - 1][i[2]]
                    arena.Matrix[i[1] - 1][i[2]] = i[0].Id
                    i[1] = i[1] - 1
                    i[0].x = i[0].x - 1
                    arena.canv.move(i[3], -1, 0)
                    arena.canv.move(i[4], -1, 0)
                    arena.canv.update()
            elif (Step == 2):
                if (arena.Matrix[i[1]][i[2] + 1] == 0 or arena.Matrix[i[1]][i[2] + 1] == 1):
                    arena.Matrix[i[1]][i[2]] = i[0].IsChargable
                    i[0].IsChargable = arena.Matrix[i[1]][i[2] + 1]
                    arena.Matrix[i[1]][i[2] + 1] = i[0].Id
                    i[2] = i[2] + 1
                    i[0].y = i[0].y - 1
                    arena.canv.move(i[3], 0, 1)
                    arena.canv.move(i[4], 0, 1)
                    arena.canv.update()
            elif (Step == 3):  # step down
                if (arena.Matrix[i[1]][i[2] - 1] == 0 or arena.Matrix[i[1]][i[2] - 1] == 1):
                    arena.Matrix[i[1]][i[2]] = i[0].IsChargable
                    i[0].IsChargable = arena.Matrix[i[1]][i[2] - 1]
                    arena.Matrix[i[1]][i[2] - 1] = i[0].Id
                    i[2] = i[2] - 1
                    i[0].y = i[0].y + 1
                    arena.canv.move(i[3], 0, -1)
                    arena.canv.move(i[4], 0, -1)
                    arena.canv.update()
                    
            if int(i[0].Battery == 50):
                arena.canv.itemconfig(i[3], fill="green")
            elif (i[0].Battery == 0):
                arena.canv.itemconfig(i[3], fill="black")
            elif ((i[0].Battery < 50) and (i[0].Battery > 0)):
                arena.canv.itemconfig(i[3], fill="yellow")
        SendMSG(arena)

def SendMSG(arena):
    #determine which robots send/receive a message
    for i in arena.ListStaticBot:
        Rand = int(random.random()*2)
        if(Rand == 0):
            i[0].GetMessage()
        else:
            i[0].SendMessage()
    for i in arena.ListMoveBot:
        Rand = int(random.random()*2)
        if (Rand == 0):
            i[0].GetMessage()
        else:
            i[0].GetMessage()
    MyAir(arena)

def MyAir(arena): 
    #Check that all robots recived messages.
    SendBots = []
    ReciveBots = []
    
    for i in arena.ListStaticBot:
        if i[0].SendMessage:
            SendBots.append(i)
        else:
            ReciveBots.append(i)

    for i in arena.ListMoveBot:
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
                #update id 
                i[0].TotalMessages[MBot[0].id] = ([MBot[0].MSG ,minDis])
                if(MBot[0].id not in i[0].IndexSent):
                    #add to neighbors
                    i[0].IndexSent.append(MBot[0].id)
                if not(i[0].IsStatic):
                    i[0].Guess()

def RDistance(i,j):
    #distance between the robots.
    x1 = i[1]
    x2 = j[1]
    y1 = i[2]
    y2 = j[2]
    dis = math.sqrt(math.pow(x1-x2,2)+ math.pow(y1-y2,2))
    return dis * random.unifrom(0.8,1.2)
 
                  
if __name__ == "__main__":
    main()
