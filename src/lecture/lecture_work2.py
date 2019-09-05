class TodoList:
    def __init__(self, name):
        self.name = name
        self.items = []

    def __str__(self):
        return f"{self.name}: {self.items}"

    def __repr__(self):
        return f"TodoList({repr(self.name)})"

quit = False

all_lists = []

current_list = None

while not quit:
    command = input("(C)reate new list\n(S)elect a list\n(A)dd item\n(Q)uit\nCommand: ")

    command = command.lower().strip()

    if command == '':
        continue

    if command == 'q':
        quit = True

    elif command == 'c':
        name = input("Enter list name: ").strip()

        new_list = TodoList(name)
        all_lists.append(new_list)

        print(all_lists)

    elif command == 's':
        name = input("Enter list name: ").strip()

        named_list = None

        for l in all_lists:
            if l.name == name:
                named_list = l
                break
        
        if named_list is None:
            print(f"No such list named {name}")

        else:
            current_list = named_list

    elif command == 'a':
        item_name = input("Enter item: ").strip()

        current_list.items.append(item_name)

# tl = TodoList("list 1")

# tl.items.append("Get milk")
# tl.items.append("Go mountain biking")
# print(tl)
