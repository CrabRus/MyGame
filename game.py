import time
import random
import tkinter
from tkinter import *
from tkinter import ttk
import threading
class Room:
    def __init__(self, name, number, edges=[], availability = False):
        self.name = name
        self.number = number
        self.edges = edges
        self.availability = availability

class Office(Room):
    def __init__(self,name, number, edges=[], availability = False, r_door = False, l_door = False, energy_count = 100.0, use_energy = 0):
        self.r_door = r_door
        self.l_door = l_door
        self.energy_count = energy_count
        self.use_energy = use_energy

l_Hall = Room("Левый холл",1,[2,5], False)
scene = Room("Сцена",2,[1,3,4], True)
r_Hall = Room("Правый холл",3,[2,6], False)
office = Office("Офис охранника",4, [], False, False, False)
l_pocket = Room("Левый кармашек", 5, [1], False)
r_pocket = Room("Правый кармашек", 6, [3], False)

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
        while True:
            real_trajectory = random.choice(self.trajectory)
            for i in rooms:
                if i.number == self.real_location:
                    for y in real_trajectory:
                        self.real_location = y
                        for z in rooms:
                            if z.number == self.real_location:
                                next_location = z.name
                        print(f"{self.name} перешел в: {next_location}")

                        w_l = self.attack_office()
                        if w_l == True:
                            print(w_l)
                            break
                        time.sleep()
            break

    def attack_office(self):
        if self.real_location == 5:
            time.sleep(random.choice([7, 8, 9, 10]))
            final_choice = random.choice([True, False])
            if final_choice == True:
                if office.l_door == False:
                    print("Отбитый на голову Фредди вошел в офис офранника с левой двери")
                    return True
                else:
                    self.real_location = 2
                    print("Отбитый на голову Фредди вернулся на сцену")
                    return False
            elif final_choice == False:
                self.real_location = 2
                print("Отбитый на голову Фредди решил вернуться на сцену")
                return False
        if self.real_location == 6:
            time.sleep(random.choice([7, 8, 9, 10]))
            final_choice = random.choice([True, False])
            if final_choice == True:
                if office.r_door == False:
                    print("Отбитый на голову Фредди вошел в офис офранника с правой двери")
                    return True
                else:
                    self.real_location = 2
                    print("Отбитый на голову Фредди вернулся на сцену")
                    return False
            elif final_choice == False:
                self.real_location = 2
                print("Отбитый на голову Фредди решил вернуться на сцену")
                return False

# def move_animatronics(animatronics):
#     for i in animatronics:

def start_game(animatronics, rooms, office):

    def update_energy():
        while True:
            if office.energy_count >0:
                office.energy_count = office.energy_count - 0.1 - (office.use_energy*0.7)
                energy_label_text.set(f"Энергия: {office.energy_count.__round__(1)}%")
                print(office.energy_count.__round__(1))
                time.sleep(1)

    def l_lockdoor():
        if office.l_door == False:
            l_btn_text.set("ON")
            office.use_energy += 1
            office.l_door = True
        elif office.l_door == True:
            l_btn_text.set("OFF")
            office.use_energy -= 1
            office.l_door = False

    def r_lockdoor():
        if office.r_door == False:
            r_btn_text.set("ON")
            office.use_energy += 1
            office.r_door = True
        elif office.r_door == True:
            r_btn_text.set("OFF")
            office.use_energy -= 1
            office.r_door = False


    window = Tk()
    window.geometry('400x400+400+200')
    window.title('FNAF')

    l_btn_text = StringVar(value="OFF")
    r_btn_text = StringVar(value="OFF")
    energy_label_text = StringVar(value=f"Энергия: {office.energy_count.__round__(1)}%")

    label_l_door = Label(text="Левая дверь").pack()
    l_button = Button(textvariable=l_btn_text, height=3, width=10, command=l_lockdoor).pack()
    label_r_door=Label(text="Правая дверь").pack()
    r_button = Button(textvariable=r_btn_text, height=3, width=10, command=r_lockdoor).pack()
    energy_label = Label(textvariable=energy_label_text).pack()

    threadMove = threading.Thread(target=freddy.move_trajectory)
    threadUpdateEnergy = threading.Thread(target=update_energy)
    threadMove.start()
    threadUpdateEnergy.start()
    window.mainloop()



rooms = [r_Hall, scene, l_Hall, r_pocket, l_pocket]
freddy = Animatronic("Отбитый на голову Фредди",1, 0, 2, [[1,5],[3,6]])
animatronics = [freddy]


start_game(animatronics, rooms, office)