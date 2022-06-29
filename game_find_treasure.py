import random, time

# zmienne skarb
TreasureMax_x, TreasureMin_y = 15, 15
Treasure_x = random.randint(0,TreasureMax_x)
Treasure_y = random.randint(0,TreasureMin_y)
Treasure_xy = {"x":Treasure_x,"y":Treasure_y}
x, y = 0, 0
#zmienne user
User_xy = {"x":0,"y":0}

#licznik prob
counter = 0

#funkcje
def movement(move):
    global x,y
    move = move.capitalize()

    if move == 'W':
        y += 1
        if y <= 15: #gora
            User_xy['y'] = y
            return User_xy['y']
        else:
            y = 15
            print('Wspolrzedna poza obszarem gry, tak nie moze byc!')
            return y
    elif move == 'S': #dol
        y -= 1
        if y >= 0:
            User_xy['y']= y
            return User_xy['y']
        else:
            y = 0
            print('Wspolrzedna poza obszarem gry, tak nie moze byc!')
            return y
    elif move == "D": #prawo
        x += 1
        if x <= 15:
            User_xy['x'] = x
            return User_xy['x']
        else:
            x = 0
            print('Wspolrzedna poza obszarem gry, tak nie moze byc!')
            return x

    elif move == "A": #lewo
        x -= 1
        if x >= 0:
            User_xy['x'] = x
            return User_xy['x']
        else:
            x = 0
            print('Wspolrzedna poza obszarem gry, tak nie moze byc!')
            return x
    else:
        return print('Zly klawisz, sterowanie tylko za pomoca W S A D')

def podpowiedz(user_xy, fcn):
    if  user_xy['x'] == Treasure_xy['x'] and user_xy['y'] == Treasure_xy['y']:
        return fcn()
    elif (user_xy['x'] == Treasure_xy['x'] - 4 and user_xy['y'] == Treasure_xy['y'] ) or \
    (user_xy['y'] == Treasure_xy['y'] - 4) and user_xy['x'] == Treasure_xy['x']:
        return print('Podpowiedz: \n Jestes bardzo blisko skarbu!')
    elif user_xy['y'] == Treasure_xy['y']:
        return print('Podpowiedz: \n Jestes w idealnej wspolrzednej y, idz w lewo albo prawo ')
    elif user_xy['x'] == Treasure_xy['x']:
        return print('Podpowiedz: \n Jestes w idealnej wspolrzednej x, idz w gore albo w dol ')
    else:
        return print('Graj dalej')

def dekorator(wsp):
    def wrap():
        print('|--------------------------------------|')
        wsp()
        print('|--------------------------------------|')
    return wrap

#funkcje anonimowe do dekoratora
lam = lambda : print(f'Twoje obecne wspolrzedne to x: {User_xy["x"]}, a y: {User_xy["y"]}')
clear = lambda: print('\n' * 10)
result = lambda: print('\nBrawo udalo ci sie znalezc skarb!!!')

#przypisanie dekoratora
dek_wspol = dekorator(lam)

if __name__ == "__main__":
    print('''*Znajdz skarb*
    Poruszanie:
     W - gora 
     S - dol 
     A - w lewo 
     D - w prawo
Gra konczy sie jesli gracz odkryje gdzie znajduje sie skarb :)\n''')
    while (play := input('Chcesz zacząć gre? y/n ')) != 'n':
        print('Gra zacznie sie za 5 sekund ...')

        for t in range(5, 0, -1):
            print(t)
            time.sleep(1)
        clear()
        while User_xy != Treasure_xy:
            user_move = input('Podaj gdzie chcesz sie poruszyc: ')
            movement(user_move)
            time.sleep(1)
            clear()
            dek_wspol()
            podpowiedz(User_xy, result)
            counter+=1

        print('Ilosc poruszen do zdobycia skarbu:{0} '.format(counter))
        break

#---------------------------------------
    if play == 'n':
        print('\nNie? to wychodzimy z gry ')
