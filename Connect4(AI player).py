import random
import math

def generateField(nrow, ncol):
    if not isinstance(nrow, int) or not isinstance(ncol, int):
        print("Error: Both nrow and ncol must be integers.")
        return -1
    if nrow <= 0 or ncol <= 0:
        print("Error: nrow and ncol must be positive integers.")
        return -1
    field = [[" "] * ncol for _ in range(nrow)]
    return field


def drawField(field):
    if not field or not isinstance(field, list):
        print("Error: Invalid field.")
        return
    row = len(field)
    col = len(field[0])

    # Print column labels
    print("   " + "   ".join([str(i + 1) for i in range(col)]))
    print("  " + "--- " * col)

    for x in range(row):
        for y in range(col):
            print(f" {field[x][y]} ", end="")
            if y != col - 1:
                print("|", end="")
        print()
        print("  " + "--- " * col)


def doMove(current_player, field):
    if current_player == 0:  # Human player
        try:
            position = int(input(f"Player {current_player} (R), choose your column (1-{len(field[0])}): "))
        except ValueError:
            print("Error: Please enter a valid integer for the column.")
            return False

        if position < 1 or position > len(field[0]):
            print(f"Error: Column must be between 1 and {len(field[0])}.")
            return False

        j = position - 1
    else:  # AI player
        j = aiMove(field)
        print(f"Player {current_player} (Y), chooses column {j + 1}")

    i = len(field) - 1

    while i >= 0:
        if field[i][j] == " ":
            field[i][j] = "R" if current_player == 0 else "Y"
            return True
        i -= 1

    if current_player == 0:
        print("Column is full. Choose another column.")
    return False


def aiMove(field):
    _, best_column = minimax(field, 4, True, -math.inf, math.inf)
    return best_column


def minimax(field, depth, maximizing_player, alpha, beta):
    valid_columns = [j for j in range(len(field[0])) if field[0][j] == " "]
    is_terminal = checkWinningState(field) or not checkEmptySlot(field)

    if depth == 0 or is_terminal:
        if is_terminal:
            if checkWinningState(field):
                return (1000 if maximizing_player else -1000), None
            else:  # Tie
                return 0, None
        return evaluateField(field), None

    if maximizing_player:
        value = -math.inf
        best_column = random.choice(valid_columns)
        for col in valid_columns:
            temp_field = [row[:] for row in field]
            makeMove(temp_field, col, "Y")
            score, _ = minimax(temp_field, depth - 1, False, alpha, beta)
            if score > value:
                value = score
                best_column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value, best_column
    else:
        value = math.inf
        best_column = random.choice(valid_columns)
        for col in valid_columns:
            temp_field = [row[:] for row in field]
            makeMove(temp_field, col, "R")
            score, _ = minimax(temp_field, depth - 1, True, alpha, beta)
            if score < value:
                value = score
                best_column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value, best_column


def evaluateField(field):
    score = 0
    center_col = len(field[0]) // 2
    center_array = [field[i][center_col] for i in range(len(field))]
    score += center_array.count("Y") * 3

    for row in field:
        score += evaluateArray(row, "Y") - evaluateArray(row, "R")

    for col in range(len(field[0])):
        column_array = [field[i][col] for i in range(len(field))]
        score += evaluateArray(column_array, "Y") - evaluateArray(column_array, "R")

    for x in range(len(field)):
        for y in range(len(field[0])):
            score += evaluateDiagonals(field, x, y, "Y") - evaluateDiagonals(field, x, y, "R")

    return score


def evaluateArray(array, piece):
    score = 0
    for i in range(len(array) - 3):
        window = array[i:i + 4]
        if window.count(piece) == 4:
            score += 100
        elif window.count(piece) == 3 and window.count(" ") == 1:
            score += 5
        elif window.count(piece) == 2 and window.count(" ") == 2:
            score += 2
    return score


def evaluateDiagonals(field, x, y, piece):
    nrow, ncol = len(field), len(field[0])
    score = 0
    if x + 3 < nrow and y + 3 < ncol:
        window = [field[x + i][y + i] for i in range(4)]
        score += evaluateArray(window, piece)
    if x - 3 >= 0 and y + 3 < ncol:
        window = [field[x - i][y + i] for i in range(4)]
        score += evaluateArray(window, piece)
    return score


def makeMove(field, col, piece):
    for i in range(len(field) - 1, -1, -1):
        if field[i][col] == " ":
            field[i][col] = piece
            break


def movearound(field, lastMovePos):
    ncol = len(field[0])
    nrow = len(field)
    x = lastMovePos[0]
    y = lastMovePos[1]
    s = ['', '', '', '']
    for offset in range(-3, 4):
        xCurrent = x + offset
        yCurrent = y + offset
        if 0 <= xCurrent < nrow and 0 <= yCurrent < ncol:
            s[0] += field[xCurrent][yCurrent]
        xCurrent = x + offset
        yCurrent = y - offset
        if 0 <= xCurrent < nrow and 0 <= yCurrent < ncol:
            s[1] += field[xCurrent][yCurrent]
        xCurrent = x + offset
        yCurrent = y
        if 0 <= xCurrent < nrow and 0 <= yCurrent < ncol:
            s[2] += field[xCurrent][yCurrent]
        xCurrent = x
        yCurrent = y + offset
        if 0 <= xCurrent < nrow and 0 <= yCurrent < ncol:
            s[3] += field[xCurrent][yCurrent]

    for k in range(4):
        if 'RRRR' in s[k] or 'YYYY' in s[k]:
            return True
    return False


def checkWinningState(field):
    ncol = len(field[0])
    nrow = len(field)
    for y in range(ncol):
        for x in range(nrow):
            lastMovePos = [x, y]
            if movearound(field, lastMovePos):
                return True
    return False


def checkEmptySlot(field):
    for row in field:
        if " " in row:
            return True
    return False


def startGame(nrow=6, ncol=7):
    field = generateField(nrow, ncol)
    if field == -1:
        return

    drawField(field)
    current_player = 0

    while True:
        if not doMove(current_player, field):
            continue

        drawField(field)

        if checkWinningState(field):
            print(f"Player {current_player} wins!")
            break

        if not checkEmptySlot(field):
            print("The game is a tie!")
            break

        current_player = 1 - current_player


try:
    startGame()
except Exception as e:
    print(f"An unexpected error occurred: {e}")
