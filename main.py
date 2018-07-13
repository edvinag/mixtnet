import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random as rnd

class node:

    def __init__(self):
        self.point = [rnd.uniform(0, 10), rnd.uniform(0, 10)]
        self.connections = []
        self.power = 1


    def getpower(self):
        return self.power


    def getpoint(self):
        return self.point


    def shoot(self, power):
        plt.title("Power: %d" % power)
        if power > 0.01:
            for c in self.connections:
                plot(self, c, power)
            self.power += power * 0.5
            if len(self.connections) > 0:
                return [self.connections, power*0.5]
        else:
            self.power += power * 0.5
        return None


def plot(n, c, power):
    plt.scatter(n.point[0], n.point[1], c=[1, 0, 0], s=pow(n.power * 3, 2), zorder=4)
    plt.plot([n.point[0], c[0].point[0]], [n.point[1], c[0].point[1]], c=[1, 0.5, 0.5], linewidth=pow(3*c[1], 2), zorder=3)


def plotall():
    for n in nodes:
        plt.scatter(n.point[0], n.point[1], c=[0, 0, 0], s=pow(n.power * 3, 2), zorder=2)
        for c in n.connections:
            plt.plot([n.point[0], c[0].point[0]], [n.point[1], c[0].point[1]], c=[0.5, 0.5, 0.5], linewidth=1, zorder=1)
    plt.draw()

nodes = []
for _ in range(10):
    n = node()
    nodes.append(node())

for n in nodes:
    subnodes = nodes.copy()
    subnodes.pop(subnodes.index(n))
    for c in rnd.sample(subnodes, rnd.randint(1, 5)):
        n.connections.append([c, rnd.uniform(0.1, 0.7)])

fig = plt.figure()
for time in range(1000):
    plt.clf()
    toshoot = []
    toshoot.append(nodes[0].shoot(1))
    plotall()
    plt.pause(0.00001)
    for _ in range(100):
        newtoshoot = {}
        for c in toshoot:
            if c is not None:
                for n in c[0]:
                    if n[0] not in newtoshoot:
                        newtoshoot[str(n[0])] = [n[0], c[1]*n[1]]
                    else:
                        newtoshoot[str(n[0])][1] += c[1]*n[1]
        toshoot = []
        plt.clf()
        for key, value in newtoshoot.items():
            s = value[0].shoot(value[1])
            if s is not None:
                toshoot.append(s)
        plotall()
        print(toshoot)
        if len(toshoot) == 0:
            break

        plt.pause(0.00001)

    plotall()

plt.show()

'''
for n in nodes:
    print("node")
    plt.scatter(n.point[0], n.point[1], c=[0, 0, 0], s=n.power*10, zorder=2)
    plt.draw()
    plt.pause(0.1)
    for c in n.connections:
        plt.plot([n.point[0], c[0].point[0]], [n.point[1], c[0].point[1]], c=[0.5, 0.5, 0.5], linewidth=1, zorder=1)
        # ax.arrow(n.point[0], n.point[1], c[0].point[0]-n.point[0], c[0].point[1]-n.point[1], head_width=1, head_length=0.5, fc='k', ec='k')
        plt.draw()
        plt.pause(0.1)
        print("- connection")

plt.show()





for n in nodes:
    subnodes = nodes.copy()
    subnodes.pop(subnodes.index(n))
    for c in rnd.sample(subnodes, rnd.randint(0, 3)):
        n.connections.append([c, rnd.uniform(0, 0.5)])


for n in nodes:
    plt.scatter(n.point[0], n.point[1], c=[0, 0, 0], s=n.power*10, zorder=2)
    for c in n.connections:
        plt.plot([n.point[0], c[0].point[0]], [n.point[1], c[0].point[1]], c=[1-c[1], 1-c[1], 1-c[1]], linewidth=c[1], zorder=1)

plt.show()
'''