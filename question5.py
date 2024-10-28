# Print Keys with Even Values

def keys_with_even_values(d):
    for key, value in d.items():
        if value % 2 == 0:
            print(key)

# Test case
sample_dict = {'a': 2, 'b': 3, 'c': 4}
keys_with_even_values(sample_dict)