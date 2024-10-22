import random

def calculate_conflicts(board):
    n = len(board)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def generate_neighbors(board):
    neighbors = []
    for col in range(len(board)):
        for row in range(len(board)):
            if row != board[col]:
                new_board = board[:]
                new_board[col] = row
                neighbors.append(new_board)
    return neighbors

def print_board(board):
    n = len(board)
    for row in range(n):
        line = ""
        for col in range(n):
            line += "Q " if board[col] == row else ". "
        print(line)
    print()

def hill_climbing(n):
    board = [random.randint(0, n - 1) for _ in range(n)]
    current_conflicts = calculate_conflicts(board)
    print("Initial board:")
    print_board(board)
    print(f"Conflicts: {current_conflicts}")
    
    while True:
        neighbors = generate_neighbors(board)
        next_board = None
        next_conflicts = current_conflicts
        for neighbor in neighbors:
            neighbor_conflicts = calculate_conflicts(neighbor)
            if neighbor_conflicts < next_conflicts:
                next_board = neighbor
                next_conflicts = neighbor_conflicts
        if next_board is None or next_conflicts == 0:
            break
        print("Current board:")
        print_board(board)
        print(f"Conflicts: {current_conflicts}")
        print("Best neighbor:")
        print_board(next_board)
        print(f"Conflicts: {next_conflicts}")
        board = next_board
        current_conflicts = next_conflicts
    print("Final board:")
    print_board(board)
    print(f"Conflicts: {current_conflicts}")
    return board, current_conflicts

n = 4
solution, conflicts = hill_climbing(n)
print("Solution:", solution)
print("Conflicts:", conflicts)
