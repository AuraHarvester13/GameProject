def main():
    # map 
    rooms = {
        'foyer': {
            'west': 'parlor',
            'north': 'basement'},
        'parlor': {
            'east': 'foyer',
            'north': 'kitchen',
            'item': 'locket'},
        'kitchen': {
            'north': 'grand hall',
            'south': 'parlor',
            'item': 'bone'},
        'grand hall': {
           'east': 'upstairs hall',
           'south': 'kitchen',
           'item': 'bone'},
        'upstairs hall': {
            'west': 'grand hall',
            'east': 'attic',
            'item': 'bone'},
        "attic": {
            'west': 'upstairs hall',
            'south': 'conservatory',
            'item': 'bone'},
        'conservatory':{
            'west': 'basement',
            'north': 'attic',
            'item': 'bone'},
        'basement':{
            'east': 'conservatory',
            'south': 'foyer',
            'villain': 'dark entity'}
    }

    # player gameplay instructions
    print("Whispering Walls")
    print("You must collect all 6 items before the dark entity gets to you.")
    print("------------------------------------------------------------")
    print("Move Commands: 'go {direction}' (direction: north, south, east, west or exit)")
    print("------------------------------------------------------------")
    print("Action Command: 'get item' (adds nearby item to inventory)")
    print("---------------------------------------------------")

    game(rooms)


def game(rooms):
    # start
    current_room = 'foyer'
    inventory = []

    # game play loop
    while True:

        # status update
        print(f"You are in the {current_room}\nInventory: {inventory}")
        print("---------------------------------------------------")
        user_input = input("\nWhat do you want to do?\n")

        # exit game     
        if user_input.lower() == 'exit':
            current_room = 'exit'
            print("Thanks for playing")
            break

        
        command = user_input.lower().split()

        # invalid input    
        if len(command) != 2:
            print("Go where? Do what?")

        # valid input
        if len(command) == 2:
            if command[0] == 'go':
                direction = command[1]
                if direction in rooms[current_room]:
                    current_room = rooms[current_room][direction]

                    # get villain, end gameplay 
                    if current_room == 'basement':
                        boss = rooms[current_room].get('villain')
                        #lose
                        if len(inventory) < 6:
                            current_room == 'exit'
                            print(f"You have been possessed")
                            break
                        # win
                        else:
                            current_room == 'exit'
                            print(f"You beat the Dark Entity and freed the trapped souls!")
                            break
                #get index
                    if rooms[current_room].get('item', '') != "":
                        get_item = input(f'There is an item in here\n')
                        print("---------------------------------------------------")
                        command = get_item.lower().split()
                        if command[0] == 'get':
                            item = command[1]
                            if item in rooms[current_room]:
                                item_part = rooms[current_room][item] 
                                print(f'You found a {item_part}!\n')

                                inventory.append(item_part)
                                del rooms[current_room][item] 
                    else:
                        print(f'There is no item')
                        continue

            # wrong direction input 
            else:
                print("You can't go that way")

main()




    
    
 