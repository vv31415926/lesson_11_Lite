import numpy as np
import random

class Cards:
    def __init__(self):
        self.lst_card = [  [ [0,0] for x in range(0, 9)] for y in range(0, 3)  ]
        self.numOK=[]

    def generate(self):
        lst = [ x for x in range( 1,91 ) ] # все возможные бочки
        lst = random.sample( lst, 90)  # встряхнуть мешок

        i = 0           # по бочкам
        r = 0
        completion = 0
        while completion < 27:
            n = lst[i]      # текущий уникальный номер
            col = min(n // 10, 8)   # колонка для этого номера
            for r in range(0, 3):
                if self.lst_card[r][col][0] == 0:  # ячейка не занята
                    self.lst_card[r][col][0] = n
                    completion += 1
                    break
            i += 1

        lst9 = [0,1,2,3,4,5,6,7,8]
        lst9 = random.sample( lst9, 9 )
        for r in range(0,2 ):   # оставить в строке только 5 номеров
            lstx = random.sample( lst9, 4 )
            for c in lstx:
                self.lst_card[r][c][0] = 0   #  [0] - число на бочке [1] - 0:не выпало, 1-выпало

        r = 2
        isNul = True
        while isNul:
            lstx = random.sample(lst9, 4)
            isNul = False
            for c in lstx:
                if self.lst_card[0][c][0] + self.lst_card[1][c][0] == 0:
                    isNul = True
                    break
        for c in lstx:
            self.lst_card[r][c][0] = 0

    def seek_number(self, num ):
        yes = False
        for i in range(3):
            for j in range(9):
                if self.lst_card[i][j][0] == num:   # совпало
                    self.lst_card[i][j][0] = 0
                    self.lst_card[i][j][1] = 1
                    self.numOK.append(  num )
                    yes = True
        return yes

    def get_numOK(self):
        return self.numOK


    def get_cards(self):
        s=[]
        for i in range(3):
            sc=[]
            for j in range(9):
                if self.lst_card[i][j][1] == 0:   # не выпала
                    sc.append( self.lst_card[i][j][0]  )
                else:
                    sc.append( -1 )
            s.append( sc )
        return s


if __name__ == '__main__':
    c = Cards()
    card = c.generate()
    for i in range(3):
        print( card[i])