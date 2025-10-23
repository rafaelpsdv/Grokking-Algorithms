
# Caso base: valor correto
# Caso recursivo 1: se valor menor que palpite, ponteiro maior é um índice antes do índice do palpite.
# Caso recursivo 2: se valor maior que palpite, ponteiro menor é um índice após índice do palpite.

def binary_search(value, arr, l_pointer, r_pointer):
    idx_middle = (r_pointer + l_pointer) // 2
    guess = arr[idx_middle]

    if l_pointer > r_pointer:
        return None
    if value == guess:
        return idx_middle
    if value < guess:
        return binary_search(value, arr, l_pointer, idx_middle - 1)       
    else:
        return binary_search(value, arr, idx_middle + 1, r_pointer)       

lista = [1,5,32,33,37,42,51,66,67,69,70]

print(binary_search(51, lista, 0, len(lista) - 1))


