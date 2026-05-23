def second_largest(arr):
    largest = float('-inf')
    second = float('-inf')

    for num in arr:
        if num > largest:
            second = largest
            largest = num

        elif num > second and num != largest:
            second = num

    if second == float('-inf'):
        return -1

    return second

print(second_largest([3, 1, 4, 1, 5, 9, 2, 6]))   
print(second_largest([10, 10, 10]))               
print(second_largest([5, 3]))                     
print(second_largest([-1, -2, -3]))               