#!python3
#Testy do "Gra w kółko i krzyżyk"
#Testujemy:
#   - poprawność tworzenia planszy
#   - czy może zrobić ruch

import game as g

def createBoardCorrectness():
    corrrectBoard = [[None, None, None], [None, None, None], [None, None, None]]
    board = g.makeBoard()
    if corrrectBoard != board:
        print("Wrong board.")
    else:
        pass

createBoardCorrectness()

def canMoveCorrectness():
    board = g.makeBoard()
    l1 = [0, 1, 2]
    l2 = [0, 1, 2]
    for n, m in zip(l1, l2):
        coor = [n, m]
        sign = 'o'
        if not g.canMove(coor, sign, board):
            print("The move had not been created or had been creatd wrong.")

canMoveCorrectness()

def isFullCorrectness():
    new_board = [['o','x','o'], ['o','o','x'], ['x','o','o']]
    if not g.isFull(new_board):
        print("Sth is wrong.")
    new_board = [['o','x','o'], ['o','o','x'], ['x','o', None]]
    if g.isFull(new_board):
        print("Sth is wrong.")
