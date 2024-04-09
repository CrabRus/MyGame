import time
import random

class Node:
    def __init__(self, name, number, edges=[], availability = False):
        self.name = name
        self.number = number
        self.edges = edges
        self.availability = False

r_Hall = Node("Правый холл",1,[2], False)
scene = Node("Сцена",2,[1,3], True)
l_Hall = Node("Левый холл",3,[2], False)

rooms = [r_Hall, scene, l_Hall]

class Animatronic:
    def __init__(self, name="", number = 1, pre_location = 0, real_location = 2, next_location = 0):
        self.name = name
        self.number = number
        self.real_location = real_location
    def move(self):
        for i in rooms:
            if i.number == self.real_location:
                self.real_location = random.choice(i.edges)
                print(f"{self.name} перешел на {self.real_location}")
                break

freddy = Animatronic("Отбитый на голову Фредди")

for i in range(5):
    freddy.move()



