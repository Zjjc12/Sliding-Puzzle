import PuzzleGenerator as PG
import numpy as np
import curses

#set puzzle size
puzzleSize = 4

#initialize puzzle
puzzle = PG.GeneratePuzzle(puzzleSize)

#game state
gameState = True

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





			screen.addstr (str(puzzle))

		#if left is pressed
		elif char == curses.KEY_LEFT:
			#add 1 more move
			moves += 1
			#clear screen
			screen.clear()
			

		#if up is pressed    
		elif char == curses.KEY_UP:
			#add 1 more move
			moves += 1
			#clear screen
			screen.clear()
			

		#if down is pressed    
		elif char == curses.KEY_DOWN:
			#add 1 more move
			moves += 1
			#clear screen
			screen.clear()

finally:
	# shut down cleanly
	curses.nocbreak(); screen.keypad(0); curses.echo()
	curses.endwin()


print("YOU WON!!")
