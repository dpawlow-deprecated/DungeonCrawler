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
        if player.stats['hamster_found'] == True:
            print "%s is sad." % player.stats['hamster_name']
        else:
            pass
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

    def enter(self, previous_room):
        if player.stats['has_key'] == False:
            print text.key_room['intro']
            player.stats['has_key'] = True
            return self.exit()
        else:
            print text.key_room['intro_returning']
            return self.exit()

    def exit(self):
        menu = fn.Menu()
        menu_ls = ['North Door', 'East Door']
        choice = menu.generate(menu_ls, "Which door do you take?")

        if choice == '1':
            return (self.coord[0], self.coord[1] + 1)
        elif choice == '2':
            return (self.coord[0] + 1, self.coord[1])
        else:
            print "Try again."
            return self.exit()

class ExitRoom(Room):
    
    def __init__(self):
        self.coord = (0, 4)
        self.first_visit = True

    def enter(self):
        if self.first_visit == True and player.stats['has_key'] == True:
            print text.exit_room['intro_with_key']
            exit(1)
        elif self.first_visit == True and player.stats['has_key'] == False:
            print text.exit_room['intro_no_key']
            return self.exit()
        elif self.first_visit == False and player.stats['has_key'] == False:
            print text.exit_room['returning_no_key']
            return self.exit()
        else:
            print text.exit_room['returning_with_key']
            exit(1)

    def exit(self):
        menu = fn.Menu()
        menu_ls = ['East Door', 'South Door']
        choice = menu.generate(menu_ls, "Which door do you take?")

        if choice == '1':
            return (self.coord[0] + 1, self.coord[1])
        elif choice == '2':
            return (self.coord[0], self.coord[1] - 1)
        else:
            print "Try again."
            return self.exit()

class SwordRoom(Room):

    def __init__(self):
        self.coord = (3, 2)

    def enter(self, previous_room):
        if player.stats['has_sword'] == False:
            print text.sword_room['intro']
            player.stats['has_sword'] = True

            if player.stats['has_flame_sword'] == True:
                print "But you already have your great flaming sword."
                return self.exit()
            else:
                player.stats['dmg'] += 4
                return self.exit()

        else:
            print text.sword_room['intro_returning']
            return self.exit()

    def exit(self):
        exit_menu = ["North Door", "East Door", "South Door", "West Door"]
        return super(SwordRoom, self).exit(self.coord, exit_menu,
         SwordRoom)

class FlameSwordRoom(Room):

    def __init__(self):
        self.coord = (4, 0)

    def enter(self, previous_room):
        if player.stats['has_flame_sword'] == False:
            print text.flamesword_room['intro']
            player.stats['has_flame_sword'] = True

            if player.stats['has_sword'] == True:
                player.stats['dmg'] += 5
            else:
                player.stats['dmg'] += 9

        else:
            print text.flamesword_room['intro_returning']

        return self.exit()

    def exit(self):
        menu = fn.Menu()
        menu_ls = ['North Door', 'West Door']
        choice = menu.generate(menu_ls, "Which door do you take?")

        if choice == '1':
            return (self.coord[0], self.coord[1] + 1)
        elif choice == '2':
            return (self.coord[0] - 1, self.coord[1])
        else:
            print "Try again."
            return self.exit()

class RiddleRoom(Room):
    
    def __init__(self):
        self.coord = (1, 4)
        first_visit = True

    def enter(self, previous_room):
        if first_visit == True:
            print text.riddle_room['intro']
            print "What's your name?"
            name = raw_input('> ')
            print ""

            if name == player.name:
                pass
            else:
                print "Wrong!"
                print "You explode in a whirlwind of names!"
                return (-1, -1)

            print "What's your quest?"
            quest = raw_input('> ')
            print ""

            if len(quest) > 3:
                pass
            else:
                print "Wrong!"
                print "You explode in a whirlwind of quests!"
                return (-1, -1)

            print "What's your favourit colour?"
            colour = raw_input('> ').lower()
            print ""

            if colour == player.stats['favourite_colour']:
                pass
            else:
                print "Wrong!"
                print "You explode in a whirlwind of colour!"
                return (-1, -1)
            
            print ""
            print text.riddle_room['pass_test']
            return self.exit()
        else:
            print "intro_returning"
            return self.exit()

    def exit(self):
        menu = fn.Menu()
        menu_ls = ['East Door', 'South Door', 'West Door']
        choice = menu.generate(menu_ls, "Which door do you take?")

        if choice == '1':
            return (self.coord[0] + 1, self.coord[1])
        elif choice == '2':
            return (self.coord[0], self.coord[1] - 1)
        elif choice == '3':
            return (self.coord[0] - 1, self.coord[1])
        else:
            print "Try again."
            return self.exit()

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

class GnomeRoom(Room):

    def __init__(self):
        self.coord = (4, 1)
        self.first_visit = True

    def enter(self, previous_room):
        if self.first_visit == True:
            self.first_visit = False
            print text.gnome_room['intro']
            print ""
            raw_input("Press RETURN to continue > ")
            print ""
            return self.exit()
        else:
            print text.gnome_room['intro_returning']
            return self.exit()

    def exit(self):
        menu = fn.Menu()
        menu_ls = ['North Door', 'South Door', 'West Door']
        choice = menu.generate(menu_ls, "Which door do you take?")

        if choice == '1':
            return (self.coord[0], self.coord[1] + 1)
        elif choice == '2':
            return (self.coord[0], self.coord[1] - 1)
        elif choice == '3':
            return (self.coord[0] - 1, self.coord[1])
        else:
            print "Try again."
            return self.exit()

class TeleportRoom1(Room):

    def __init__(self):
        self.coord = (0, 1)
    
    def enter(self, previous_room):
        print ""
        print "With a flash, the room shifts and you feel dizzy."
        print "You've been teleported to another room! Witchcraft!"
        print ""
        tp = TeleportRoom2()
        return tp.exit()

    def exit(self):
        menu = fn.Menu()
        menu_ls = ['North Door', 'East Door', 'South Door']
        choice = menu.generate(menu_ls, "Which door do you take?")

        if choice == '1':
            return (self.coord[0], self.coord[1] + 1)
        elif choice == '2':
            return (self.coord[0] + 1, self.coord[1])
        elif choice == '3':
            return (self.coord[0], self.coord[1] - 1)
        else:
            print "Try again."
            return self.exit()

class TeleportRoom2(Room):

    def __init__(self):
        self.coord = (3, 0)

    def enter(self, previous_room):
        print ""
        print "With a flash, the room shifts and you feel dizzy."
        print "You've been teleported to another room! Witchcraft!"
        print ""
        tp = TeleportRoom1()
        return tp.exit()

    def exit(self):
        menu = fn.Menu()
        menu_ls = ['North Door', 'East Door', 'South Door']
        choice = menu.generate(menu_ls, "Which door do you take?")

        if choice == '1':
            return (self.coord[0], self.coord[1] + 1)
        elif choice == '2':
            return (self.coord[0] + 1, self.coord[1])
        elif choice == '3':
            return (self.coord[0], self.coord[1] - 1)
        else:
            print "Try again."
            return self.exit()

class PaintingsRoom(Room):

    def __init__(self):
        self.coord = (1, 0)
        self.first_visit = True

    def enter(self, previous_room):
        if (player.stats['has_flame_sword'] == False and
             self.first_visit == True):
            print text.paintings_room['intro_no_sword']
        elif (player.stats['has_flame_sword'] == True and
             self.first_visit == True):
            print text.paintings_room['intro_has_sword']
        elif (player.stats['has_flame_sword'] == True and
             self.first_visit == False):
            print text.paintings_room['returning_has_sword']
        else:
            print text.paintings_room['returning_no_sword']

        return self.exit()

    def exit(self):
        menu = fn.Menu()
        menu_ls = ['North Door', 'East Door', 'West Door']
        choice = menu.generate(menu_ls, "Which door do you take?")

        if choice == '1':
            return (self.coord[0], self.coord[1] + 1)
        elif choice == '2':
            return (self.coord[0] + 1, self.coord[1])
        elif choice == '3':
            return (self.coord[0] - 1, self.coord[1])
        else:
            print "Try again."
            return self.exit()

class RandomPotionRoom(Room):
    
    def __init__(self):
        self.coord = (4, 4)
        self.first_visit = True
        self.potion_full = True

    def enter(self, previous_room):
        if self.first_visit == True and self.potion_full == True:
            self.first_visit = False
            print text.random_potion_room['intro']
            return self.choose_action()
        elif self.first_visit == False and self.potion_full == True:
            print text.random_potion_room['returning_bottle_full']
            return self.choose_action()
        elif self.first_visit == False and self.potion_full == False:
            print text.random_potion_room['returning_bottle_empty']
            return self.exit()

    def choose_action(self):
        potion = randint(1, 4)
        print ""
  
        if potion == 1:
            print text.random_potion_room['drinking_venom']
            return (-1, -1)
        elif potion == 2:
            print text.random_potion_room['drinking_fortify']
            player.stats['maxHealth'] *= 2
            player.stats['health'] = player.stats['maxHealth']
            print "Your health is now at %d" % player.stats['health']
            return self.exit()
        elif potion == 3:
            print text.random_potion_room['drinking_shrink']
            player.stats['dmg'] /= 2
            print "Your damage is now %d" % player.stats['dmg']
            return self.exit()
        else:
            print text.random_potion_room['drinking_double_damage']
            player.stats['dmg'] *= 2
            print "Your damage is now %d" % player.stats['dmg']
            return self.exit()

        print ""

    def exit(self):
        menu = fn.Menu()
        menu_ls = ['South Door', 'West Door']
        choice = menu.generate(menu_ls, "Which door do you take?")

        if choice == '1':
            return (self.coord[0], self.coord[1] - 1)
        elif choice == '2':
            return (self.coord[0] - 1, self.coord[1])
        else:
            print "Try again."
            return self.exit()

class PitRoom(Room):

    def __init__(self):
        self.coord = (3, 4)

    def enter(self, previous_room):
        print text.pit_room['intro']
        enter_menu = ["Try to jump through the pit.", "Run away!"]
        menu = fn.Menu()
        choice = menu.generate(enter_menu, "What do you do?")

        if choice == '1':
            roll = randint(1, 20) + player.stats['agility']

            if roll < 10:
                print text.pit_room['death']
                return (-1, -1)
            else:
                print text.pit_room['pass_through']
                return self.exit()
        
        elif choice == '2':
            return previous_room
        else:
            self.enter(previous_room)

    def exit(self):
        menu = fn.Menu()
        menu_ls = ['East Door', 'South Door', 'West Door']
        choice = menu.generate(menu_ls, "Which door do you take?")

        if choice == '1':
            return (self.coord[0] + 1, self.coord[1])
        elif choice == '2':
            return (self.coord[0], self.coord[1] - 1)
        elif choice == '3':
            return (self.coord[0] - 1, self.coord[1])
        else:
            print "Try again."
            return self.exit()

class HamsterRoom(Room):

    def __init__(self):
        self.coord = (0, 3)
        self.first_visit = True

    def enter(self, previous_room):
        if self.first_visit == True:
            self.first_visit = False
            player.stats['hamster_found'] = True
            print text.hamster_room['intro']
            print "How will you name it?"
            name = raw_input('> ')
            player.stats['hamster_name'] = '%s the space hamster' % name
            return self.exit()
        else:
            print ("You enter the room in which you found %s." % 
             player.stats['hamster_name'])
            print "There's nothing else here."
            return self.exit()

    def exit(self):
        menu = fn.Menu()
        menu_ls = ['North Door', 'East Door', 'South Door']
        choice = menu.generate(menu_ls, "Which door do you take?")

        if choice == '1':
            return (self.coord[0], self.coord[1] + 1)
        elif choice == '2':
            return (self.coord[0] + 1, self.coord[1])
        elif choice == '3':
            return (self.coord[0], self.coord[1] - 1)
        else:
            print "Try again."
            return self.exit()

class TreasureRoom(Room):

    def __init__(self):
        self.coord = (4, 3)
        self.first_visit = True

    def enter(self, previous_room):
        if self.first_visit == True:
            print text.treasure_room['intro']
            self.first_visit = False
            player.stats['has_gold'] = True
            return self.exit()
        else:
            print text.treasure_room['returning']
            return self.exit()

    def exit(self):
        menu = fn.Menu()
        menu_ls = ['North Door', 'South Door', 'West Door']
        choice = menu.generate(menu_ls, "Which door do you take?")

        if choice == '1':
            return (self.coord[0], self.coord[1] + 1)
        elif choice == '2':
            return (self.coord[0], self.coord[1] - 1)
        elif choice == '3':
            return (self.coord[0] - 1, self.coord[1])
        else:
            print "Try again."
            return self.exit()

# Combat rooms below this line.

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

class HunterRoom(Room):

    hunter_stats = {
    'dmg' : 1,
    'health' : 14,
    'initiative' : 20,
    'accuracy' : 20,
    'alive' : True
    }

    def __init__(self):
        self.coord = (3, 1)
        self.first_visit = True
        self.hostile = False
        self.hunter = fn.Character('Rob the treasure hunter',
             self.hunter_stats)
        self.first_time = True

    def enter(self, previous_room):

        if (player.stats['has_gold'] == True or
             player.stats['has_diamond'] == True):
            self.hostile = True
        else:
            self.hostile = False

        if self.hunter.stats['alive'] and self.first_visit == True:
            print text.hunter_room['intro']
            self.first_visit = False
        elif self.hunter.stats['alive'] and self.first_visit == False:
            print text.hunter_room['returning_alive']
        else:
            print text.hunter_room['returning_dead']
            return self.exit()

        if self.hostile == True:
            print text.hunter_room['hostile']
            return self.choose_action()
        else:
            print text.hunter_room['indifferent']
            return self.exit()

    def choose_action(self):

        if (self.hunter.stats['alive'] == True and
            player.stats['alive'] == True):
            choice_ls = ['Give him the treasure', 'Fight!', 'Run away!']
            menu = fn.Menu()
            choice = menu.generate(choice_ls, 'What do you do?')

            if choice == '1':
                player.stats['has_diamond'] = False
                player.stats['has_gold'] = False
                self.hostile = False
                print text.hunter_room['give_gold']
                return self.exit()
            elif choice == '2':
                combat = fn.Combat(player, self.hunter, self.choose_action,
                previous_room)
                return combat.rounds()
            elif choice == '3':
                return previous_room
            else:
                return self.choose_action(previous_room)
        elif player.stats['alive'] == False:
            print text.hunter_room['death_by_hunter']
            return (-1, -1)
        else:
            print "The treasure hunter is dead!"
            print ""
            return self.exit()

    def exit(self):
        exit_menu = ["North Door", "East Door", "South Door", "West Door"]
        return super(HunterRoom, self).exit(self.coord, exit_menu,
         HunterRoom)
 
class OgreRoom(Room):

    ogre_stats = {
    'dmg' : 5,
    'health' : 25,
    'initiative' : 0,
    'accuracy' : 15,
    'alive' : True
    }

    def __init__(self):
        self.coord = (4, 2)
        self.ogre = fn.Character('Mogor the ogre', self.ogre_stats)
        self.first_time = True

    def enter(self, previous_room):
        if self.ogre.stats['alive'] and self.first_time == True:
            print text.ogre_room['intro_alive']
            self.first_time = False
            return self.choose_action(previous_room)
        elif self.ogre.stats['alive'] and self.first_time == False:
            print text.ogre_room['returning_alive']
            return self.choose_action(previous_room)
        else:
            print text.ogre_room['returning_dead']
            return self.exit()

    def choose_action(self, previous_room):

        if (self.ogre.stats['alive'] == True and
            player.stats['alive'] == True):
            choice_ls = ['Fight!', 'Run away!']
            menu = fn.Menu()
            choice = menu.generate(choice_ls, 'What do you do?')

            if choice == '1':
                combat = fn.Combat(player, self.ogre, self.choose_action,
                previous_room)
                return combat.rounds()
            elif choice == '2':
                return previous_room
            else:
                return self.choose_action(previous_room)
        elif player.stats['alive'] == False:
            print text.ogre_room['death_by_ogre']
            return (-1, -1)
        else:
            print "The ogre is dead!"
            print ""
            return self.exit()

    def exit(self):
        menu = fn.Menu()
        menu_ls = ['North Door', 'South Door', 'West Door']
        choice = menu.generate(menu_ls, "Which door do you take?")

        if choice == '1':
            return (self.coord[0], self.coord[1] + 1)
        elif choice == '2':
            return (self.coord[0], self.coord[1] - 1)
        elif choice == '3':
            return (self.coord[0] - 1, self.coord[1])
        else:
            print "Try again."
            return self.exit()

class OrcRoom(Room):

    orc_stats = {
    'dmg' : 3,
    'health' : 15,
    'initiative' : 100,
    'accuracy' : 50,
    'alive' : True
    }

    def __init__(self):
        self.coord = (4, 2)
        self.orc = fn.Character('Grunt the orc', self.orc_stats)
        self.first_time = True

    def enter(self, previous_room):
        if self.orc.stats['alive'] and self.first_time == True:
            print text.orc_room['intro_alive']
            self.first_time = False
            return self.choose_action(previous_room)
        elif self.orc.stats['alive'] and self.first_time == False:
            print text.orc_room['returning_alive']
            return self.choose_action(previous_room)
        else:
            print text.orc_room['returning_dead']
            return self.exit()

    def choose_action(self, previous_room):

        if (self.orc.stats['alive'] == True and
            player.stats['alive'] == True):
            choice_ls = ['Fight!', 'Run away!']
            menu = fn.Menu()
            choice = menu.generate(choice_ls, 'What do you do?')

            if choice == '1':
                combat = fn.Combat(player, self.orc, self.choose_action,
                previous_room)
                return combat.rounds()
            elif choice == '2':
                return previous_room
            else:
                return self.choose_action(previous_room)
        elif player.stats['alive'] == False:
            print text.orc_room['death_by_orc']
            return (-1, -1)
        else:
            print "The orc is dead!"
            print ""
            return self.exit()

    def exit(self):
        menu = fn.Menu()
        menu_ls = ['North Door', 'East Door', 'West Door']
        choice = menu.generate(menu_ls, "Which door do you take?")

        if choice == '1':
            return (self.coord[0], self.coord[1] + 1)
        elif choice == '2':
            return (self.coord[0] + 1, self.coord[1])
        elif choice == '3':
            return (self.coord[0] - 1, self.coord[1])
        else:
            print "Try again."
            return self.exit()

class HarpyRoom(Room):

    harpy_stats = {
    'dmg' : 1,
    'health' : 10,
    'initiative' : 100,
    'accuracy' : 100,
    'alive' : True
    }

    def __init__(self):
        self.coord = (4, 2)
        self.harpy = fn.Character('Grunt the harpy', self.harpy_stats)
        self.first_time = True

    def enter(self, previous_room):
        if self.harpy.stats['alive'] and self.first_time == True:
            print text.harpy_room['intro_alive']
            self.first_time = False
            return self.choose_action(previous_room)
        elif self.harpy.stats['alive'] and self.first_time == False:
            print text.harpy_room['returning_alive']
            return self.choose_action(previous_room)
        else:
            print text.harpy_room['returning_dead']
            return self.exit()

    def choose_action(self, previous_room):

        if (self.harpy.stats['alive'] == True and
            player.stats['alive'] == True):
            choice_ls = ['Fight!', 'Run away!']
            menu = fn.Menu()
            choice = menu.generate(choice_ls, 'What do you do?')

            if choice == '1':
                combat = fn.Combat(player, self.harpy, self.choose_action,
                previous_room)
                return combat.rounds()
            elif choice == '2':
                return previous_room
            else:
                return self.choose_action(previous_room)
        elif player.stats['alive'] == False:
            print text.harpy_room['death_by_harpy']
            return (-1, -1)
        else:
            print "The harpy dies in an explosion of feathers!"
            print ""
            return self.exit()

    def exit(self):
        menu = fn.Menu()
        menu_ls = ['South Door', 'East Door', 'West Door']
        choice = menu.generate(menu_ls, "Which door do you take?")

        if choice == '1':
            return (self.coord[0], self.coord[1] - 1)
        elif choice == '2':
            return (self.coord[0] + 1, self.coord[1])
        elif choice == '3':
            return (self.coord[0] - 1, self.coord[1])
        else:
            print "Try again."
            return self.exit()

class DragonRoom(Room):

    dragon_stats = {
    'dmg' : 100,
    'health' : 100,
    'initiative' : 100,
    'accuracy' : 50,
    'alive' : True
    }

    def __init__(self):
        self.coord = (4, 2)
        self.dragon = fn.Character('Smaug the dragon', self.dragon_stats)
        self.first_time = True

    def enter(self, previous_room):
        if self.dragon.stats['alive'] and self.first_time == True:
            print text.dragon_room['intro_alive']
            self.first_time = False
            return self.choose_action(previous_room)
        elif self.dragon.stats['alive'] and self.first_time == False:
            print text.dragon_room['returning_alive']
            return self.choose_action(previous_room)
        else:
            print text.dragon_room['returning_dead']
            return self.exit()

    def choose_action(self, previous_room):

        if (self.dragon.stats['alive'] == True and
            player.stats['alive'] == True):
            choice_ls = ['Fight!', 'LEG IT!!!']
            menu = fn.Menu()
            choice = menu.generate(choice_ls, 'What do you do?')

            if choice == '1':
                combat = fn.Combat(player, self.dragon, self.choose_action,
                previous_room)
                return combat.rounds()
            elif choice == '2':
                return previous_room
            else:
                return self.choose_action(previous_room)
        elif player.stats['alive'] == False:
            print text.dragon_room['death_by_dragon']
            return (-1, -1)
        else:
            print "You?! Killed a DRAGON?!?"
            print ""
            return self.exit()

    def exit(self):
        menu = fn.Menu()
        menu_ls = ['North Door', 'East Door', 'West Door']
        choice = menu.generate(menu_ls, "Which door do you take?")

        if choice == '1':
            return (self.coord[0], self.coord[1] + 1)
        elif choice == '2':
            return (self.coord[0] + 1, self.coord[1])
        elif choice == '3':
            return (self.coord[0] - 1, self.coord[1])
        else:
            print "Try again."
            return self.exit()


###

class Map(object):

    rooms = {
        (0, 0) : KeyRoom(),
        (0, 1) : TeleportRoom1(),
        (0, 2) : DragonRoom(),
        (0, 3) : HamsterRoom(),
        (0, 4) : ExitRoom(),
        (1, 0) : PaintingsRoom(),
        (1, 1) : GoblinRoom(),
        (1, 2) : CodeRoom(),
        (1, 3) : SpiderRoom(),
        (1, 4) : RiddleRoom(),
        (2, 0) : OrcRoom(),
        (2, 1) : BladesRoom(),
        (2, 2) : StartingRoom(),
        (2, 3) : HealthRoom(),
        (2, 4) : HarpyRoom(),
        (3, 0) : TeleportRoom2(),
        (3, 1) : HunterRoom(),
        (3, 2) : SwordRoom(),
        (3, 3) : ZombieRoom(),
        (3, 4) : PitRoom(),
        (4, 0) : FlameSwordRoom(),
        (4, 1) : GnomeRoom(),
        (4, 2) : OgreRoom(),
        (4, 3) : TreasureRoom(),
        (4, 4) : RandomPotionRoom(),
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
print ""
print "What's your favourite colour?"
favourite_colour = raw_input('> ').lower()

stats = {
    'dmg' : 1,
    'initiative' : 50,
    'accuracy' : 60,
    'agility' : randint (-3, 3),
    'health' : 20,
    'maxHealth' : 20,
    'alive' : True,
    'has_key' : False,
    'has_sword' : False,
    'has_flame_sword' : False,
    'has_gold' : False,
    'has_diamond' : False,
    'favourite_colour' : favourite_colour,
    'hamster_found' : False,
    'hamster_name' : ' '
}

player = fn.Character(player_name, stats)

a_map = Map((2, 2))
eng = fn.Engine(a_map)
eng.play()
