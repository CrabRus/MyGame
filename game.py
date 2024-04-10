import time
import random

class Room:
    def __init__(self, name, number, edges=[], availability = False):
        self.name = name
        self.number = number
        self.edges = edges
        self.availability = False

class Office(Room):
    def __init__(self,name, number, edges=[], availability = False, r_door = False, l_door = False):
        self.r_door = r_door
        self.l_door = l_door


l_Hall = Room("Левый холл",1,[2,5], False)
scene = Room("Сцена",2,[1,3], True)
r_Hall = Room("Правый холл",3,[2,6], False)
office = Office("Офис охранника",4, [], False, True, False)
l_pocket = Room("Левый кармашек", 5, [1], False)
r_pocket = Room("Правый кармашек", 6, [3], False)

rooms = [r_Hall, scene, l_Hall, r_pocket, l_pocket]

class Animatronic:
    def __init__(self, name="", number = 1, pre_location = 0, real_location = 2, trajectory = []):
        self.name = name
        self.number = number
        self.pre_location = pre_location
        self.real_location = real_location
        self.trajectory = trajectory
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



    def move_trajectory(self):
        real_trajectory = random.choice(self.trajectory)
        for i in rooms:
            if i.number == self.real_location:
                for y in real_trajectory:
                    self.real_location = y
                    for z in rooms:
                        if z.number == self.real_location:
                            next_location = z.name
                    print(f"{self.name} перешел в: {next_location}")
                    self.attack_office()
                    time.sleep(3)
                break

    def attack_office(self):
        if self.real_location == 5:
            time.sleep(random.choice([7, 8, 9, 10]))
            final_choice = random.choice([True, False])
            if final_choice == True:
                if office.l_door == False:
                    print("Отбитый на голову Фредди вошел в офис офранника с левой двери")
                else:
                    self.real_location = 2
                    print("Отбитый на голову Фредди вернулся на сцену")

        if self.real_location == 6:
            time.sleep(random.choice([10]))
            final_choice = random.choice([True, False])
            if final_choice == True:
                if office.r_door == False:
                    print("Отбитый на голову Фредди вошел в офис офранника с правой двери")
                else:
                    self.real_location = 2
                    print("Отбитый на голову Фредди вернулся на сцену")



freddy = Animatronic("Отбитый на голову Фредди",1, 0, 2, [[1,5],[3,6]])

animatronics = [freddy]
# for i in range(10):
#     freddy.move()
#     time.sleep(1)

# def start_game(animatronics, rooms):
#




freddy.move_trajectory()