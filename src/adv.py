from room import Room
from player import Player
import time

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

player = Player(name="", currentRoom=room['outside'])

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

print('Welcome to The Adventure!')

# Get the player name
time.sleep(1)
name = input('What is your name Traveler? ')
player.name = name

# Start 
print(f"Hello {player.name}! Let's go on an adventure!")
time.sleep(1)
begin = input('Shall we begin? Y/N ')
if begin == 'Y' or begin == 'y':

    print('Lets begin!')
    time.sleep(1)
    print(f"You are currently {player.currentRoom.name}")
    time.sleep(.5)

    while True:
        
        print("Where should we go next?")
        time.sleep(.5)
        options = player.currentRoom.options()
        directionOptions = ""
        if options[0] != None:
            directionOptions += f"[N] North: {options[0]} \n"
        if options[1] != None:
            directionOptions += f"[E] East: {options[1]} \n"
        if options[2] != None:
            directionOptions += f"[S] South: {options[2]} \n"
        if options[3] != None:
            directionOptions += f"[W] West: {options[3]} \n"
            
        direction = input(directionOptions);
        if direction == 'N' or direction == 'n':
            player.currentRoom = options[0]
        elif direction == 'E' or direction == 'e':
            player.currentRoom = options[1]
        elif direction == 'S' or direction == 's':
            player.currentRoom = options[2]
        elif direction == 'W' or direction == 'w':
            player.currentRoom = options[3]
        elif direction == 'Q' or direction == 'q':
            break

        time.sleep(.5)
        print(f"Fantastic! Now we're here: {player.currentRoom.name}")
        time.sleep(.5)

    time.sleep(.5)
    print('See you next time!')
                
else:
    print('Next time then!')