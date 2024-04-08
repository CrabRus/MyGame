class Node:
    def __init__(self, number, edges=[], availability = False):
        self.number = number
        self.edges = edges
        self.availability = False

r_Hall = Node(1,[2], False)
scene = Node(2,[1,3], True)
l_Hall = Node(3,[2], False)

class Animatronic:
    def __init__(self, number = 1, location = 2):
        self.number = number
        self.location = location
    def move(self):

