import numpy as np
from myplayers import *
import time, os

class Manager():
    def __init__(self):
        self.ground = np.zeros((6,50), dtype=str)
        self.plants = []
        self.zombes = []

    def show(self):
        self.ground[:] = ' '
        for i in self.plants:
            i.show(self.ground)
        for i in self.zombes:
            i.show(self.ground)
        print('\n')
        print('-'*50)
        for i in self.ground:
            print(''.join(i))
            print('-'*50)

    def remove(self):
        self.plants = [i for i in self.plants if i.life>0 and i.x>=0 and i.x<50]
        self.zombes = [i for i in self.zombes if i.life>0]

    def check(self):
        if len(self.zombes)==0:return 1
        for i in self.zombes:
            if i.x<0:return -1
        return 0
    
    def step(self):
        for i in self.plants:
            obj = i.inrange(self.zombes)
            
            if not obj is None:
                rst = i.attact(obj)
                if not rst is None:
                    self.plants.append(rst)
                    
            else: i.step()
        for i in self.zombes:
            obj = i.inrange(self.plants)
            if obj is None: i.step()
            else: i.attact(obj)
        self.remove()

    def addplant(self, plant):
        self.plants.append(plant)

    def addzombe(self, zomeb):
        self.zombes.append(zomeb)

    def mainloop(self):
        while True:
            #a = os.system('cls')
            self.step()
            self.show()
            sta = self.check()
            if sta==1: print('Plant Win')
            if sta==-1: print('Zombe Win')
            if sta!=0:
                input()
                break
            time.sleep(0.2)

manager = Manager()
manager.addplant(Plantf(0,2))
manager.addzombe(Zombez(49, 2))
manager.addplant(PlantF(0,3))
manager.addzombe(ZombeZ(40, 3))
manager.addplant(PlantHomework(49, 5))
manager.addzombe(ZombeZ(40, 5))
manager.mainloop()

        

    
