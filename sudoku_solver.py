def is_valid(board, row, col, num):
    if num in board[row]:
        return False

    if num in [board[i][col] for i in range(9)]:
        return False
    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 25)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()

def get_sudoku_input():
    print("Enter the Sudoku board row by row. Use '0' for empty cells.")
    sudoku_board = []
    for i in range(9):
        while True:
            try:
                row = input(f"Enter row {i + 1} (e.g., 5,3,0,0,7,0,0,0,0): ").strip()
                row = list(map(int, row.split(',')))
                if len(row) != 9 or any(n < 0 or n > 9 for n in row):
                    raise ValueError("Row must contain exactly 9 numbers between 0 and 9.")
                sudoku_board.append(row)
                break
            except ValueError as e:
                print(f"Invalid input. {e}")
    return sudoku_board

print("Input Sudoku Board:")
sudoku_board = get_sudoku_input()

print("Original Sudoku Board:")
print_board(sudoku_board)

if solve_sudoku(sudoku_board):
    print("\nSolved Sudoku Board:")
    print_board(sudoku_board)
else:
    print("\nNo solution exists.")
