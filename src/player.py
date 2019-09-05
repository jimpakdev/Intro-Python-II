# Write a class to hold player information, e.g. what room they are in
# currently.
from items import Item

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
    
    def __str__(self):
        return f"Player: {self.name}, Current Room: {self.current_room}"

    def add_inventory(self, item):
        self.inventory.append(item)

    def remove_inventory(self, item):
        self.inventory.remove(item)

    def display_inventory(self):
        for i in self.inventory:
            print(i)
