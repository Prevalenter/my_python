class Plant():
    def __init__(self, a, x, y, dt, force, life):
        self.a, self.x, self.y, self.dt = a, x, y, dt
        self.life, self.force = life, force
        self.curt = 0

    def inrange(self, zombes):
        self.curt = (self.curt+1)%self.dt
        if self.curt!=0:return None
        for i in zombes:
            if i.y == self.y and i.x>self.x: return [i]
    
    def step(self):pass

    def attact(self, obj):pass
    
    def show(self, ground):
        ground[self.y, self.x] = self.a

class Bullet(Plant):
    def __init__(self, a, x, y, dt, force, life):
        self.a, self.x, self.y, self.dt = a, x, y, dt
        self.life, self.force = life, force
        self.curt = 1

    def inrange(self, zombes):
        for i in zombes:
            if i.y == self.y:
                if i.x == self.x:
                    return [i]
        return None

    def step(self):
        self.curt = (self.curt+1)%self.dt
        if self.curt == 0:self.x += 1
            
    def attact(self, obj):
        for i in obj:
            i.life -= self.force
        self.life = -1
    
class Zombe():
    def __init__(self, a, x, y, dt, force, life):
        self.a, self.x, self.y, self.dt = a, x, y, dt
        self.life, self.force = life, force
        self.curt = 0

    def inrange(self, plts):
        for i in plts:
            if i.y == self.y and i.x+1 == self.x:
                return [i]
        return None
    
    def step(self):
        self.curt = (self.curt+1)%self.dt
        if self.curt == 0:self.x -= 1

    def attact(self, objs):
        for i in objs:
            i.life -= self.force

    def show(self, ground):
        ground[self.y, self.x] = self.a
