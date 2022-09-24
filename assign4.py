# TODO: From a text file read in the text
# introduction of your game and print it to the console.
request = ""
f = open("assign4data.txt", "r")
print(f.read())
# TODO: Setup a dictionary with several key
# value pairs. It should contain an inventory list
# and the initial location. Call the dictionary `player`.
player = {
    'inventory_list': ["courage", "holy water"],
    'initial_location': ["foyer"]
    }
# TODO: Set up a dictionary of rooms each room having a description,
# a list of items and a dictionary of exits. Add 5 rooms.
rooms = {
    'parlor': {'description': ["Come have a chat in the parlor"], 'item_list': ["notpad", "drink"], 'exits': ["foyer", "kitchen"]},
    'kitchen': {'description': ["Be out guest!"], 'item_list': ["knife", "pot"], 'exits': ["parlor", "library", "pantry"]},
    'foyer': {'description': ["Welcome to the foyer!"], 'item_list': ["candle", "pen"], 'exits': ["parlor", "library"]},
    'library': {'description': ["Read your favorite books, but beware! Things might get spooky!"], 'item_list': ["book", "bookmark"], 'exits': ["kitchen", "foyer"]},
    'pantry': {'description': ["Find all the snacks you need here!"], 'item_list': ["oreos", "chips"], 'exits': ["kitchen"]}
}
# TODO: Create a variable and set it equal to the initial room stored
# in the `player` dictionary.
current_room = "foyer"

# TODO: Setup on infinite loop.
while request != 'quit':
    # TODO: Create a variable to store the command that is input by the user.
    # Allow for commands like `take sword`
    # **Hint: `split()` and store the different parts in their own variables.**
    g_i = open("game_instructions.txt", "r")
    request = input(g_i.read())
    split = request.split()
    # request = request.split()
    # TODO: Create four `if` statements
    # TODO: One that checks verbs and exits.
    if split[0] == "enter":
        if split[1] in rooms:
            # Make sure you check if the player can go in
            # the direction that the have asked for.
            if split[1] in rooms[current_room]['exits']:
                current_room = split[1]
                # This is where you list all of the items in the room.
                print("You are now in the", current_room)
                print("The items in this room are ", rooms[current_room]["item_list"])

                # TODO: In one room have the player talk with
                # another character save the dialog.
                if current_room == "kitchen":
                    file = open("butler_conversation.txt", "w")
                    file.writelines(["Butler: Welcome! I am your butler. What would you like to eat? "])
                    food = input("Welcome! I am your butler. What would you like to eat? ")
                    file.writelines(["\nMe: ", food])
                    while food != "no":
                        food = input("Yummy! Anything else? (type a food or 'no' to end) ")
                        file.writelines(["\nButler: Yummy! Anything else?"])
                        file.writelines(["\nMe: ", food])
                    file.close()
                # TODO: In one room add a monster and have the player
                # fight the monster (add an attack verb).
                # Store the monster stats in a dictionary.
                ghost = {
                    'hypnotized': False,
                    'scared': False
                }
                if current_room == "library":
                    while ghost['hypnotized'] is False and ghost['scared'] is False:
                        print("""I am the Ghost who haunts this library! You dare to enter!?
                                \n To scare the ghost away you must hypnotize
                                him and splash the holy water on him""")
                        move = input("Whats your move? (hypnotize or holy water? ")
                        move_split = move.split()
                        if move_split[0] == "hypnotize":
                            ghost['hypnotized'] = True
                            print("Great! You have hypnotized the Ghost!")
                            if ghost['hypnotized'] is True and ghost['scared'] is True:
                                print("You scared the ghost away!")
                            else:
                                move = input("Whats your move? (hypnotize or holy water? ")

                        elif move_split[0] == "holy":
                            ghost['scared'] = True
                            print("You sprayed him with holy water!")
                            if ghost['hypnotized'] is True and ghost['scared'] is True:
                                print("You scared the ghost away!")
                            else:
                                move = input("Whats your move? (hypnotize or holy water? ")
                        else:
                            move = input("That didn't work! Whats your move? (hypnotize or holy water?")
                    print("You scared the ghost away!")
            else:
                print("You can't get there from here")

    elif request == "map":
        # Create a map verb that prints a map of the dungeon.
        print("""
            ----------------------------------
            |             Foyer              |
            |                                |
            -----   --------------   ---------
            |  Parlor      |     Library     |
            |              |        w/ghost  |
            ----   -----------------   -------
            |            Kitchen             |
            |                                |
            -----  --------------------------
            |  Pantry      |
            |    w/monster |
            ----------------
        """)
    # TODO: Prints items in the room
    elif request == "items":
        print(rooms[current_room]['item_list'])
    # TODO: Prints Butlers conversation
    elif request == "conversation":
        b_c = open("butler_conversation.txt", "r")
        print(b_c.read())
        b_c.close()
    # TODO: One that allows the user to print the current inventory
    elif request == "inventory":
        print(player["inventory_list"])
    # TODO: One that allows the user to quit.
    elif request == "quit":
        break
    # Also allow the user to add all items in the room to the inventory.
    elif split[1] == "all":
        player["inventory_list"].extend(rooms[current_room]["item_list"])
        rooms[current_room]["item_list"].clear()
    # TODO: One that allows the player to pick up single
    # items and odd them to the inventory of the `player`.
    else:
        if split[1] == rooms[current_room]['item_list'][0]:
            new_item = rooms[current_room]["item_list"][0]
            player["inventory_list"].append(new_item)
            del rooms[current_room]["item_list"][0]
        elif split[1] == rooms[current_room]['item_list'][1]:
            new_item = rooms[current_room]["item_list"][1]
            player["inventory_list"].append(new_item)
            del rooms[current_room]["item_list"][1]
        else:
            print("That item isnt in this room")
