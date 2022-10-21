def sumOfArray(array):
    sum = 0
    for i in array:
	    sum = sum + i
    return(sum)

arr = [15, 5, 10, 23]
n = len(arr)
ans = sumOfArray(arr)

print('Sum of Numbers in an Array is', ans)
