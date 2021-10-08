from cards import Cards

class Gamer:
    def __init__(self, name):
        self.name = name
        self.card = Cards()

    def get_name(self):
        return self.name

    def new_card(self):
        self.card.generate()

    def seek_number(self, num ):
        return self.card.seek_number( num )

    #def set_barrel(self, b ):   # совпавшие с номерами
    #    self.barrel += b



    def get_cards(self):
        return self.card.get_cards(), self.card.get_numOK()




