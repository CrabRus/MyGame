import time
import random

class Node:
    def __init__(self, name, number, edges=[], availability = False):
        self.name = name
        self.number = number
        self.edges = edges
        self.availability = False

r_Hall = Node("Правый холл",1,[2,5], False)
scene = Node("Сцена",2,[1,3], True)
l_Hall = Node("Левый холл",3,[2,6], False)
office = Node("Офис охранника",4, [], False)
r_pocket = Node("Правый кармашек", 5, [1], False)
l_pocket = Node("Левый кармашек", 6, [3], False)

rooms = [r_Hall, scene, l_Hall, r_pocket, l_pocket]

class Animatronic:
    def __init__(self, name="", number = 1, pre_location = 0, real_location = 2):
        self.name = name
        self.number = number
        self.pre_location = pre_location
        self.real_location = real_location
    def move(self):
        for i in rooms:
            if i.number == self.real_location:
                self.pre_location = self.real_location
                self.real_location = random.choice(i.edges)
                next_location = ""
                for y in rooms:
                    if y.number == self.real_location:
                        next_location = y.name
                print(f"{self.name} перешел в: {next_location}")
                break

freddy = Animatronic("Отбитый на голову Фредди",1, 0, 2)

animatronics = [freddy]
for i in range(10):
    freddy.move()
    time.sleep(1)

#def start_game(animatronics, rooms):



