def pboard(board):
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")
    print("---+---+---")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("---+---+---")
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
def checkwin(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player: return True
        if board[0][i] == board[1][i] == board[2][i] == player: return True
        if board[0][0] == board[1][1] == board[2][2] == player: return True
        if board[0][2] == board[1][1] == board[2][0] == player: return True
    return False
def checkdraw(board):
    for x in board:
        if " " in x: return False
    return True
def boyi(board, depth, is_maximizing, a, b):
    if checkwin(board, "O"): return 10 - depth
    if checkwin(board, "1"): return depth - 10
    if checkdraw(board): return 0

    if is_maximizing:
        max_eval = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval_score = boyi(board, depth + 1, False, a, b)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval_score)
                    a = max(a, eval_score)
                    if b <= a: break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "1"
                    eval_score = boyi(board, depth + 1, True, a, b)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval_score)
                    b = min(b, eval_score)
                    if b <= a: break
        return min_eval
def find_best_move(board):
    best_score = -float('inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = boyi(board, 0, False, -float('inf'), float('inf'))
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move
board = [[" " for i in range(3)] for i in range(3)]
print("你是1，AI是O。")
print("输入 1-9 选择位置：")
print(" 7 | 8 | 9 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 1 | 2 | 3 \n")
while True:
    pboard(board)
    try:
        choice = int(input("轮到你下棋(1-9):"))
        if choice < 1 or choice > 9:
            print("请输入1-9")
            continue
        row = (choice - 1) // 3
        col = (choice - 1) % 3

        if board[row][col] != " ":
            print("这里已经被占了")
            continue
        board[row][col] = "1"
        if checkdraw(board):
            pboard(board)
            print("ai放水了")
            break
        airow, aicol = find_best_move(board)
        board[airow][aicol] = "O"
        if checkwin(board, "O"):
            pboard(board)
            print("菜就多练")
            break
        if checkdraw(board):
            pboard(board)
            print("ai放水了")
            break

    except ValueError:
        print("请输入数字")