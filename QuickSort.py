
# "low" = beginning index of the array/sub-array
# "high" = end index of the array/sub-array
def DoPartition(array, low, high):

  # I picked the right-most element as pivot (you can pick any)
  pivot = array[high]

  # leftPartition keeps track of the location where the next element
  #       that's smaller than the pivot will be placed.
  leftPartition = low

  for index in range (low, high):
    # If an element is LESS than or EQUAL to pivot
    if (array[index] <= pivot):
      # Move the element to the left partition (leftPartition)
      array[leftPartition], array[index] = array[index], array[leftPartition]
      # Increment leftPartition by 1, since the current leftPartition
      #       just got filled
      leftPartition = leftPartition + 1
  
  # After all the smaller items are places on the left partition, we
  #       move the pivot (array[high]) to the 
  #       middle (right next to the last left partition)
  array[leftPartition], array[high] = array[high], array[leftPartition]

  # Return the pivot location so that the array can be split in two for the next
  #       round of recursion calls
  return (leftPartition)

def quickSort (array, low, high):

        if(low < high):

                # Receive the pivot location
                PartitionIndex = DoPartition(array, low, high)

                # Split the array in two halves and call quickSort() on both halves
                quickSort(array, low, PartitionIndex-1)
                quickSort(array, PartitionIndex+1, high)

def main():

    TestArray = [3,11,98,56,20,19,4,45,88,30,7,7,7,8,8] 
    quickSort(TestArray, 0, len(TestArray)-1)

    print ("The sorted result is:") 
    for i in range(len(TestArray)): 
        print ("%d" %TestArray[i])


if __name__ == '__main__':
    main()
    
    