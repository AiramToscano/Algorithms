def is_palindrome_recursive(word, low_index, high_index):
    if (word == ''):
        return False
    arrayWord = list(word)
    if (arrayWord[low_index] != arrayWord[high_index]):
        return False
    if (low_index >= high_index):
        return True
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)


# print(is_palindrome_recursive('AGUA',0,3))
