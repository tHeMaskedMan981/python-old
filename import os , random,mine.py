import os , random

def printBoard( board, players=None, instructions=False) :
	clear_screen = os.system('cls' if os.name =='nt' else 'clear')
	if (instructions==True):
		print('welcome to tic tac toe !\n')
	else:
		print('computer - ' + players[1] + '\tplayer - ' + players[0] + '\n')

for i in xrange (1,9,3):
	print( '             |          | ')
	print( '       ' + board[i] + '|' + board[i+1] + '|' + board[i+2])
	print( '             |          | ')
	print('    ----------')

def inputPlayerLetter():
	print(' do u want to be X or O?')
	letter= raw_input().upper()
	while not (letter=='X' or letter =='O'):
		print('invalid input. do u want to be X or O?')
		letter= raw_input().upper()

	if letter =='X':
		return ['X', 'O']
	else :
		return ['O', 'X']
def toss():



	if random.randint(0,1)==0:
		return 'computer'
	else :
		return ' player'

def playAgain():
	print('do u want to play again (Y/N)')
	return not raw_input().lower().startswith('n')

def inputPlayerMove(board):

	print('whata is your next move? (1-9)')
	move = raw_input()
	while move not in ' 1 2 3 4 5 6 7 8 9' .split() or not isEmpty( board, int(move)):
		print ('invalid input! what is your next move? (1-9)')
		move=raw_input()
	return int(move)

def isEmpty(board, move):

	return board[move] ==' '

def checkWin(board, letter):

	return((board[7] == letter and board[8]== letter and board[9]==letter) or
	(board[4] == letter and board[5]== letter and board[6]==letter) or
	(board[1] == letter and board[2]== letter and board[3]==letter) or
	(board[1] == letter and board[4]== letter and board[7]==letter) or
	(board[2] == letter and board[5]== letter and board[8]==letter) or
	(board[3] == letter and board[6]== letter and board[9]==letter) or
	(board[3] == letter and board[5]== letter and board[7]==letter) or
	(board[1] == letter and board[5]== letter and board[9]==letter) )

def chooseRandomMoveFromList(board, movelList):

	possibleMoves = []
	for i in movelList:
		if isEmpty(board, i):
			possibleMoves.append(i)

	if len(possibleMoves) !=0:
		return random.choice(possibleMoves)
	else:
		return None

def getComputerMove(board, players):

	playerLetter, computerLetter = players


	for i in range(1,10):
		copyBoard = board[:]
		if isEmpty(copyBoard,i):
				copyBoard[i] = computerLetter
				if checkWin(copyBoard, computerLetter):

					return i


	for i in range(1,10):
		copyBoard = board[:]
		if isEmpty(copyBoard,i):
				copyBoard[i] = playerLetter
				if checkWin(copyBoard, playerLetter):

					return i

	move = chooseRandomMoveFromList(board, [1,3,7,9])
	if move != None:
		return move

	if isEmpty(board,5):
		return 5

	return chooseRandomMoveFromList(board, [2,4,6,8])
	
if__name__== "__main__"	:
	while  True:
		board = [' '] + '1 2 3 4 5 6 7 8 9' .split()
		printBoard(board, None, True)
		board = [' ']*10
		players=inputPlayerLetter()
		playerLetter, computerLetter = players
		turn = toss()
		print ( 'the' + turn + 'will go first. \n press ENTER to continue')	
		raw_input()
		gameOver = False

		while not gameOver:
			if turn == 'player':
				printBoard(board, players)
				move=inputPlayerMove(board)
				board[move] = playerLetter

				if checkWin(board, playerLetter):
					printBoard(board, players)
					print ( ' congratulations! YOU HAVE  won the game!')
					gameOver = True

				else: 
					if isBoardFull(board):
						printBoard(board, players)
						print (' the game is a tie!')
						break
					else : 
					    turn = 'computer'

			else:		
				move= getComputerMove(board, players)
				board[move] = computerLetter

				if checkWin(board, computerLetter):
					printBoard(board, players)
					print ( ' the computer won the game.')
					gameOver = True

				else: 
					if isBoardFull(board):
						printBoard(board, players)
						print('the game is a tie!')
						break

					else:
						turn = 'player'	
						
		if not playAgain():
			break	
