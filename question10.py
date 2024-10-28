#  List of Tuples to Dictionary

def tuples_to_dict(tuples_list):
    return {key: value for key, value in tuples_list}

# Test case
tuples_list = [("apple", 5), ("banana", 7), ("cherry", 3)]
print("Converted dictionary:", tuples_to_dict(tuples_list))