
# Caso base: 0 items na lista.
# Caso recursivo: mais de um item na lista.

def recursive_counter(arr):
    if len(arr) == 0:
        return 0
    else:
        return 1 + recursive_counter(arr[1:])
    
print(recursive_counter([5,7,2,328,0,-1,]))