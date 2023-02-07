#
# Author : 
# ID : 
#
# test3.py - Basic simulation of Teletubbies
#

import random
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
import numpy as np
import time
from WandaFish import Clownfish
from WandaCrab import Crab
from WandaFood import Food
    
# def directive(ttime):
#     '''directive - takes the iteration count (loop counter), coverts to time of day (24-hour clock)
#                    then returns directive for Teletubbies

#     ttime - loop counter
#     '''
#     ttime = ttime%24

#     if ttime == 6:
#         directive = "feed"
#     else:
#         directive = "swim"
    
#     return directive


def plotFish(fList):
    '''plotFish - plots all the Fish using a scatter plot

    fList - list of Fish
    '''
    xvalues = []
    yvalues = []
    sizes = []
    
    for f in fList:
        xvalues.append(f.getPos()[0])
        yvalues.append(f.getPos()[1])
        sizes.append(f.getSize())
        
    plt.scatter(xvalues, yvalues, s=sizes, color="orange", marker="o") 
    plt.scatter(xvalues, yvalues, s=sizes, color="orange", marker="o") 

def plotCrab(cList):
    
    xvalues = []
    yvalues = []
    sizes = []
    
    for c in cList:
        xvalues.append(c.getPos()[0])
        yvalues.append(c.getPos()[1])
        sizes.append(c.getSize())
        
    plt.scatter(xvalues, yvalues, s=sizes, color="red", marker="x") 

def plotFood(eList):
    
    xvalues = []
    yvalues = []
    size = []
    
    for e in eList:
        xvalues.append(e.getPos()[0])
        yvalues.append(e.getPos()[1])
        size.append(e.getSize())
        
    plt.scatter(xvalues, yvalues, s=size, color="brown", marker="h") 

def plotBackground(water, rock, sand, limits):
    plt.gca().add_patch(Rectangle(water[0], water[1], water[2], facecolor=water[3], zorder=0))
    plt.gca().add_patch(Rectangle(sand[0], sand[1], sand[2], facecolor=sand[3], zorder=0))
    plt.gca().add_patch(Circle(rock[0], rock[1], edgecolor=rock[2], fill=True, zorder=0))

XMAX = 500
YMAX = 400
    
def main():
    water = [(0,0), XMAX, YMAX, "lightblue"]
    sand = [(0,0), XMAX, YMAX-300, "yellow"]
    rock = [(XMAX/10, (YMAX-100)/10), 80, "grey"]
    fnames = ["Nemo", "Marlin"]
    cnames = ["Sebastian"]
    fish = []
    crab = []
    food = []
    limits = (XMAX, YMAX)
    
    for i in range(len(fnames)):
        xpos = random.randint(0, water[1])
        ypos = random.randint(0, water[2])
        fish.append(Clownfish(fnames[i], (xpos,ypos), "orange"))

    for i in range(len(cnames)):
        xpos = random.randint(0, sand[1])
        ypos = random.randint(0, sand[2])
        crab.append(Crab(cnames[i], (xpos,ypos), "red"))

    for i in range(10):
        xpos = random.randint(250, water[1])
        ypos = random.randint(350, water[2])
        food.append(Food((xpos,ypos), "brown"))
     
    for i in range(0, 15, 1):
        print("\n####### TIMESTEP ",i, "#######")
    
        for f in fish:
            f.stepChange(limits)
        for c in crab:
            c.stepChange(limits)
        for e in food:
            e.stepChange(limits)

        # Movement and interaction

    

        # mode = directive(i)
        # if mode == "feed":
        # elif mode == "swim":
        
        ax = plt.gca()         
        ax.set_aspect(1)         
        plt.xlim(0,limits[0])
        plt.ylim(0,limits[1])

        plotBackground(water, rock, sand, limits)
        plotFish(fish)
        plotCrab(crab)
        plotFood(food)
        
        plt.pause(1)
        plt.clf()
    
if __name__ == "__main__":
    main()
