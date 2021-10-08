from gamer import Gamer
import random

class Go_game:
    def __init__(self):
        self.gamers = []  # игроки
        self.bag = [ x for x in range( 1,91 )]
        self.missing=[]   # Не выпавшие
        self.take=[]
        self.isVictory = -1

    def win_gamer(self, i):
        lst, lstOK = self.gamers[i].get_cards()
        if len( lstOK ) == 15:
            self.isVictory = i
        left = '|'
        right = '|'
        s = ''
        if self.isVictory < 0:
            for i in range(3):
                s += left
                for j in range(9):
                    n = lst[i][j]
                    ch = '   '
                    if n > 0:
                        ch = str(n)
                        s += ch.rjust(3, ' ') + right
                    elif n < 0:
                        ch = ' X '
                        s += ch +right
                    else:
                        s += ch + right
                if i == 0:
                    s += '           Принял: '
                    for ss in lstOK:
                        s += str(ss)+'.'

                s += '\n'
        else:
            if self.isVictory == i:
                s = "П О Б Е Д А   !!!\n "
        return s

    def win_game(self, n_barrel):
        print( '*'*60)
        if n_barrel == 0:
            barrel = ''
        else:
            barrel = str( n_barrel )
        print( 'Мешок:', self.bag )
        print(' Бочка из мешка: ', barrel )

        for i,g in enumerate( self.gamers ):
            print( i+1,'Игрок: ', g.get_name() )
            print( self.win_gamer(i) )

        print( 'Не выпавшие:' )
        ss = ''
        for i,vv in enumerate(self.missing):
            ss += str(vv)+'.'
            aaa = (i+1)%10
            if i+1 % 10 == 0:
                ss += '\n'
        print( ss )

    def start_game(self):
        args = ['Comp', 'Homo Sapiens']

        for s in args:  # чтение игроков
            self.gamers.append( Gamer(s) )

        print('Вступили в игру:')
        for i, g in enumerate(self.gamers):  # вывод имен игроков
            print( i+1,g.get_name() )

        # раздача карточек (по одной)
        for i in range( len(self.gamers) ):
            self.gamers[i].new_card()


        game = True
        n_barrel = 0
        while self.isVictory < 0:
            self.win_game( n_barrel )

            if self.isVictory >= 0:
                continue

            n = input('Продолжим? (1-Да, 0-нет)')
            if n == '0':
                self.isVictory = 100
            else:
                ind = random.randint( 0, len( self.bag )-1 )
                print(ind)
                n_barrel = self.bag.pop( ind )  # достали без возвращения из мешка

                ok = 0
                for g in self.gamers:
                    isOK = g.seek_number(n_barrel)
                    if isOK:
                        ok += 1
                    #print( '---------------------------------------',isOK )
                if ok == 0:
                    self.missing.append(n_barrel)


if __name__ == '__main__':
    loto = Go_game()
