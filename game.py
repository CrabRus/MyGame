import time
import random
from tkinter import *
from tkinter import ttk
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
office = Office("Офис охранника",4, [], False, False, False)
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
            elif final_choice == False:
                print("Отбитый на голову Фредди решил вернуться на сцену")
        if self.real_location == 6:
            time.sleep(random.choice([10]))
            final_choice = random.choice([True, False])
            if final_choice == True:
                if office.r_door == False:
                    print("Отбитый на голову Фредди вошел в офис офранника с правой двери")
                else:
                    self.real_location = 2
                    print("Отбитый на голову Фредди вернулся на сцену")
            elif final_choice == False:
                print("Отбитый на голову Фредди решил вернуться на сцену")


freddy = Animatronic("Отбитый на голову Фредди",1, 0, 2, [[1,5],[3,6]])

animatronics = [freddy]
def start_game(animatronics, rooms, office):
    window = Tk()
    window.geometry('450x400+400+200')
    window.title('FNAF')

    l_btn_text = StringVar(value="OFF")
    r_btn_text = StringVar(value="OFF")
    def l_lockdoor():
        if office.l_door == False:
            l_btn_text.set("ON")
            office.l_door = True
        elif office.r_door == False:
            l_btn_text.set("OFF")
            office.l_door = False

    def r_lockdoor():
        if office.r_door == False:
            r_btn_text.set("ON")
            office.r_door = True
        else:
            r_btn_text.set("OFF")
            office.r_door = False

    l_button = Button(textvariable=l_btn_text, height=3, width=10, command=l_lockdoor).place(x=100,y=0)
    r_button = Button(textvariable=r_btn_text, height=3, width=10, command=r_lockdoor).place(x=200,y=0)
    window.mainloop()

start_game(animatronics, rooms, office)
freddy.move_trajectory()