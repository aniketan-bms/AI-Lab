def dls(state, goal, depth, path):

    if state == goal:
        return path

    if depth == 0:
        return None

    zero = state.index(0)
    row = zero // 3
    col = zero % 3

    moves = []

    if row > 0:
        moves.append(zero - 3)

    if row < 2:
        moves.append(zero + 3)

    if col > 0:
        moves.append(zero - 1)

    if col < 2:
        moves.append(zero + 1)

    for move in moves:

        new_state = list(state)
        new_state[zero], new_state[move] = \
            new_state[move], new_state[zero]

        new_state = tuple(new_state)

        if new_state not in path:
            result = dls(
                new_state,
                goal,
                depth - 1,
                path + [new_state]
            )

            if result:
                return result

    return None


def ids(start, goal):

    depth = 0

    while True:
        result = dls(start, goal, depth, [start])

        if result:
            return result

        depth += 1


def display(solution):

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

print("IDS Solution:")
solution = ids(start, goal)
display(solution)