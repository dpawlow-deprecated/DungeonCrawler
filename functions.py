class Menu(object):
    """Generates all the menus that are needed in the game"""

    def generate(self, lists, question):
        n = 0
        print question

        for i in lists:
            print "%d) %r" % (lists.index(i) + 1, i)
        
        return raw_input("> ")


class Character(object):
    """Template for all characters"""

    def __init__(self, name, stats):
        self.name = name
        self.stats = stats
