# Keys with Values Greater than n

def keys_with_values_greater_than(d, n):
    result = [key for key, value in d.items() if value > n]
    return result

# Test case
sample_dict = {'a': 5, 'b': 12, 'c': 3}
print("Keys with values greater than n:", keys_with_values_greater_than(sample_dict, 4))