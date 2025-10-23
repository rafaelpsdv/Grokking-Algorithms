
def fat(x):
    if x == 1:
        return 1
    else:
        return x * fat(x-1)
    
def fato(x):
    fator = 1
    for i in range (x, 0, -1):
        fator = fator * i
    return fator

print(fat(3))