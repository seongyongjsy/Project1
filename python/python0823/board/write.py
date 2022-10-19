board_list = []

def write_board(new_board):
    global board_list
    board_list.append(new_board)

class Board:
    def __init__(self, board_num, board_title, board_writer):
        self.board_num = board_num
        self.board_title = board_title
        self.board_writer = board_writer

        def __repr__(self):
            return f"{self.board_num}-{self.board_title}/{self.board_writer}"