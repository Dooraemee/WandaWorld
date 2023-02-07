from WandaCrab import Crab
from WandaFish import Fish
from WandaFood import Food
import matplotlib.pyplot as plt


class Aquarium:
    def __init__(self) -> None:
        self.fishies: list[Fish] = []
        self.fish_food: list[Food] = []

    def add_food(self, food: list[Food]):
        self.fish_food += food

    def add_fish(self, fish: list[Fish]):
        self.fish += fish

    def render(self):
        for i in self.fishies:
            p = i.get_point()
            plt.scatter(p[0], p[1], s = p[2], color=p[3], marker="o") 

