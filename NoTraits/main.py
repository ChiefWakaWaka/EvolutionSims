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

while True:
    round += 1
    averageDup = 0
    averageDeath = 0
    averageGen = 0

    for i in range (len(bots)):
        averageDup += bots[i].duplicate
        averageDeath += bots[i].death
    averageDup /= len(bots)
    averageDeath /= len(bots)

    xAxis.append(round)
    yAxis.append(len(bots))
    plt.axis([round - 200, max(xAxis), min(yAxis) - min(yAxis)*0.1, max(yAxis) + max(yAxis)*0.1])
    plt.plot(xAxis, yAxis, color="blue")
    plt.pause(0.005)
    plt.draw()
    round += 1

    if(len(xAxis) > 200):
        yAxis.pop(0)
        xAxis.pop(0)

    print(len(bots), averageDup, averageDeath)
    #print(averageDup - averageDeath)

    for obj in bots:
        dupChance = random.uniform(0,1) < obj.duplicate
        deathChance = random.uniform(0,1) < obj.death
        if(dupChance == True):
            bots.append(Character(obj.generation + 1, obj.duplicate + random.uniform(-0.02, 0.02), 0.01, obj.xPos, obj.yPos))
        if(deathChance == True):
            bots.remove(obj)
        obj.death += 0.001
        obj.duplicate = 2 / (len(bots) + 1)

plt.show()
