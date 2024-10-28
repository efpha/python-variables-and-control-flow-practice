#  Two Sum Problem

def two_sum(lst, target):
    seen = set()
    for num in lst:
        if target - num in seen:
            return True
        seen.add(num)
    return False

# Test case
nums = [1, 3, 5, 7]
target = 8
print("Two sum result:", two_sum(nums, target))