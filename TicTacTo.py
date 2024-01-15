def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # 가로, 세로, 대각선을 확인하여 승자를 찾습니다.
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    # 보드가 가득 찼는지 확인합니다.
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    # 초기 보드 생성
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)

        # 현재 플레이어에게 위치 입력 받기
        row = int(input(f"플레이어 {current_player}, 행을 선택하세요 (0, 1, 2): "))
        col = int(input(f"플레이어 {current_player}, 열을 선택하세요 (0, 1, 2): "))

        # 선택한 위치가 비어있는지 확인하고 비어있으면 해당 위치에 마크
        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("이미 선택된 위치입니다. 다른 위치를 선택하세요.")
            continue

        # 현재 플레이어가 이겼는지 확인
        if check_winner(board, current_player):
            print_board(board)
            print(f"플레이어 {current_player}가 이겼습니다!")
            break

        # 보드가 가득 찼는지 확인
        if is_board_full(board):
            print_board(board)
            print("무승부입니다!")
            break

        # 다음 플레이어로 변경
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
