"""
Напишите игру "Крестики-нолики".
"""


def draw_board(board):
    """
    отрисовка поля.
    """
    print('     |     |')
    print('  ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9])
    print('  7  |  8  |  9 ')
    print('_____|_____|_____')
    print('     |     |')
    print('  ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6])
    print('  4  |  5  |  6 ')
    print('_____|_____|_____')
    print('     |     |')
    print('  ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3])
    print('  1  |  2  |  3 ')
    print('     |     |')
  
def is_winner(board, player):
    """
    проверка победителя.
    """
    return ((board[7] == player and board[8] == player and board[9] == player) or
            (board[4] == player and board[5] == player and board[6] == player) or
            (board[1] == player and board[2] == player and board[3] == player) or
            (board[7] == player and board[4] == player and board[1] == player) or
            (board[8] == player and board[5] == player and board[2] == player) or
            (board[9] == player and board[6] == player and board[3] == player) or
            (board[7] == player and board[5] == player and board[3] == player) or
            (board[9] == player and board[5] == player and board[1] == player))

def is_board_full(board):
    """
    заполнено ли игровое поле.
    """
    return all(x != ' ' for x in board.values())

def get_player_move(board, player):
    """
    запрашиваем у игрока номер клетки
    """
    while True:
        move = input(f'Игрок {player}, введите номер клетки (1-9): ')
        if move.isdigit():
            move = int(move)
            if move in board.keys() and board[move] == ' ':
                return move
        print('Неправильный ход. Попробуйте еще раз.')

def play_game():
    """
    апуск игры "Крестики-нолики".
    """
    board = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
    draw_board(board)
    current_player = 'X'
    while True:
        move = get_player_move(board, current_player)
        board[move] = current_player
        draw_board(board)
        if is_winner(board, current_player):
            print(f'Игрок {current_player} победил!')
            break
        if is_board_full(board):
            print('Ничья!')
            break
        current_player = 'O' if current_player == 'X' else 'X'

play_game()