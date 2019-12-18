'''
-*- coding: utf-8 -*-
@Author  : Alex
@Time    : 2019/9/5 15:12
@Software: PyCharm
@File    : gobang.py
'''


def printBoard(checkboard):
    print('\033[1;37;41m---------简易五子棋游戏（控制台版）---------\033[0m')
    print("\033[1;30;46m--------------------------------")
    print("   1  2  3  4  5  6  7  8  9  10")
    for i in range(len(checkboard)):
        print(chr(i + ord('A')) + " ", end=" ")
        for j in range(len(checkboard[0])):
            print(checkboard[i][j] + " ", end=" ")
        print()
    print("--------------------------------\033[0m")


def check_status(checkboard, location, flagch):
    finish = False
    # 判断左方
    if location[0] >= 4:
        if (checkboard[location[0] - 1][location[1]] == flagch
                and checkboard[location[0] - 2][location[1]] == flagch
                and checkboard[location[0] - 3][location[1]] == flagch
                and checkboard[location[0] - 4][location[1]] == flagch):
            finish = True
    # 判断右方
    if location[0] + 4 <= 9:
        if (checkboard[location[0] + 1][location[1]] == flagch
                and checkboard[location[0] + 2][location[1]] == flagch
                and checkboard[location[0] + 3][location[1]] == flagch
                and checkboard[location[0] + 4][location[1]] == flagch):
            finish = True
    # 判断下方
    if location[1] + 4 <= 9:
        if (checkboard[location[0]][location[1] + 1] == flagch
                and checkboard[location[0]][location[1] + 2] == flagch
                and checkboard[location[0]][location[1] + 3] == flagch
                and checkboard[location[0]][location[1] + 4] == flagch):
            finish = True
    # 判断上方
    if location[1] - 4 >= 0:
        if (checkboard[location[0]][location[1] - 1] == flagch
                and checkboard[location[0]][location[1] - 2] == flagch
                and checkboard[location[0]][location[1] - 3] == flagch
                and checkboard[location[0]][location[1] - 4] == flagch):
            finish = True
    # 判断右上方
    if location[0] >= 4 and location[1] >= 4:
        if (checkboard[location[0] - 1][location[1] - 1] == flagch
                and checkboard[location[0] - 2][location[1] - 2] == flagch
                and checkboard[location[0] - 3][location[1] - 3] == flagch
                and checkboard[location[0] - 4][location[1] - 4] == flagch):
            finish = True
    # 判断右下方
    if location[0] >= 4 and location[1] + 4 <= 9:
        if (checkboard[location[0] - 1][location[1] + 1] == flagch
                and checkboard[location[0] - 2][location[1] + 2] == flagch
                and checkboard[location[0] - 3][location[1] + 3] == flagch
                and checkboard[location[0] - 4][location[1] + 4] == flagch):
            finish = True
    # 判断左上方
    if location[0] + 4 <= 9 and location[1] - 4 >= 0:
        if (checkboard[location[0] + 1][location[1] - 1] == flagch
                and checkboard[location[0] + 2][location[1] - 2] == flagch
                and checkboard[location[0] + 3][location[1] - 3] == flagch
                and checkboard[location[0] + 4][location[1] - 4] == flagch):
            finish = True
    # 判断左下方
    if location[0] + 4 <= 9 and location[1] + 4 <= 9:
        if (checkboard[location[0] + 1][location[1] + 1] == flagch
                and checkboard[location[0] + 2][location[1] + 2] == flagch
                and checkboard[location[0] + 3][location[1] + 3] == flagch
                and checkboard[location[0] + 4][location[1] + 4] == flagch):
            finish = True
    return finish

def do_bang(checkboard, position, flagch):
    y, x = position[:]
    if 0 <= x <= 9 and 0 <= y <= 9:
        if checkboard[x][y] == '-':
            checkboard[x][y] = flagch
        else:
            print('\033[31m******您输入位置已经有其他棋子，请重新输入！\033[0m')
            return 0
    else:
        print('\033[31m***您输入的坐标有误请重新输入！***\033[0m')
        return 0


def print_msg(checkboard, flag):
    # 输出最后胜利的棋盘
    print("\033[1;37;44m--------------------------------")
    print("   1  2  3  4  5  6  7  8  9  10")
    for i in range(len(checkboard)):
        print(chr(i + ord('A')) + " ", end=' ')
        for j in range(len(checkboard[i])):
            print(checkboard[i][j] + " ", end=' ')
        print()
    print("--------------------------------\033[0m")
    # 输出赢家
    if (flag == 1):
        print('\033[32m*棋胜利！***\033[0m')
    else:
        print('\033[32mo棋胜利！***\033[0m')


def main():
    checkboard = [["-" for _ in range(10)] for _ in range(10)]
    flag = 1
    while True:
        printBoard(checkboard)
        location = [0] * 2
        if flag == 1:
            instr = input('\033[1;37;40m请*输入棋子坐标（例如A1）：\033[0m') # 白字黑底
        else:
            instr = input('\033[1;37;40m请*输入棋子坐标（例如A1）：\033[0m') # 白字黑底
        if flag == 1:
            flagch = "*"
        else:
            flagch = "o"
        location[1] = ord(instr[0]) - 65
        location[0] = int(instr[1]) - 1
        mark = do_bang(checkboard, location, flagch)
        if mark == 0:
            continue
        if check_status(checkboard, location, flagch):
            print_msg(checkboard, flag)
            break
        flag *= -1


if __name__ == '__main__':
    main()