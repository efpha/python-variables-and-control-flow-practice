# Returning sum of all the numbers in the list

nums = [1, 2, 3, 4, 5]
def getSum(arr):
    sum = 0
    for x in arr:
        sum += arr[x - 1]
    return sum
    
print("Sum of list:", getSum(nums))
