# import the python datetime module to help us create a timestamp
from datetime import date
from slithering import Anaconda, Copperhead, CornSnake, RatSnake, Salamander
from swimming import Goldfish, Goose, Koi, Mallard, Swan
from walking import Donkey, Goat, Llama, Sheep, Zebra


miss_fuzz = Llama("Miss Fuzz", "Domestic Llama", "midday", "Llama Chow")

eeyore = Donkey("Eeyore", "Donkey", "morning", "Donkey Chow")

vincent = Goat("Vincent", "Pygmy Goat", "afternoon", "Goat Chow")

marty = Zebra("Marty", "Plains Zebra", "midday", "Zebra Chow")

shaun = Sheep("Shaun", "Merino Sheep", "morning", "Sheep Chow")

bitey = Copperhead("Bitey", "Southern Copperhead", "Mice")

wilbur = RatSnake("Wilbur", "Black Rat Snake", "Mice")

stretchy = Anaconda("Stretchy", "Green Anaconda", "Mice")

popcorn = CornSnake("Popcorn", "Amelastic Corn Snake", "Mice")

sally = Salamander("Sally", "Spotted Salamander","Crickets")

quackers = Mallard("Quackers", "Mallard Duck","Duck Feed")

goldie = Goldfish("Goldie", "Common Goldfish", "Fish Food")

kenji = Koi("Kenji", "Butterfly Koi", "Fish Food")

ryan = Goose("Ryan", "Canada Goose", "Goose Feed")

odette = Swan("Odette", "Mute Swan", "Swan Feed")
 
print(f'{miss_fuzz.name} the {miss_fuzz.species} is available to pet during the {miss_fuzz.shift} shift.')
miss_fuzz.feed()
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
