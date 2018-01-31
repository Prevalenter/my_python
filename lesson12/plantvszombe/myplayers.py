from spirit import *

class Bullet1(Bullet):
    def __init__(self, x, y):
        Bullet.__init__(self, '.', x, y, 1, 5, 100)

class Bullet2(Bullet):
    def __init__(self, x, y):
        Bullet.__init__(self, 'o', x, y, 1, 20, 100)
        
class Plantf(Plant):
    def __init__(self, x, y):
        Plant.__init__(self, 'f', x, y, 3, 10, 100)

    def attact(self, obj):
        return Bullet1(self.x+1, self.y)

class PlantF(Plant):
    def __init__(self, x, y):
        Plant.__init__(self, 'F', x, y, 8, 10, 150)

    def attact(self, obj):
        return Bullet2(self.x+1, self.y)

class Zombez(Zombe):
    def __init__(self, x, y):
        Zombe.__init__(self, 'z', x, y, 2, 10, 100)

class ZombeZ(Zombe):
    def __init__(self, x, y):
        Zombe.__init__(self, 'Z', x, y, 3, 20, 200)

class Bullet3(Bullet):
    def __init__(self, x, y):
        Bullet.__init__(self, '.', x, y, 1, 2, 100)

# 只能修改以下部分，实现战局逆转
class PlantHomework(Plant):
    def __init__(self, x, y):
        Plant.__init__(self, '7', x, y, 3, 10, 100)
    def attact(self, obj):
        return BulletHomework(self.x-1, self.y)
    #重写攻击范围函数，植物7可以向后攻击
    def inrange(self, zombes):
        self.curt = (self.curt+1)%self.dt
        if self.curt!=0:return None
        for i in zombes:
            if i.y == self.y : return [i]
class BulletHomework(Bullet):
    def __init__(self, x, y):
        Bullet.__init__(self, '<', x, y, 1, 10, 100)
        #重写攻击的豆子的移动方式，是向后移动
    def step(self):
        self.curt = (self.curt+1)%self.dt
        if self.curt == 0:self.x -= 1       
        return None        

