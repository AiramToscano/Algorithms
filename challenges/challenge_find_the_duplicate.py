

def find_duplicate(nums):
    try:
        return duplicate(nums)
    except Exception:
        return False


def duplicate(nums):
    nums.sort()
    for index, i in enumerate(nums):
        if (int(i) < 1):
            return False
        if (nums[index] == nums[index + 1]):
            return nums[index]
    return False

# print(find_duplicate([1, 3, 4, 100, 2, 2]))
