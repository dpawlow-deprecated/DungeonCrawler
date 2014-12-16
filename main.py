from sys import exit
from random import randint

import functions as fn
import text

class Engine(object):
    """Runs the game by handing the next room to the player"""

    def __init__(self, room_map):
        self.room_map = room_map

    def play(self):
        current_room = self.room_map.starting_room
        exit_room = self.room_map.rooms[(0, 4)]

        while current_room != exit_room or hero.has_key == False:
            next_room_coord = current_room.enter()
            current_room = self.room_map.next_room(next_room_coord)
        

class Room(object):
    """Template for rooms. Contains exit() for rooms with four doors"""

    def exit(self, coord, menu_ls, room):
        menu = fn.Menu()
        choice = menu.generate(menu_ls, "Which door do you take?")

        if choice == '1':
            return (coord[0], coord[1] + 1)
        elif choice == '2':
            return (coord[0] + 1, coord[1])
        elif choice == '3':
            return (coord[0], coord[1] - 1)
        elif choice == '4':
            return (coord[0] - 1, coord[1])
        else:
            print "Try again."
            instance = room()
            return instance.exit()


class StartingRoom(Room):

    def __init__(self):
        self.coord = (2, 2)
        self.first_time = True

    def enter(self):
        if self.first_time == True:
            self.first_time = False
            print text.starting_room['intro_first_time']
            return self.exit()
        else:
            print text.starting_room['intro_returning']
            return self.exit()

    def exit(self):
        menu_ls = ["North Door", "East Door", "South Door", "West Door"]
        return super(StartingRoom, self).exit(self.coord, menu_ls,
         StartingRoom)


class KeyRoom(Room):
    
    def __init__(self):
        self.coord = (0, 0)


class ExitRoom(Room):
    pass

class SwordRoom(Room):

    def __init__(self):
        self.coord = (3, 2)

class HunterRoom(Room):

    def __init__(self):
        self.coord = (3, 1)

class BladesRoom(Room):

    def __init__(self):
        self.coord = (2, 1)

    def enter(self):
        print text.blades_room['intro']
        print "run away"
        return self.prev_coord


class GoblinRoom(Room):

    def __init__(self):
        self.coord = (1, 1)

class CodeRoom(Room):

    def __init__(self):
        self.coord = (1, 2)

class SpiderRoom(Room):

    def __init__(self):
        self.coord = (1, 3)

class HealthRoom(Room):
    """Has a one-use-only health potion."""

    def __init__(self):
        self.coord = (2, 3)
        self.bottle_full = True

    def enter(self):
        if self.bottle_full == True:
            print text.health_room['intro_bottle_full']
            enter_menu = ["Drink from the bottle.", "Exit the room."]
            menu = fn.Menu()
            choice = menu.generate(enter_menu, "What do you do?")

            if choice == '1':
                hero.stats['Health'] = hero.stats['MaxHealth']
                print text.health_room['drink_potion']
                self.bottle_full = False 
                return self.exit()           
            else:
                return self.exit()

        else:
            print text.health_room['intro_bottle_empty']
            return self.exit()

    def exit(self):
        menu_ls = ["North Door", "East Door", "South Door", "West Door"]
        return super(HealthRoom, self).exit(self.coord, menu_ls,
         HealthRoom)

class ZombieRoom(Room):

    def __init__(self):
        self.coord = (3, 3)


class RiddleRoom(Room):
    pass

class Map(object):

    rooms = {
        (0, 0) : KeyRoom(),
        (0, 4) : ExitRoom(),
        (1, 1) : GoblinRoom(),
        (1, 2) : CodeRoom(),
        (1, 3) : SpiderRoom(),
        (2, 1) : BladesRoom(),
        (2, 2) : StartingRoom(),
        (2, 3) : HealthRoom(),
        (3, 1) : HunterRoom(),
        (3, 2) : SwordRoom(),
        (3, 3) : ZombieRoom(),
    }

    def __init__(self, starting_room):
        self.starting_room = Map.rooms.get(starting_room)

    def next_room(self, room_coord):
        val = Map.rooms.get(room_coord)
        return val

#    def previous_room(self, next_coord, prev_coord):


    def opening_room(self):
        return self.next_room(self.starting_room)





stats = {
    'str' : 3,
    'Health' : 14,
    'MaxHealth' : 120,
    'has_key' : False
}
hero = fn.Character('pepe', stats)

a_map = Map((2, 2))
eng = Engine(a_map)
eng.play()
