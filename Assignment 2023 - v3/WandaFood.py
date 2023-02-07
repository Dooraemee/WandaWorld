import random

class Food:
    def __init__(self, pos, colour):
        self.startpos = pos
        self.xpos = pos[0]
        self.ypos = pos[1]
        self.size = 10
        self.colour = colour
        self.eaten = False

    # def eat(self) -> None:
    #     print("nom nom nom!!")
    #     self.amount -= 1
    def __str__(self):
        return str(self)

    def getPos(self):
        return (self.xpos, self.ypos)
    
    # def getAmount(self):
    #     return self.amount
    
    def getSize(self):
        return self.size
    
    def stepChange(self):
        super().tick()
        xmov = random.choice([20,-20])
        ymov = 20
        self.xpos += xmov
        self.ypos -= ymov