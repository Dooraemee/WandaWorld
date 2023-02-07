from random import random

class Fish():
    def __init__(self, name, pos, size, colour) -> None:
        self.name = name
        self.startpos = pos
        self.xpos = pos[0]
        self.ypos = pos[1]
        self.size = size
        self.colour = colour

    def __str__(self):
        return str(self)
    
    def getPos(self):
        return (self.xpos, self.ypos)
            
    def getName(self):
        return self.name

    def getColour(self):
        return self.colour
    
    def tick(self):
        pass
        

    def getSize(self):
        return self.size

    def get_point(self) -> tuple[int, int, int, str]:
        return (self.xpos, self.ypos, self.size, self.colour)
    


class Clownfish(Fish):

    def __init__(self,name,  pos): 
        super().__init__(name, pos, 20, "orange")

    def eaten(self):
        print("Clownfish was eaten")

    def tick(self):
        super().tick()
        xmov = random.choice([20,-20])
        ymov = random.choice([20,-20])
        self.xpos += xmov
        self.ypos -= ymov

# class Crab(Fish):
#     def __init__(self, name, pos, colour):
#         Fish().__init__(self, name, pos, colour)
    
#     def getPos(self):
#         return (self.xpos, self.ypos)
            
#     def getName(self):
#         return self.name
                                
#     def getSize(self):
#         return self.size

#     def getColour(self):
#         return self.colour
    
#     def stepChange(self, limits):
#         xmov = 30
#         self.xpos += xmov
        

#     def attack(self):
#         print("Crab attacked fish")