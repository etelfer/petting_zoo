from datetime import date

class Mallard:
    def __init__(self, name, species):
        # Establish the properties of each animal
        # with a default value
        self.name = ""
        self.species = ""
        self.date_added = date.today()
        self.swimming = True