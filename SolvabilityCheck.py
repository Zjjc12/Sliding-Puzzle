import math
import numpy as np

def inversionCheck(array):
	inversion = 0

	#delete x from array
	for i in range(len(array)):
		if array[i] == "x":
			del (array[i])
			break
	# find inversion by looking for pair with inverted position
	for a in array:
		for b in array:
			if int(a) > int(b) and array.index(b) - array.index(a) > 0:
				#change inversion pair by 1
				inversion += 1
	return inversion


def isPuzzleSolvable(matrix):
	#convert numpy matrix to flat python list
	array = matrix.A1.tolist()

	#if n*n is even
	if math.sqrt(len(array)) % 2 == 0:
		#loop through all rows to check to see where "x" is
		for x in range (0, len(matrix)):
			#for every odd row (index starts at 0)
			if x % 2 == 0:
				#loop through columns of matrix in row x to see if "x" exist
				for y in range(0, len(matrix)):
					if (matrix[x,y] == "x"):
						#if "x" is in odd row, and inversion is odd, return true
						if (inversionCheck(array)) % 2 == 0:
							return False
						#if "x" is in odd row, and inversion is even, return false
						else:
							return True

			#for every even row
			else:
				#loop through columns of matrix in row x to see if "x" exist
				for y in range(0, len(matrix)):
					if (matrix[x, y] == "x"):
						#if x is in even row, and inversion is even, return true
						if (inversionCheck(array)) % 2 == 0:
							return True
						#if x is in even row, and inversion is odd, return false
						else:
							return False
	#if n*n is odd
	else:
		#if inversion is even, return true
		if inversionCheck(array) % 2 == 0:
			return True
		#if inversion is odd, return true
		else:
			return False




