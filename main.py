from sys import exit
from random import randint

import functions as fn
import text


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

class Death(Room):

    def enter(self, previous_room):
        print "You died."
        exit(1)

class StartingRoom(Room):

    def __init__(self):
        self.coord = (2, 2)
        self.first_time = True

    def enter(self, prev):
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

    def enter(self, previous_room):
        if hero.stats['sword'] == False:
            print text.sword_room['intro']
            hero.stats['sword'] = True
            hero.stats['dmg'] += 5
            return self.exit()
        else:
            print text.sword_room['intro_returning']
            return self.exit()

    def exit(self):
        exit_menu = ["North Door", "East Door", "South Door", "West Door"]
        return super(SwordRoom, self).exit(self.coord, exit_menu,
         SwordRoom)


class HunterRoom(Room):

    def __init__(self):
        self.coord = (3, 1)

class BladesRoom(Room):

    def __init__(self):
        self.coord = (2, 1)

    def enter(self, previous_room):
        print text.blades_room['intro']
        enter_menu = ["Try to scurry through the blades.", "Run away!"]
        menu = fn.Menu()
        choice = menu.generate(enter_menu, "What do you do?")

        if choice == '1':
            roll = randint(1, 20) + hero.stats['agility']

            if roll < 14:
                print text.blades_room['death']
                return (-1, -1)
            else:
                print text.blades_room['pass_through']
                return self.exit()
        
        elif choice == '2':
            return previous_room
        else:
            self.enter(previous_room)

    def exit(self):
        exit_menu = ["North Door", "East Door", "South Door", "West Door"]
        return super(BladesRoom, self).exit(self.coord, exit_menu,
         BladesRoom)

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

    def enter(self, prev):
        if self.bottle_full == True:
            print text.health_room['intro_bottle_full']
            enter_menu = ["Drink from the bottle.", "Exit the room."]
            menu = fn.Menu()
            choice = menu.generate(enter_menu, "What do you do?")

            if choice == '1':
                hero.stats['health'] = hero.stats['maxHealth']
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

    zombie_stats = {
    'dmg' : 1,
    'health' : 14,
    'initiative' : 20,
    'accuracy' : 20,
    'alive' : True
    }

    def __init__(self):
        self.coord = (3, 3)
        self.zombie = fn.Character('Bob the Zombie', self.zombie_stats)
        self.first_time = True

    def enter(self, previous_room):
        if self.zombie.stats['alive'] and self.first_time == True:
            print text.zombie_room['intro_alive']
            self.first_time = False
            return self.choose_action(previous_room)
        elif self.zombie.stats['alive'] and self.first_time == False:
            print text.zombie_room['returning_alive']
            return self.choose_action(previous_room)
        else:
            print text.zombie_room['returning_dead']
            return self.exit()

    def choose_action(self, previous_room):
        choice_ls = ['Fight!', 'Run away!']
        menu = fn.Menu()
        choice = menu.generate(choice_ls, 'What do you do?')

        if choice == '1':
            combat = fn.Combat(hero, self.zombie, self.choose_action,
             previous_room)
            combat.rounds()
        elif choice == '2':
            return previous_room
        else:
            return self.choose_action(previous_room)

    def exit():
        exit_menu = ["North Door", "East Door", "South Door", "West Door"]
        return super(ZombieRoom, self).exit(self.coord, exit_menu,
         ZombieRoom)






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
        (-1, -1) : Death()
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
    'dmg' : 1,
    'str' : 3,
    'initiative' : 50,
    'health' : 14,
    'maxHealth' : 120,
    'has_key' : False,
    'agility' : randint (-3, 3),
    'sword' : False,
    'name' : 'Player',
    'alive' : True,
    'accuracy' : 50
}
hero = fn.Character('pepe', stats)

a_map = Map((2, 2))
eng = fn.Engine(a_map)
eng.play()
