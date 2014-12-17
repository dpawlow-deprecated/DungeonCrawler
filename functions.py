from random import randint

class Menu(object):
    """Generates all the menus that are needed in the game"""

    def generate(self, lists, question):
        n = 0
        print question

        for i in lists:
            print "%d) %r" % (lists.index(i) + 1, i)
        
        return raw_input("> ")


class Engine(object):
    """Runs the game by handing the selected room to the player"""

    def __init__(self, room_map):
        self.room_map = room_map

    def play(self):
        current_room = self.room_map.starting_room
        exit_room = self.room_map.rooms[(0, 4)]
        prev_room_coord = (2, 2)

        while current_room != exit_room or hero.has_key == False:
            # The previous room coordinates are given mainly for the
            # "run away!" functionality.        
            next_room_coord = current_room.enter(prev_room_coord)
            prev_room_coord = current_room.coord
            current_room = self.room_map.next_room(next_room_coord)
            

class Character(object):
    """Template for all characters"""

    def __init__(self, name, stats):
        self.name = name
        self.stats = stats

class Combat(object):

    def __init__(self, player, enemy, scene, previous_room):
        self.scene = scene
        self.previous_room = previous_room
        if player.stats['initiative'] >= enemy.stats['initiative']:
            self.ch1 = player
            self.ch2 = enemy
        else:
            self.ch1 = enemy
            self.ch2 = player

    def rounds(self):
        print ""

        if (self.ch1.stats['alive'] == True and 
            self.ch1.stats['accuracy'] > randint(1, 100)):
            self.ch2.stats['health'] -= self.ch1.stats['dmg']
            print "%s takes %d damage!" % (self.ch2.name,
                self.ch1.stats['dmg'])
        else:
            print "%s's attack misses!" % self.ch1.name
        
        if self.ch2.stats['health'] <= 0:
            self.ch2.stats['alive'] = False
            return self.scene(self.previous_room)
        else:
            pass

        print ""
        
        if (self.ch2.stats['alive'] == True and
            self.ch2.stats['accuracy'] > randint(1, 100)):
            self.ch1.stats['health'] -= self.ch2.stats['dmg']
            print "%s takes %d damage!" % (self.ch1.name,
                self.ch2.stats['dmg'])
        else:
            print "%s's attack misses!" % self.ch2.name
        
        print ""

        if self.ch1.stats['health'] <= 0:
            self.ch1.stats['alive'] = False
        else:
            pass

        return self.scene(self.previous_room)