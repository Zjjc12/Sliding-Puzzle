import math
import numpy as np

def inversionCheck(array):
	inversion = 0
	for i in range(len(array)):
		if array[i] == "x":
			del (array[i])
			break;
	for x in array:
		if (int(x) - (array.index(x) + 1)) > 0:
			inversion += int(x) - (array.index(x) + 1)
	return inversion


def isPuzzlePossible(matrix):
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

matrix = np.matrix([[3, 9, 1, 15], [14, 11, 4, 6], [13, "x", 10, 12], [2, 7, 8, 5]])

print (matrix)
print ("Inversions:", inversionCheck (matrix.A1.tolist()))
print("This puzzle's solvability:", isPuzzlePossible(matrix))
