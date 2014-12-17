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
        if player.stats['sword'] == False:
            print text.sword_room['intro']
            player.stats['sword'] = True
            player.stats['dmg'] += 5
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
            roll = randint(1, 20) + player.stats['agility']

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

    goblin_stats = {
    'dmg' : 3,
    'health' : 5,
    'initiative' : 70,
    'accuracy' : 70,
    'alive' : True
    }

    def __init__(self):
        self.coord = (1, 1)
        self.goblin = fn.Character('Grexlyx the goblin', self.goblin_stats)
        self.first_time = True

    def enter(self, previous_room):
        if self.goblin.stats['alive'] and self.first_time == True:
            print text.goblin_room['intro_alive']
            self.first_time = False
            return self.choose_action(previous_room)
        elif self.goblin.stats['alive'] and self.first_time == False:
            print text.goblin_room['returning_alive']
            return self.choose_action(previous_room)
        else:
            print text.goblin_room['returning_dead']
            return self.exit()

    def choose_action(self, previous_room):

        if (self.goblin.stats['alive'] == True and
            player.stats['alive'] == True):
            choice_ls = ['Fight!', 'Run away!']
            menu = fn.Menu()
            choice = menu.generate(choice_ls, 'What do you do?')

            if choice == '1':
                combat = fn.Combat(player, self.goblin, self.choose_action,
                previous_room)
                return combat.rounds()
            elif choice == '2':
                return previous_room
            else:
                return self.choose_action(previous_room)
        elif player.stats['alive'] == False:
            print text.goblin_room['death_by_goblin']
            return (-1, -1)
        else:
            print "The goblin is dead!"
            print ""
            return self.exit()

    def exit(self):
        exit_menu = ["North Door", "East Door", "South Door", "West Door"]
        return super(GoblinRoom, self).exit(self.coord, exit_menu,
         GoblinRoom)


class CodeRoom(Room):

    def __init__(self):
        self.coord = (1, 2)
        self.code_tuple = (str(randint(0, 1)), str(randint(0, 1)),
         str(randint(0, 1)), str(randint(0, 1)), str(randint(0, 1)))
        self.code = ''.join(self.code_tuple)
        self.code_cracked = False
        self.first_time = True

    def enter(self, previous_room):
        if self.first_time == True:
            print text.code_room['first_intro']
            self.first_time = False
            return self.choose_action()
        elif self.code_cracked == False:
            print text.code_room['intro_returning']
            return self.choose_action()
        else:
            print text.code_room['returning_cracked']
            return self.exit()

    def choose_action(self):
        action_ls = ["Fiddle with the levers.", "Exit Room."]
        menu = fn.Menu()
        choice = menu.generate(action_ls, "What do you do?")
        ### CHEAT ###
        print "### CHEAT ###"
        print self.code
        ###

        if choice == '1':
            print text.code_room['explain_mechanism']
            print "How do you configure them? (ex: 10101)"
            code = raw_input('> ')

            if code == self.code:
                print text.code_room['cracking_code']
                self.code_cracked = True
                return self.exit()
            else:
                print "This code doesn't seem to do anything."
                return self.choose_action()

        elif choice == '2':
            return self.exit()
        else:
            return self.choose_action()

    def exit(self):
        exit_menu = ["North Door", "East Door", "South Door", "West Door"]
        return super(CodeRoom, self).exit(self.coord, exit_menu,
         CodeRoom)

class SpiderRoom(Room):

    spider_stats = {
    'dmg' : 2,
    'health' : 10,
    'initiative' : 100,
    'accuracy' : 70,
    'alive' : True
    }

    def __init__(self):
        self.coord = (1, 3)
        self.spider = fn.Character('Shelob the spider', self.spider_stats)
        self.first_time = True

    def enter(self, previous_room):
        if self.spider.stats['alive'] and self.first_time == True:
            print text.spider_room['intro_alive']
            self.first_time = False
            return self.choose_action(previous_room)
        elif self.spider.stats['alive'] and self.first_time == False:
            print text.spider_room['returning_alive']
            return self.choose_action(previous_room)
        else:
            print text.spider_room['returning_dead']
            return self.exit()

    def choose_action(self, previous_room):

        if (self.spider.stats['alive'] == True and
            player.stats['alive'] == True):
            choice_ls = ['Fight!', 'Run away!']
            menu = fn.Menu()
            choice = menu.generate(choice_ls, 'What do you do?')

            if choice == '1':
                combat = fn.Combat(player, self.spider, self.choose_action,
                previous_room)
                return combat.rounds()
            elif choice == '2':
                return previous_room
            else:
                return self.choose_action(previous_room)
        elif player.stats['alive'] == False:
            print text.spider_room['death_by_spider']
            return (-1, -1)
        else:
            print text.spider_room['killing_spider']
            return self.exit()

    def exit(self):
        exit_menu = ["North Door", "East Door", "South Door", "West Door"]
        return super(SpiderRoom, self).exit(self.coord, exit_menu,
         SpiderRoom)

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
                player.stats['health'] = player.stats['maxHealth']
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

        if (self.zombie.stats['alive'] == True and
            player.stats['alive'] == True):
            choice_ls = ['Fight!', 'Run away!']
            menu = fn.Menu()
            choice = menu.generate(choice_ls, 'What do you do?')

            if choice == '1':
                combat = fn.Combat(player, self.zombie, self.choose_action,
                previous_room)
                return combat.rounds()
            elif choice == '2':
                return previous_room
            else:
                return self.choose_action(previous_room)
        elif player.stats['alive'] == False:
            print text.zombie_room['death_by_zombie']
            return (-1, -1)
        else:
            print "The zombie is dead!"
            print ""
            return self.exit()

    def exit(self):
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

  #  def opening_room(self):
   #     return self.next_room(self.starting_room)


print "Hey, there, adveturer!"
print "What's your name?"
player_name = raw_input('> ')

stats = {
    'dmg' : 1,
    'str' : 3,
    'initiative' : 50,
    'health' : 20,
    'maxHealth' : 120,
    'has_key' : False,
    'agility' : randint (-3, 3),
    'sword' : False,
    'name' : 'Player',
    'alive' : True,
    'accuracy' : 50,
    'has_diamond' : False
}
player = fn.Character(player_name, stats)

a_map = Map((2, 2))
eng = fn.Engine(a_map)
eng.play()
