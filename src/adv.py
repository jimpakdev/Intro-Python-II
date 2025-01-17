from player import Player
from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


player_one = Player("Player 1", room["outside"])
print(player_one)

running = True

def handleInput( user_input ):
    lower_input = user_input.lower()
    
try: 
    if lower_input == "n" and hasattr( player_one.current_room, 'n_to' ) :
        player_one.current_room = player_one.current_room.n_to
    # elif lower_input == "s" and hasattr( player_one.current_room, 's_to' ) :
    #     player_one.current_room = player_one.current_room.s_to
    # elif lower_input == "e" and hasattr( player_one.current_room, 'e_to' ) :
    #     player_one.current_room = player_one.current_room.e_to
    # elif lower_input == "w" and hasattr( player_one.current_room, 'w_to') :
    #     player_one.current_room = player_one.current_room.w_to
    # elif lower_input == "q" : 
    #     break
# else: 
#     print("Enter `n`, `s`, `e, `w` to travel in a direction.  Enter `q` to exit game")



    #when lower_input == 'q' -> run the quit function, running = false
    #check entry
    #check room exists

while running:
    print( f" My Current Room: {player_one.current_room}" )
    make_move = input("Enter a direction: ")
    handleInput( make_move )


