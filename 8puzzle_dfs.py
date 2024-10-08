from collections import deque
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
                
def generate_moves(state):
    x, y = find_blank(state)
    moves = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            moves.append(new_state)
    return moves
    
def bfs(initial_state, goal_state):
    visited = set()
    queue = deque([(initial_state, [])])
    while queue:
        state, path = queue.popleft()
        visited.add(tuple(map(tuple, state)))
        if state == goal_state:
            return path
        for next_state in generate_moves(state):
            if tuple(map(tuple, next_state)) not in visited:
                queue.append((next_state, path + [next_state]))
    return None

def dfs(initial_state, goal_state):
    visited = set()
    stack = [(initial_state, [])]
    while stack:
        state, path = stack.pop()
        visited.add(tuple(map(tuple, state)))
        if state == goal_state:
            return path
        for next_state in generate_moves(state):
            if tuple(map(tuple, next_state)) not in visited:
                stack.append((next_state, path + [next_state]))
    return None

def print_solution(solution):
    if solution:
        for step, state in enumerate(solution):
            print(f"Step {step + 1}:")
            for row in state:
                print(row)
            print()
    else:
        print("No solution found.")

initial_state = [[1, 2, 3],
                 [4, 7, 5],
                 [6, 0, 8]]

goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

print("Solving using BFS:")
bfs_solution = bfs(initial_state, goal_state)
if bfs_solution:
    print("BFS Solution found in", len(bfs_solution), "steps.")
    print_solution(bfs_solution)
else:
    print("No solution found using BFS.")
print("Solving using DFS:")
dfs_solution = dfs(initial_state, goal_state)
if dfs_solution:
    print("DFS Solution found in", len(dfs_solution), "steps.")
    print_solution(dfs_solution)
else:
    print("No solution found using DFS.")
