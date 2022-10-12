def find_duplicate(nums):
    try:
        return duplicate(nums)
    except Exception:
        return False


def duplicate(nums):
    maior = []
    arrayOrd = sorted(nums)
    for i in arrayOrd:
        if (int(i) < 1):
            return False
        if (arrayOrd.count(i) > 1 and i not in maior):
            maior.append(i)
    return maior[0]


# print(find_duplicate([1, 3, 4, 2, 2, 2]))
