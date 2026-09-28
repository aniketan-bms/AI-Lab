def dfs(start, goal):
    stack = [(start, [])]
    visited = set()

    while stack:
        state, path = stack.pop()

        if state in visited:
            continue

        visited.add(state)

        if state == goal:
            return path + [state]

        zero = state.index(0)
        row = zero // 3
        col = zero % 3

        moves = []

        if row > 0:
            moves.append(zero - 3)   # Up
        if row < 2:
            moves.append(zero + 3)   # Down
        if col > 0:
            moves.append(zero - 1)   # Left
        if col < 2:
            moves.append(zero + 1)   # Right

        for move in moves:
            new_state = list(state)
            new_state[zero], new_state[move] = \
                new_state[move], new_state[zero]

            new_state = tuple(new_state)

            if new_state not in visited:
                stack.append((new_state, path + [state]))

    return None


def display(solution):
    if solution is None:
        print("No solution")
        return

    for state in solution:
        print(state[0:3])
        print(state[3:6])
        print(state[6:9])
        print()


start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

print("DFS Solution:")
solution = dfs(start, goal)
display(solution)