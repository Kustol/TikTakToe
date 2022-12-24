import random
import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy

sign = 0

global board
board = [[' ' for x in range(3)] for y in range(3)]



def CheckWins(b, p):
    return ((b[0][0] == p and b[0][1] == p and b[0][2] == p) or
            (b[1][0] == p and b[1][1] == p and b[1][2] == p) or
            (b[2][0] == p and b[2][1] == p and b[2][2] == p) or
            (b[0][0] == p and b[1][0] == p and b[2][0] == p) or
            (b[0][1] == p and b[1][1] == p and b[2][1] == p) or
            (b[0][2] == p and b[1][2] == p and b[2][2] == p) or
            (b[0][0] == p and b[1][1] == p and b[2][2] == p) or
            (b[0][2] == p and b[1][1] == p and b[2][0] == p))


def isfree(i, j):
    return board[i][j] == ' '


def isfull():
    flag = True
    for i in board:
        if (i.count(' ') > 0):
            flag = False
    return flag


def pc():
    possiblemove = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                possiblemove.append([i, j])
    move = []
    if possiblemove == []:
        return
    else:
        for let in ['O', 'X']:
            for i in possiblemove:
                boardcopy = deepcopy(board)
                boardcopy[i[0]][i[1]] = let
                if CheckWins(boardcopy, let):
                    return i
        corner = []
        for i in possiblemove:
            if i in [[0, 0], [0, 2], [2, 0], [2, 2]]:
                corner.append(i)
        if len(corner) > 0:
            move = random.randint(0, len(corner) - 1)
            return corner[move]
        edge = []
        for i in possiblemove:
            if i in [[0, 1], [1, 0], [1, 2], [2, 1]]:
                edge.append(i)
        if len(edge) > 0:
            move = random.randint(0, len(edge) - 1)
            return edge[move]



def get_text_pc(i, j, gb, p1, p2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            p1.config(state=DISABLED)
            p2.config(state=ACTIVE)
            board[i][j] = 'X'
        else:
            button[i][j].config(state=ACTIVE)
            p2.config(state=DISABLED)
            p1.config(state=ACTIVE)
            board[i][j] = 'O'
        sign += 1
        button[i][j].config(text=board[i][j])
    x = True
    if CheckWins(board, 'X'):
        gb.destroy()
        x = False
        box = messagebox.showinfo('Победа!', "Победа за Игроком")
    elif CheckWins(board, 'O'):
        gb.destroy()
        x = False
        box = messagebox.showinfo('Победа!', "Победил 'Ш'елезяка")
    elif (isfull()):
        gb.destroy()
        x = False
        box = messagebox.showinfo('Ничья', 'Ничья')
    if (x):
        if sign % 2 != 0:
            move = pc()
            button[move[0]][move[1]].config(state=DISABLED)
            get_text_pc(move[0], move[1], gb, p1, p2)


def gameboard_pc(game_board, p1, p2):
    global button
    button = []
    for i in range(3):
        m = 3 + i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text_pc, i, j, game_board, p1, p2)
            button[i][j] = Button(
                game_board, bd=8, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()



def withpc(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title('Крестики-Нолики')
    p1 = Button(game_board, text='Игрок : X', width=10)
    p1.grid(row=1, column=1)
    p2 = Button(game_board, text="'Ш'елезяка : O",
                width=10, state=DISABLED)

    p2.grid(row=2, column=1)
    gameboard_pc(game_board, p1, p2)