from array import array

# Caso base: array vazio ou com único elemento são o caso base.
# Caso recursivo: array com mais de um elemento.

def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        
        left = []
        right = []

        for item in arr[1:]:
            if item > pivot:
                right.append(item)
            else:
                left.append(item)
        
        return quicksort(left) + [pivot] + quicksort(right)
        
arr = [8,2,7,22,1,32,3,12,21]

print(quicksort(arr))

