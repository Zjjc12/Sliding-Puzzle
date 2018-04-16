import SolvabilityCheck as SC
import random
import numpy as np

def GeneratePuzzle(size):
	#start off as unsolvable
	isSolvable = False

	#number of elements in the matrix
	numInArray = size**2

	#create array
	while isSolvable == False:
		#create an empty list with size square of the size. Ie. 4^2 = 16
		array = [None] * numInArray
		#place x in random location
		array[random.randint(0, numInArray -1)] = "x"

		#Add number to list to make sure no number appear twice
		#list of used number
		used = []
		#generate the rest of the numbers
		for a, index in zip(array, range(len(array))):
			#if it is not "x"
			if (a != "x"):
				#while it is not changed yet
				while a == None:
					#random number

					randomNum = random.randint(1, numInArray)
					#check to see if the random number is used
					if randomNum not in used:
						array[index] = randomNum
						used.append(randomNum)
						break
		#make array into numpy array
		array = np.array(array)
		#make numpy array into array in array with size of size
		array = array.reshape(size, size)
		#make numpy array into a numpy matrix
		matrix = np.matrix(array)
		# check to see if puzzle is solvable
		if SC.isPuzzleSolvable(matrix) == True:
			# if solvable, return puzzle, if not repeat
			isSolvable = True
	#return matrix
	return matrix
			
#IDEAS:
	#invert a number if not solvable (change inversion)
	#random index in a list of unused numbers
	
	
print (GeneratePuzzle(4))

	

	