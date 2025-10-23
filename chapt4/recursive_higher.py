

# Caso base: 1 item na lista -> próprio valor
# Caso recursivo: 

# [5, 4, 2, 1, 7] -> [1, 7] -> [2] [7] -> 


def recursive_higher(arr):
    if len(arr) == 1:
        return arr[0]

    return max(arr[0],recursive_higher(arr[1:]))

print(recursive_higher([1,7,5,2,9,3,12,-1,7]))