
def soma(lista):
    total = 0
    for x in lista:
        total += x
    return total

arr = [1,2,3,4,5,6]

print(soma(arr))

#======== recursão ======

# Caso base (mais simples):
#   1. arr com 0 elementos a soma é 0.
#   2. arr com 1 elemento a soma é o próprio elemento.

def soma_recursiva(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + soma_recursiva(arr[1:])

print('SOMA RECURSIVA: ')
print(soma_recursiva(arr))