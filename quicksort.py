#import random

#Uncomment to use the example
#numbers = []
#for i in range(9):
   #numbers.append(random.randint(1,100));

def quicksort(arr):
    if (len(arr) == 0):
        return arr
    pivot = arr[0]
    del arr[0]
    left = []
    right = []

    for element in arr:
        if (element < pivot):
            left.append(element)
        else:
            right.append(element)

    left = quicksort(left)
    right = quicksort(right)

    left.append(pivot)

    return left + right
    

#numbers = quicksort(numbers)
#print(numbers)
