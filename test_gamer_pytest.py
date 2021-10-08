from gamer import Gamer
from cards import Cards
import numpy as np

class Test_gamer:
    def setup(self):
        self.gamer = Gamer('Valery')
        self.card = Cards()

    def teardown(self):
        pass

    def test_init(self):
        assert self.gamer.name == 'Valery'
        assert isinstance(self.gamer.card, Cards)

    def test_get_name(self):
        assert self.gamer.name == 'Valery'

    def test_new_card(self):
        self.card.generate()

        for r in range( 3 ):
            num_count = 0
            for c in range( 9 ):
                if self.card.lst_card[r][c][0] > 0 :  #  [0] - число на бочке [1] - 0:не выпало, 1-выпало
                    num_count += 1
            assert  num_count == 5   # в строке карточки 5 цифр
            arr = np.array(self.card.lst_card)
            lst = np.sum( arr, axis=0 )
            for r in lst:
                assert r[0] > 0   # в колонках карточки есть хотя бы одна цифра

    def test_seek_number(self):  #  наличие числа  на карточке игрока
        for i in range( 9 ):
            n = self.card.lst_card[0][i][0]
            if n > 0:
                break
        assert self.card.seek_number(n) == True
        assert self.card.seek_number(91) == False
