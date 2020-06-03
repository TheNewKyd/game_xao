#!python3
#Gra w kółko i krzyżyk
#Potrzebne funkcje:
#   - tworzenie planszy
#   - weryfikacja ruchów
#   - zliczanie znaków w jednej linii
#   - w jednej komórce, jeden znaków

from tabulate import tabulate

def threeInRow(new_board):
    b = new_board

    for r in range(3):
        if b[r][1] == b[r][0] == b[r][2]:
            winner = b[r][1]
            return winner
            break
        else:
            pass

def threeInCol(new_board):
    b = new_board

    for c in range(3):
        if b[1][c] == b[0][c] == b[2][c]:
            winner = b[1][c]
            return winner
            break
        else:
            pass

def threeInCross(new_board):
    b = new_board

    if b[1][1] == b[0][2] == b[2][0]:
        winner = b[1][1]
        return winner

    elif b[1][1] == b[0][0] == b[2][2]:
        winner = b[1][1]
        return winner
    else:
        pass

def makeBoard():
    board = [[None, None, None] for rows in range(3)]
    return board

def canMove(coor,sign, board):
    board = board
    coor_a = coor[0]
    coor_b = coor[1]

    if board[coor_a][coor_b] == None:
        board[coor_a][coor_b] = sign
        print(tabulate(board))

    new_board = board

    return new_board

def isFull(new_board):
    return None not in new_board

def endWindow(winner):
    endGame(False)
    return f"Zwycięzcą turnieju szamanów zostaje {winner}"

def endGame(info):
    return info

def theGame(coor, sign, board):
    new_board = canMove(coor, sign, board)
    sign_list = ['x', 'o']

    if threeInRow(new_board) in sign_list:
        winner = threeInRow(new_board)
        return endWindow(winner)

    elif threeInCol(new_board) in sign_list:
        winner = threeInCol(new_board)
        return endWindow(winner)

    elif threeInCross(new_board) in sign_list:
        winner = threeInCross(new_board)
        return endWindow(winner)

    elif not isFull(new_board):
        return "Plansz pełna."
