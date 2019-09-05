# Implement a class to hold room information. This should have name and
from items import Item

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def __str__(self):
        return f"Room: {self.name}, Description: {self.description}"

    def add_item(self, item): 
        self.items.append(item)
    
    def remove_item(self, item):
        self.items.remove(item)

    def display_items(self):
        if len(self.items) == 0:
            print("No items in the room")
            return
        for i in self.items:
            print(i.name)
