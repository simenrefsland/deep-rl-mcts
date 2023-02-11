from statemanager.hexstatemanager import HexStateManager
from statemanager.hexboarddisplay import HexBoardDisplay

if __name__ == "__main__":
    board = HexStateManager(6)
    board_display = HexBoardDisplay()

    i = 0
    player = (1, 0)
    while board.check_winning_state(player) is False:
        player = (1, 0) if i % 2 == 0 else (0, 1)
        move = board.make_random_move(player)
        i += 1
        board_display.visualize(
            board.convert_to_diamond_shape(), delay=0.5, newest_move=move)

    board_display.visualize(
        board.convert_to_diamond_shape(), winner=player)
