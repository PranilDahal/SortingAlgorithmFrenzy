# Python code for Bubble Sort
def BubbleSort(array):
    	
    # Highest we can go in the array
	maxPosition = len(array) - 1
	# Iterate through the array
	for x in range(maxPosition):
		# For every iteration, we get ONE sorted element.
		# After x iterations, we have x sorted elements
		# We don't swap on the sorted side - only go up to (maxPosition-x)
		for y in range(0,maxPosition - x):
			# If an element is greater than the element after it, swap places
			if array[y] > array[y+1]:
    				array[y], array[y+1] = array[y+1], array[y]
					#Done! 


def main():

    TestArray = [3,11,98,56,20,19,4,45,88,30,7,7,7,8,8] 
    BubbleSort(TestArray)

    print ("#LetsCodeNepal: The bubble sorted result is-") 
    for i in range(len(TestArray)): 
        print ("%d" %TestArray[i])


if __name__ == '__main__':
    main()