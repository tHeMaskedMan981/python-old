import os, random
 
def printBoard(board,  players=None, instructions=False):
    # This function prints out the board that it was passed.
    clear_screen = os.system('cls' if os.name == 'nt' else 'clear')
 
    # If instructions are to be displayed
    if (instructions == True):
        print('Welcome to Tic Tac Toe!\n')
    else:
        print('Computer - ' + players[1] + '\tPlayer - ' + players[0] + '\n')
 
    # "board" is a list of 10 characters representing the board (ignore index 0)
    for i in xrange (1,9,3):
        print('       |   |')
        print('     ' + board[i] + ' | ' + board[i+1] + ' | ' + board[i+2])
        print('       |   |')
        print('    -----------')
 
def inputPlayerLetter():
    # Assigns X or O for player letter. Return list with [playerLetter,computerLetter]
    print('Do you want to be X or O?')
    letter = raw_input().upper()
    while not (letter == 'X' or letter == 'O'):
        print('Invalid input. Do you want to be X or O?')
        letter = raw_input().upper()
 
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
 
def toss():
    # Toss to find who goes first, computer or player.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'
 
def playAgain():
    # Returns whether user wants to continue playing.
    print('Do you want to play again? (Y/N)')
    return not raw_input().lower().startswith('n')
 
def inputPlayerMove(board):
    # Let the player type in his move.
    print('What is your next move? (1-9)')
    move = raw_input()
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isEmpty(board, int(move)):
        print('Invalid input! What is your next move? (1-9)')
        move = raw_input()
    return int(move)
 
def isBoardFull(board):
    # Return True if every space on board (except index 0) is non-empty.
    for i in range(1, 10):
        if isEmpty(board, i):
            return False
    return True
 
def isEmpty(board, move):
    # Return True if the passed move index in board list is empty.
    return board[move] == ' '
 
def checkWin(board, letter):
    # Returns True if three continuous letters found on board.
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or # bottom row
    (board[4] == letter and board[5] == letter and board[6] == letter) or # middle row
    (board[1] == letter and board[2] == letter and board[3] == letter) or # top row
    (board[1] == letter and board[4] == letter and board[7] == letter) or # left column
    (board[2] == letter and board[5] == letter and board[8] == letter) or # middle column
    (board[3] == letter and board[6] == letter and board[9] == letter) or # right column
    (board[3] == letter and board[5] == letter and board[7] == letter) or # left diagonal
    (board[1] == letter and board[5] == letter and board[9] == letter)) # right diagonal
 
def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isEmpty(board, i):
            possibleMoves.append(i)
 
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
 
def getComputerMove(board, players):
    # Given a board and the computer's letter, determine where to move and return that move.
    playerLetter, computerLetter = players
 
    # Tic Tac Toe AI:
    # Win: Check if computer can win on next move
    for i in range(1, 10):
        copyBoard = board[:]
        if isEmpty(copyBoard, i):
            copyBoard[i] = computerLetter
            if checkWin(copyBoard, computerLetter):
                return i
 
    # Block: Check if the player could win on next move
    for i in range(1, 10):
        copyBoard = board[:]
        if isEmpty(copyBoard, i):
            copyBoard[i] = playerLetter
            if checkWin(copyBoard, playerLetter):
                return i
 
    # Random moves
    # Choose a random free corner
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
 
    # Choose center if free
    if isEmpty(board, 5):
        return 5
 
    # Choose random free edge centre
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])
 
if __name__ == "__main__":
    while True:
        board = [' '] + '1 2 3 4 5 6 7 8 9'.split()
        printBoard(board, None, True)
        board = [' '] * 10
        players = inputPlayerLetter()
        playerLetter, computerLetter = players
        turn = toss()
        print('The ' + turn + ' will go first. \nPress ENTER to continue.')
        raw_input()
        gameOver = False
 
        while not gameOver:
            if turn == 'player':
                printBoard(board, players)
                move = inputPlayerMove(board)
                board[move] = playerLetter
 
                if checkWin(board, playerLetter):
                    printBoard(board, players)
                    print('Congratulations! You have won the game!')
                    gameOver = True
                else:
                    if isBoardFull(board):
                        printBoard(board, players)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'computer'
 
            else:
                move = getComputerMove(board, players)
                board[move] = computerLetter
 
                if checkWin(board, computerLetter):
                    printBoard(board, players)
                    print('The computer won the game.')
                    gameOver = True
                else:
                    if isBoardFull(board):
                        printBoard(board, players)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'player'
 
        if not playAgain():
            break