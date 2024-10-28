# Largest Number in Tuple

def max_in_tuple(numbers):
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num
    return max_number

numbers = (10, 20, 30, 40, 50)
print("Largest number in tuple:", max_in_tuple(numbers))