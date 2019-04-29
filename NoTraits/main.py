from Character import Character
import random
import time
import math

import matplotlib.pyplot as plt

bots = []
xAxis = []
yAxis = []
dupList = []
deathList = []
round = 0

for i in range (5):
    bots.append(Character(0 ,0.1, 0.01, random.randint(0, 100), random.randint(0, 100)))

for i in range(100):
    round += 1
    averageDup = 0
    averageDeath = 0
    averageGen = 0

    for i in range (len(bots)):
        averageDup += bots[i].duplicate
        averageDeath += bots[i].death
        averageGen += bots[i].generation
    averageDup /= len(bots)
    averageDeath /= len(bots)
    averageGen /= len(bots)

    xAxis.append(round)
    yAxis.append(len(bots))
    dupList.append(averageGen)
    deathList.append(averageDeath)
    plt.axis([1, max(xAxis), 0, max(yAxis) * 1.5])
    #plt.plot(xAxis, deathList, color="blue")
    #plt.plot(xAxis, dupList, color="orange")
    plt.plot(xAxis, yAxis, color="blue")
    plt.pause(0.005)
    plt.draw()

    print(len(bots), averageDup, averageDeath)

    for obj in bots:
        dupChance = random.uniform(0,1) < obj.duplicate
        deathChance = random.uniform(0,1) < obj.death
        if(dupChance == True):
            bots.append(Character(obj.generation + 1, obj.duplicate + random.uniform(-0.02, 0.02), obj.death + random.uniform(-0.02, 0.02), obj.xPos, obj.yPos))
        if(deathChance == True):
            bots.remove(obj)
        obj.death += 0.001
        obj.duplicate = 2 / (len(bots) + 1)

plt.show()
