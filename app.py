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

_board_cells = [f'{str(x)} ' for x in range(9)]
_game_status = True
_result = None


def print_board():
    print(_board.format(_board_cells[0], _board_cells[1], _board_cells[2],
                        _board_cells[3], _board_cells[4], _board_cells[5],
                        _board_cells[6], _board_cells[7], _board_cells[8]))


def check_cell(cell):
    return cell in _board


def mark_cell(player_input, player):
    if player == '1':
        _board_cells[player_input] = "X "
    elif player == '2':
        _board_cells[player_input] = "O "


def check_board(winner, turn):
    if _board_cells[0] == _board_cells[1] == _board_cells[2]:
        print(f"Player {winner} is the winner!")
        exit(0)
    elif _board_cells[3] == _board_cells[4] == _board_cells[5]:
        print(f"Player {winner} is the winner!")
        exit(0)
    elif _board_cells[6] == _board_cells[7] == _board_cells[8]:
        print(f"Player {winner} is the winner!")
        exit(0)
    elif _board_cells[0] == _board_cells[3] == _board_cells[6]:
        print(f"Player {winner} is the winner!")
        exit(0)
    elif _board_cells[1] == _board_cells[4] == _board_cells[7]:
        print(f"Player {winner} is the winner!")
        exit(0)
    elif _board_cells[2] == _board_cells[5] == _board_cells[8]:
        print(f"Player {winner} is the winner!")
        exit(0)
    elif _board_cells[0] == _board_cells[4] == _board_cells[8]:
        print(f"Player {winner} is the winner!")
        exit(0)
    elif _board_cells[2] == _board_cells[4] == _board_cells[6]:
        print(f"Player {winner} is the winner!")
        exit(0)
    elif turn == 9:
        print("Draww")
        exit(0)


def main():
    _player = '1'
    _turn = 1
    print_board()
    print("\n")
    while True:
        player_input = input(f"Player {_player} turn: ")
        if player_input_validated := check_cell(str(player_input)):
            print(player_input)
            mark_cell(int(player_input), _player)
            print_board()
            check_board(_player, _turn)
            _turn += 1
            print(_turn)
            _player = '2' if _player == '1' else '1'
        else:
            print("Please chose a correct cell")


if __name__ == '__main__':
    main()
