# Reverse Strings in List

def reverse_strings(strings):
    return [s[::-1] for s in strings]

# Test case
strings = ["apple", "banana", "cherry"]
print("Reversed strings:", reverse_strings(strings))