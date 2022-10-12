def is_palindrome_iterative(word):
    if (word == ''):
        return False
    arrayWord = list(word)
    tamanho = arrayWord.__len__()
    tamanhoFinal = tamanho - 1
    tamnahoInicial = 0
    for i in arrayWord:
        if (arrayWord[tamnahoInicial] != arrayWord[tamanhoFinal]):
            return False
        if (tamnahoInicial >= tamanhoFinal):
            return True
        tamnahoInicial += 1
        tamanhoFinal -= 1


# print(is_palindrome_iterative('AIRAM'))
