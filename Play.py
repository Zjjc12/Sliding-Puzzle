import PuzzleGenerator as PG
import numpy as np
import curses

#ask user for puzzle size
puzzleSize= int(input("Type in the puzzle size you want and press enter. \n"))

#initialize puzzle
puzzle = PG.GeneratePuzzle(puzzleSize)

#have win?
win = False

#number of moves
moves = 0
 
# get the curses screen window
screen = curses.initscr()
 
# turn off input echoing
curses.noecho()
 
# respond to keys immediately (don't wait for enter)
curses.cbreak()
 
# map arrow keys to special values
screen.keypad(True)

#finished puzzle to check for completion
finished = []
for i in range (1, puzzleSize*puzzleSize):
	finished.append(i)
finished.append("x")

finished = np.array(finished)
#make numpy array into array in array with size of size
finished = finished.reshape(puzzleSize, puzzleSize)
#make numpy array into a numpy matrix
finishedMatrix = np.matrix(finished)


def Move(key):

	#if left is pressed
	if key == "left":
		#find where x is
		xPos = int(np.where(puzzle == "x")[1])
		yPos = int(np.where(puzzle == "x")[0])
		#if the move is not invalid
		if xPos != (len(puzzle) - 1):
			#save value in temp
			temp = puzzle[yPos, xPos + 1]
			#change value to x
			puzzle[yPos, xPos + 1] = "x"
			#change x to value
			puzzle[yPos, xPos] = temp

	#if right is pressed
	if key == "right":
		#find where x is
		xPos = int(np.where(puzzle == "x")[1])
		yPos = int(np.where(puzzle == "x")[0])
		#if the move is not invalid
		if xPos != 0:
			#save value in temp
			temp = puzzle[yPos, xPos - 1]
			#change value to x
			puzzle[yPos, xPos - 1] = "x"
			#change x to value
			puzzle[yPos, xPos] = temp

	if key == "up":
		#find where x is
		xPos = int(np.where(puzzle == "x")[1])
		yPos = int(np.where(puzzle == "x")[0])
		#if the move is not invalid
		if yPos != (len(puzzle) - 1):
			#save value in temp
			temp = puzzle[yPos + 1, xPos]
			#change value to x
			puzzle[yPos + 1, xPos] = "x"
			#change x to value
			puzzle[yPos, xPos] = temp

	if key == "down":
		#find where x is
		xPos = int(np.where(puzzle == "x")[1])
		yPos = int(np.where(puzzle == "x")[0])
		#if the move is not invalid
		if yPos != 0:
			#save value in temp
			temp = puzzle[yPos - 1, xPos]
			#change value to x
			puzzle[yPos - 1, xPos] = "x"
			#change x to value
			puzzle[yPos, xPos] = temp

screen.addstr (str(puzzle))
try:
	while True:

		char = screen.getch()
		#press q to quit
		if char == ord('q'):
			break

		#if right is pressed
		elif char == curses.KEY_RIGHT:
			#add 1 more move
			moves += 1
			#clear screen
			screen.clear()

			#move right
			Move("right")
			#reprint the puzzle
			screen.addstr (str(puzzle))

		#if left is pressed
		elif char == curses.KEY_LEFT:
			#add 1 more move
			moves += 1
			#clear screen
			screen.clear()
			
			#move left
			Move("left")
			#reprint the puzzle
			screen.addstr (str(puzzle))

		#if up is pressed    
		elif char == curses.KEY_UP:
			#add 1 more move
			moves += 1
			#clear screen
			screen.clear()
			
			#move up
			Move("up")
			#reprint the puzzle
			screen.addstr (str(puzzle))

		#if down is pressed    
		elif char == curses.KEY_DOWN:
			#add 1 more move
			moves += 1
			#clear screen
			screen.clear()

			#move down
			Move("down")
			#reprint the puzzle
			screen.addstr (str(puzzle))
		if np.array_equal(puzzle.A1, finishedMatrix.A1):
			win = True
			break


finally:
	# shut down cleanly
	curses.nocbreak(); screen.keypad(0); curses.echo()
	curses.endwin()

if win == True:
	print(chr(27) + "[2J")
	print("YOU WON!!!")
else:
	print(chr(27) + "[2J")
	print("Dont be a quiter...")


