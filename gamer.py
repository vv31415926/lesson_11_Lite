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

    def get_cards(self):
        return self.card.get_cards(), self.card.get_numOK()

    def __str__(self):
        s = f'Игрок {self.name}'
        return s

    def __eq__(self, other):
        r = (   self.name == other.name  )
        return r

    def __ne__(self, other):
        r = (   self.name != other.name  )
        return r
