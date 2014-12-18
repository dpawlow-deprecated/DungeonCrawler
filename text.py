starting_room = {
    'intro_first_time' : """
 You wake up in a dimly lit room, barely remembering falling through a
pit. Looking up you can get a peek of sunshine, it must be the hole
through which you fell.
 Looking around you find out that the room is square and has a door
on each wall. There must be a way out, back to the surface.
Lucky for you, it's possible to get oriented, thanks to the sun.
Time to move on, then.
""",
    'intro_returning' : """
 You come back to the room in which you woke up. It's still the same
old room, with the sun still shining outside.
"""
}

key_room = {
    'intro' : """
You enter a room that has only two doors. Clearly this is one of the
corners of the dungeon.
Looking around you find a big iron key hanging from a wall. This could
be really important.
""",
    'intro_returning' : """
You return to the room in which you found the key.
There doesn't seem to be much else aside from rotten chairs and tables.
"""
}

exit_room = {
    'intro_no_key' : """
You enter a room with a massive iron door on one of the walls.
Looking through the big keyhole you can get some peeks of sunshine and
fresh air. This must be the way out!
You push the door but it's locked. You look around the room for the key
but it's nowhere to be found.
After a while, you decide that the key must be in another room, time to
go looking for it.
""",
    'intro_with_key' : """
You enter a room with a massive iron door on one of the walls.
Looking through the big keyhole you can get some peeks of sunshine and
fresh air. This must be the way out!
You fit the key in the lock and turn it...
Clank!
You are free!
""",
    'returning_with_key' : """
You return to the room with the massive iron door.
You fit the key in the lock and turn it...
Clank!
You are free!
""",
    'returning_no_key' : """
You return to the room with the massive iron door, but you still hadn't
found the key. It must be somewhere around this dungeon!
"""
}

health_room = {
    'intro_bottle_full' : """
 You enter a room with a glass flask on a table in the middle.
The flask contains a red liquid, and a faded out inscription that
barely reads '... Potion'.
""",
    'intro_bottle_empty' : """
 You enter the room were you found the health potion.
The empty flask is lying around somewhere.
""",
    'drink_potion' : """
 You chug down the contents of the flask.
You feel revitalized and are now at full health.
"""
}

blades_room = {
    'intro' : """
 You enter a room with cleaving blades hanging from the ceiling. 
The blades are moving about, blocking the way to the other doors.
It seems bloody dangerous, but perhaps you can jump through the blades,
if you are quick enough...
""",
    'intro_returning' : "Oh, bloody hell! Not the blades again!",
    'death' : """
 As you try to pass through the blades, a sudden movement cleaves your
body in half.
""",
    'pass_through' : """
You narrowly make it through, your heart is racing.
"""
}

paintings_room = {
    'intro_no_sword' : """
You enter a pitch black room. Stumbling about, you eventually find
the way out.
""",
    'intro_has_sword' : """
You enter a room submerged in darkness, but drawing your flaming sword
you have your very own light source!
Hanging on the walls you see marvelous paintings with golden frames.
There are depictions of dragons, landscapes and kings long forgotten.
And you keep wondering what kind of lost stories this place could
unravel.
""",
    'returning_no_sword' : """
You enter once again to the pitch black room. You stumble again to
the exit.
""",
    'returning_has_sword' : """
You enter once again to the pitch black room, but drawing your flaming sword
you have your very own light source!
Hanging on the walls you see marvelous paintings with golden frames.
There are depictions of dragons, landscapes and kings long forgotten.
And you keep wondering what kind of lost stories this place could
unravel.
"""
}

sword_room = {
    'intro' : """
 You enter a room with walls covered in old and rusty armor. There are
broken weapons lying around everywhere. A little reflection catches your
eye, it is a sheathed sword! And it seems strangely untouched by the
rust that ate the other weapons.
Now you have a sword! It will surely be of some use.
""",
    'intro_returning' : """
 You enter to the old armory once again. So many unanswered questions.
Who owned this place?
"""
}

random_potion_room = {
    'intro' : """
You enter a room full shattered glass throughout the floor. It seems to
be from various laboratory equipment, this must've been an alchemy lab!
There remains a lonely bottle, with a transparent liquid inside and no
label. What could be the effect of this brew?
""",
    'returning_bottle_full' : """
You return to the alchemy lab. The bottle beckons you to drink it.
""",
    'returning_bottle_empty' : """
You return to the alchemy lab, there are no more bottles for you to
drink.
""",
    'drinking_venom' : """
You drink from the bottle. Moments later you begin to feel ill, drop to
the floor and draw your last breath.
It was venom! 
""",
    'drinking_fortify' : """
You drink from the bottle. Moments later you begin to feel fortified.
Your maximum health has doubled!
""",
    'drinking_shrink' : """
You drink from the bottle. Moments later you begin to feel less
powerful. Your damage is reduced by half.
""",
    'drinking_double_damage' : """
You drink from the bottle. Moments later you begin to feel more
powerful. Your damage is doubled!
"""
}

hamster_room = {
    'intro' : """
You enter a room that doesn't seem to have anything special.
Looking down you find a little hamster running around your feet.
When you kneel beside it, it climbs to your pocket and sticks its
head out.
"""
}

treasure_room = {
    'intro' : """
You enter a room with broken chests and rusted iron bars. This must've
been the Treasury.
Removing some debris you found a few gold coins!
You pocket them, thinking that this dungeon could make you rich!
""",
    'returning' : """
You return to the Treasury, but sadly there's no more gold to be found.
"""
}

zombie_room = {
    'intro_alive' : """
 You feel a unbearable smell as you enter the room. It's rotten, putrid
and rancid. As you cover your nose with your sleeve you see movement.
There is a zombie in here!
""",
    'returning_alive' : """
 You return to the awful smelling room.
The damn zombie is still here!
""",
    'returning_dead' : """
 You are back once again in the rotten room.
Covering your nose, you pass through it as quickly as you can.
""",
    'death_by_zombie' : """
 Despite all your efforts to keep the zombie at bay, it traps you in a
corner and begins to chew away at your flash.
"""
}

code_room = {
    "first_intro" : """
 You enter a room with five levers in it. It does not appear that the
levers operate the doors, so what's their purpose? 
""",
    "intro_returning" : """
 You return to the room with the levers, wondering what the correct
combination could mean.
""",
    "cracking_code" : """
 As you push the last lever into place, you hear a metallic clank! and
turn to see a wonderful diamond being dropped from a new hole in the
wall. Your luck seems to be changing, this could make you rich!
""",
    "returning_cracked" : """
 You return to the room with the levers. There seems to be nothing else
of relevance here.
""",
    "explain_mechanism" : """
 There are five levers. Each one can be up (1) or down (0).
"""
}

spider_room = {
    'intro_alive' : """
 As you enter this room, you feel sticky webs all around you. You are
focused on getting the silky substance off your clothes when you realise
that this is a spider lair: and there is a big spider right in front of
you! And it has a sac with eggs in its abdomen! Ewww!
""",
    'returning_alive' : """
 You return to the spider's lair.
Obviously, the damn spider is still in here!
""",
    'returning_dead' : """
 You return to the spider's lair. As you pass through it, hacking your
way out of the spider web, you feel hundreds of eyes looking at you.
Looking around, you see the tiny baby spiders staring at you with
reproach, as if saying 'You killed our lovely moma'.
With remorse, you look away and exit the room.
""",
    'death_by_spider' : """
 Fighting in this spider web has made you slower as you get tangled
in it. Finally, you can't move anymore, and the spider wraps you up,
probably to feed you to its offspring later.
""",
    'killing_spider' : """
 As you deliver the final blow, the spider's eggsac burst open and a
hundred tiny spider scurry away from you.
The spider is dead!
""",
}

goblin_room = {
    'intro_alive' : """
 When you enter the room you see nothing. But as you take a few steps
you are ambushed by a little and sickly looking goblin!
""",
    'returning_alive' : """
 When you come back to the room, the goblin manages to sneak up on you
once again!
""",
    'returning_dead' : """
 You return to the room in which the goblin lays dead.
You are tempted to loot him, but what could you possibly get?
'Level 1 ragged clothing'?
""",
    'death_by_spider' : """
 The little goblin evades your strikes, it's so little and so fast!
Finally it leaps to your throat and slices it open.
""",
}

ogre_room = {
    'intro_alive' : """
 As you enter this room you see a big dumb ogre, cooking what it seems
to be a rat kebab. When he notices your presence he takes his big wooden
club and says 'Mogor has human dinner now!'
""",
    'returning_alive' : """
 When you return to the ogre's room, he seems to be happy and exclaims:
'Hooray! Human dinner come back!'
""",
    'returning_dead' : """
 In the ogre's room his dinner is still cooking. As you pass by the dead
ogre you consider taking a bite off the rat kebab...
It smells pretty good...
""",
    'death_by_ogre' : """
 The big ogre squashes you against the floor.
You are going to make a lovely dinner with mashed potatoes.
""",
}

gnome_room = {
    "intro" : """
 As you enter the room you smell the strong scent of tobacco.
Through the smoke you distinguish a small figure lying against a wall.
It's a gnome!
"Don't mind me, stranger" he says, "I'm resting my feet, as I had to ran
away from an ogre who wanted me as his dinner. I see you are lost, so
I'll give you some advice: there's a way out from the dungeon: a big
door in one of the dungeon's corners. But to open that door you'll need
the key that's lying around somewhere, in some room.
 Now, I'm dreadfully tired, let me sleep, godspeed.
""",
    "intro_returning" : """
 You enter the room in which you found the little gnome. There's still
some scent of tobacco, but now, the gnome's snoring fills the air.
"""
}

riddle_room = {
    'intro' : """
 You enter a weird room, full of plants of different and unwordly
colours. In the middle of the room there is a little old man with a
stick.
He asks you:
""",
    'intro_returning' : """
You enter the room with the weird man who asks questions.
As you pass through the room he waves at you and smiles.
""",
    'pass_test' : """
 Very good! You passed your test, you can go now.
"""
}

flamesword_room = {
    'intro' : """
As you enter the room a bright light makes you cover your eyes.
When you get accustomed to the light you see that it's source is
a flaming sword!
This will definitely help against the monsters that lurk around here!
""",
    'intro_returning' : """
You return to the room in which you found the flaming sword.
Without the sword seems pretty boring.
"""
}

orc_room = {
    'intro_alive' : """
As you enter this room, an orc charges at you.
No time for introductions, it seems.
""",
    'returning_alive' : """
The orc is still in the room. He looks pretty mad, probably because you
got away last time...
""",
    'returning_dead' : """
Returning to the room in which you fought the orc, you see no reason for
staying in it. Why the orc did it, you don't know. Orcs are pretty wild
and strange creatures.
""",
    'death_by_orc' : """
With an skull shattering cry, the orc attacks.
Wait, it was not the cry that was skull shattering, it was his axe!
""",
}

harpy_room = {
    'intro_alive' : """
You enter a room full of feathers flying around. As you do, you hear
a high pitched scream and a harpy comes down on you, ready to attack.
""",
    'returning_alive' : """
Without wasting time, the harpy attacks you once again as you
enter the room!
""",
    'returning_dead' : """
You return to the room in which you fought the harpy.
There are still feathers flying around.
""",
    'death_by_harpy' : """
With lightning speed, the harpy strikes at you with its talons, time
and time and time again.
""",
}

hunter_room = {
    'intro' : """
You enter a room with a lot of rubble in it. Between some boulders you
see a man looking for something on the floor.
""",
    'returning_alive' : """
You return to the room in which you found the treasure hunter.
""",
    'returning_dead' : """
You return to the room in which you fought the treasure hunter.
Shame he hadn't found any treasure you could loot off him.
""",
    'hostile' : """
Seeing as you have some treasure in your pocket, the treasure hunter
leaps at you with a scream.
""",
    'indifferent' : """
You don't seem to interest the treasure hunter. Probably because you
aren't made of gold.
""",
    'death_by_hunter' : """
Even before you exhale your last breath, the treasure hunter begins
to check your pockets for gold.
""",
    'give_gold' : """
You give all your treasure to the treaure hunter, which seems to appease
him. He returns to his scavenging and you are now free to go.
"""
}

dragon_room = {
    'intro_alive' : """
As you enter this sulphur smelling room you see A DRAGON!
A LIVING DRAGON!
IT'S WAKING UP! 
QUICK, RUN AWAY!!!
""",
    'returning_alive' : """
HOW COULD YOU COME BACK? DIDN'T YOU SEE THAT THERE WAS A BLOODY DRAGON
IN HERE? RUN!
""",
    'returning_dead' : """
How did you manage to kill the dragon?!?
""",
    'death_by_dragon' : """
The dragon cooks you up with his fiery breath and then eats you whole.
I warned you, but you are dumb as a brick.
""",
}

pit_room = {
    'intro' : """
You enter a room with a bottomless pit! Who on their right mind could
build this room?
You'll have to jump to get to the other side of the pit to get to the
other doors.
""",
    'returning' : """
You return to the room with the bottomless pit.
Would you jump this time?
""",
    'death' : """
You try to jump to the other side but you can't get a good footing.
You fall backward into the pit!
After a looooong fall you squash against the ground.
""",
    'pass_through' : """
You jump just far enough to get to the other side!
"""
}