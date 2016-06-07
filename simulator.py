import Arena


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



if __name__ == "__main__":
    main()


