_board = """
      |      |
  {0}  |  {1}  |  {2}
 ____ | ____ | ____
      |      |
  {3}  |  {4}  |  {5}
 ____ | ____ | ____
      |      |
  {6}  |  {7}  |  {8}
      |      |
"""

_board_cells = [str(x) + ' ' for x in range(9)]
_game_status = True
_result = None


def print_board():
    print(_board.format(_board_cells[0], _board_cells[1], _board_cells[2],
                        _board_cells[3], _board_cells[4], _board_cells[5],
                        _board_cells[6], _board_cells[7], _board_cells[8]))


def check_cell(cell):
    if cell not in _board:
        return False
    else:
        return True


def mark_cell(player_input, player):
    if player == '1':
        _board_cells[player_input] = "X "
    elif player == '2':
        _board_cells[player_input] = "O "


def check_board(winner, turn):
    if _board_cells[0] == _board_cells[1] == _board_cells[2]:
        print("Player {} is the winner!".format(winner))
        exit(0)
    elif _board_cells[3] == _board_cells[4] == _board_cells[5]:
        print("Player {} is the winner!".format(winner))
        exit(0)
    elif _board_cells[6] == _board_cells[7] == _board_cells[8]:
        print("Player {} is the winner!".format(winner))
        exit(0)
    elif _board_cells[0] == _board_cells[3] == _board_cells[6]:
        print("Player {} is the winner!".format(winner))
        exit(0)
    elif _board_cells[1] == _board_cells[4] == _board_cells[7]:
        print("Player {} is the winner!".format(winner))
        exit(0)
    elif _board_cells[2] == _board_cells[5] == _board_cells[8]:
        print("Player {} is the winner!".format(winner))
        exit(0)
    elif _board_cells[0] == _board_cells[4] == _board_cells[8]:
        print("Player {} is the winner!".format(winner))
        exit(0)
    elif _board_cells[2] == _board_cells[4] == _board_cells[6]:
        print("Player {} is the winner!".format(winner))
        exit(0)
    else:
        if turn == 9:
            print("Draww")
            exit(0)


def main():
    _player = '1'
    _turn = 1
    print_board()
    print("\n")
    while True:
        player_input = input("Player {} turn: ".format(_player))
        player_input_validated = check_cell(str(player_input))
        if not player_input_validated:
            print("Please chose a correct cell")
        else:
            print(player_input)
            mark_cell(int(player_input), _player)
            print_board()
            check_board(_player, _turn)
            _turn += 1
            print(_turn)
            if _player == '1':
                _player = '2'
            else:
                _player = '1'


if __name__ == '__main__':
    main()
