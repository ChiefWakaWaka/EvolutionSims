from Creature import Creature
import random
import time
import matplotlib.pyplot as plt

bots = []
xAxis = []
yAxis = []
round = 0


for i in range(10):
    bots.append(Creature(1, 1, 0))

while True:
    # NOTE: reset food each round
    for obj in bots:
        obj.food = 0
        foodCnt = 5000

    # NOTE: collect food
    speeds = []
    for obj in bots:
        speeds.append(obj.speed)
    totalSpeed = sum(speeds)
    for obj in bots:
        obj.speed /= totalSpeed
        obj.food = foodCnt * obj.speed
        obj.speed *= totalSpeed

    # NOTE: deplete energy
    for obj in bots:
        energyUse = obj.speed**2
        obj.energy -= energyUse

    # NOTE: consume food
    for obj in bots:
        obj.energy += obj.food
        obj.food = 0

    # NOTE: Die or Duplicate creatures
    for obj in bots:
        if(obj.energy >= 2):
            bots.append(Creature(1, obj.energy + random.uniform(-0.01, 0.01), 0))
        elif(obj.energy >= 1):
            if(random.uniform(0, 1) < 0.01):
                bots.append(Creature(1, obj.energy + random.uniform(-0.01, 0.01), 0))
        elif(obj.energy < 1):
            bots.remove(obj)

    # NOTE: find and print average speed
    averageSpeed = []
    for obj in bots:
        averageSpeed.append(obj.speed)
    averageSpeed = (sum(averageSpeed) / len(averageSpeed))
    print(averageSpeed)

    # NOTE: create dynamic chart for population
    xAxis.append(round)
    yAxis.append(len(bots))
    plt.axis([round - 100, max(xAxis), min(yAxis) - min(yAxis)*0.1, max(yAxis) + max(yAxis)*0.1])
    plt.plot(xAxis, yAxis, color="blue")
    plt.pause(0.005)
    plt.draw()
    round += 1

    if(len(yAxis) > 100):
        yAxis.pop(0)
        xAxis.pop(0)

plt.show()
