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

    for x in range(row):
        for y in range(col):
            if y == col - 1:
                print(field[x][y], end="\n")
            else:
                print(field[x][y], end=" | ")
        print("--" * col * 2)


def doMove(current_player, field):
    try:
        position = int(input(f"Player {current_player}, choose your column (1-{len(field[0])}): "))
    except ValueError:
        print("Error: Please enter a valid integer for the column.")
        return False

    if position < 1 or position > len(field[0]):
        print(f"Error: Column must be between 1 and {len(field[0])}.")
        return False

    j = position - 1
    i = len(field) - 1

    while i >= 0:
        if field[i][j] == " ":
            field[i][j] = "R" if current_player == 0 else "Y"
            return True
        i -= 1

    print("Column is full. Choose another column.")
    return False


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
            s[0] += str(field[xCurrent][yCurrent])
        xCurrent = x + offset
        yCurrent = y - offset
        if 0 <= xCurrent < nrow and 0 <= yCurrent < ncol:
            s[1] += str(field[xCurrent][yCurrent])
        xCurrent = x + offset
        yCurrent = y
        if 0 <= xCurrent < nrow and 0 <= yCurrent < ncol:
            s[2] += str(field[xCurrent][yCurrent])
        xCurrent = x
        yCurrent = y + offset
        if 0 <= xCurrent < nrow and 0 <= yCurrent < ncol:
            s[3] += str(field[xCurrent][yCurrent])

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
