from BlueCreature import BlueCreature
from GreenCreature import GreenCreature
from RedCreature import RedCreature
from OrangeCreature import OrangeCreature
import random
import matplotlib.pyplot as plt

def main():
    plt.clf()
    blueCnt = []
    greenCnt = []
    redCnt = []
    orangeCnt = []
    xAxis = []
    blueTimeline = []
    redTimeline = []
    greenTimeline = []
    orangeTimeline = []
    totalTimeline = []
    round = 0

    startCnt = 50
    graphUpdate = 2
    graphHistoryLength = 200

    blueBRate = 0
    blueDRate = 0.1
    blueRRate = 0.05
    blueRRRate = 0.1
    blueRGRate = 0.1

    redBRate = 0
    redDRate = 0.05
    redRRate = 0.05
    redRORate = 0.05

    greenBRate = 0
    greenDRate = 0.1
    greenRRate = 0.1

    orangeBRate = 0
    orangeDRate = 0.05
    orangeRRate = 0.1

    for i in range(startCnt):
        blueCnt.append(BlueCreature(blueBRate, blueDRate, blueRRate, blueRRRate, blueRGRate))

    while True:
        totalCnt = len(blueCnt) + len(greenCnt) + len(redCnt) + len(orangeCnt)
        if(random.uniform(0,1) < blueBRate):
            blueCnt.append(BlueCreature(blueBRate, blueDRate, blueRRate, blueRRRate, blueRGRate))
        for obj in blueCnt:
            obj.dRate = blueDRate + ( 0.001 * totalCnt )
            if(random.uniform(0,1) < obj.dRate):
                blueCnt.remove(obj)
            if(random.uniform(0,1) < obj.rRate):
                blueCnt.append(BlueCreature(blueBRate, blueDRate, blueRRate, blueRRRate, blueRGRate))
                if(random.uniform(0,1) < obj.mRRate):
                    redCnt.append(RedCreature(redBRate, redDRate, redRRate, redRORate))
                elif(random.uniform(0,1) < obj.mGRate):
                    greenCnt.append(GreenCreature(greenBRate, greenDRate, greenRRate))

        for obj in redCnt:
            obj.dRate = redDRate + ( 0.001 * totalCnt )
            if(random.uniform(0,1) < obj.dRate):
                redCnt.remove(obj)
            if(random.uniform(0,1) < obj.rRate):
                redCnt.append(RedCreature(redBRate, redDRate, redRRate, redRORate))
                if(random.uniform(0,1) < obj.mORate):
                    orangeCnt.append(OrangeCreature(orangeBRate, orangeDRate, orangeRRate))

        for obj in greenCnt:
            obj.dRate = greenDRate + ( 0.001 * totalCnt )
            if(random.uniform(0,1) < obj.dRate):
                greenCnt.remove(obj)
            if(random.uniform(0,1) < obj.rRate):
                greenCnt.append(GreenCreature(greenBRate, greenDRate, greenRRate))

        for obj in orangeCnt:
            obj.dRate = orangeDRate + ( 0.001 * totalCnt )
            if(random.uniform(0,1) < obj.dRate):
                orangeCnt.remove(obj)
            if(random.uniform(0,1) < obj.rRate):
                orangeCnt.append(OrangeCreature(orangeBRate, orangeDRate, orangeRRate))

        print(len(blueCnt), len(redCnt), len(greenCnt), len(orangeCnt))

        xAxis.append(round)
        blueTimeline.append(len(blueCnt))
        redTimeline.append(len(redCnt))
        greenTimeline.append(len(greenCnt))
        orangeTimeline.append(len(orangeCnt))
        totalTimeline.append(totalCnt)
        round += 1
        if(round % graphUpdate == 0):
            plt.axis([round - graphHistoryLength, max(xAxis), 0, max(totalTimeline)])
            plt.plot(xAxis, blueTimeline, color="blue")
            plt.plot(xAxis, redTimeline, color="red")
            plt.plot(xAxis, greenTimeline, color="green")
            plt.plot(xAxis, orangeTimeline, color="orange")
            plt.pause(0.005)
            plt.draw()
            if(len(xAxis) > graphHistoryLength):
                blueTimeline.pop(0)
                redTimeline.pop(0)
                greenTimeline.pop(0)
                orangeTimeline.pop(0)
                xAxis.pop(0)

        if(totalCnt == 0):
            break
        if(len(orangeCnt) > 60):
            break

while True:
    blueCnt = []
    greenCnt = []
    redCnt = []
    orangeCnt = []
    totalCnt = len(blueCnt) + len(greenCnt) + len(redCnt) + len(orangeCnt)
    main()
