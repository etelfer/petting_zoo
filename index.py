# import the python datetime module to help us create a timestamp
from datetime import date
from slithering import Anaconda, Copperhead, CornSnake, RatSnake, Salamander
from swimming import Goldfish, Goose, Koi, Mallard, Swan
from walking import Donkey, Goat, Llama, Sheep, Zebra


miss_fuzz = Llama("Miss Fuzz", "Domestic Llama", "midday")

eeyore = Donkey("Eeyore", "Donkey", "morning")

vincent = Goat("Vincent", "Pygmy Goat", "afternoon")

marty = Zebra("Marty", "Plains Zebra", "midday")

shaun = Sheep("Shaun", "Merino Sheep", "morning")

bitey = Copperhead("Bitey", "Southern Copperhead")

wilbur = RatSnake("Wilbur", "Black Rat Snake")

stretchy = Anaconda("Stretchy", "Green Anaconda")

popcorn = CornSnake("Popcorn", "Amelastic Corn Snake")

sally = Salamander("Sally", "Spotted Salamander")

quackers = Mallard("Quackers", "Mallard Duck")

goldie = Goldfish("Goldie", "Common Goldfish")

kenji = Koi("Kenji", "Butterfly Koi")

ryan = Goose("Ryan", "Canada Goose")

odette = Swan("Odette", "Mute Swan")
 
print(f'{miss_fuzz.name} the {miss_fuzz.species} is available to pet during the {miss_fuzz.shift} shift.')
# print(eeyore.name)
# print(vincent.name)
# print(marty.name)
# print(shaun.name)
# print(bitey.name)
# print(wilbur.name)
# print(stretchy.name)
# print(popcorn.name)
# print(sally.name)
# print(quackers.name)
# print(goldie.name)
# print(kenji.name)
# print(ryan.name)
# print(odette.name)
