#!python3
#Gra w kółko i krzyżyk
#Gra dla dwóch graczy ,dwóch użytkowników.
#Gracze wypełniają komórki znakami + lub o,
#wygrywa ten, który ułoży 3 w lini prostej,
#po skosie, poziomo lub pionowo.

import game as g
import pyinputplus as pyip

def coordinates():
    coor = []
    words = ['First', 'Second']
    for i in range(1):
        for w in words:
            c = pyip.inputInt(f"{w} coordinate: ")
            coor.append(c)
    return coor

def checkIfGood(sign):
    sign_list = ['x', 'o']
    if sign in sign_list:
        return sign
    else:
        raise Exception("Use x or o.")

if __name__=='__main__':
    board = g.makeBoard()
    while True:
        sign = pyip.inputCustom(checkIfGood, "Sign: ")
        coor = coordinates()
        if type(g.theGame(coor, sign, board)) == str:
            break
    print(g.theGame(coor, sign, board))
