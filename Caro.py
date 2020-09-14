from random import randint

board = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def check_line(ch, x1, x2, x3):
    if board[x1] == ch and board[x2] == ch and board[x3] == ch:
        return True
    return False


def check_all(ch):
    if check_line(ch, 0, 1, 2):
        return True
    if check_line(ch, 3, 4, 5):
        return True
    if check_line(ch, 6, 7, 8):
        return True
    if check_line(ch, 0, 4, 8):
        return True
    if check_line(ch, 6, 4, 2):
        return True
    if check_line(ch, 1, 4, 7):
        return True
    if check_line(ch, 0, 3, 6):
        return True
    if check_line(ch, 2, 5, 8):
        return True

    return False


def con_o_trong():
    for x in range(0, 9):
        if board[x] != ' x ' and board[x] != ' o ':
            return True


def print_1(x1, x2, x3):
    print(board[x1], '|', board[x2], '|', board[x3], '|')
    print('--------------')


def show():
    print_1(0, 1, 2)
    print_1(3, 4, 5)
    print_1(6, 7, 8)


show()


win = 0
while con_o_trong():
    cell = int(input(" o nay da bi chiem  :"))
    if (board[cell] == 'x' or board[cell] == 'o'):
        print('o nay da bi chiem ')
    else:
        board[cell] = 'x'
        while con_o_trong:
            computer = randint(0, 8)
            if board[computer] == 'x' or board[computer] == 'o':
                pass
            else:
                board[computer] = 'o'
                break
    show()
    if check_all('x'):
        win = 'You'
        break
    if check_all('o'):
        win = 'Computer'
        break
if win == 0:
    print('hoa ca lang')
else:
    print(win, 'win')
