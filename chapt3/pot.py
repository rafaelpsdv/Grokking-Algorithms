class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        elif n % 2 != 0 or n <= 0:
            return False
        else:
            return self.isPowerOfTwo(n/2)


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        elif n % 3 != 0 or n <= 0:
            return False
        else:
            return self.isPowerOfThree(n/3)




def isPowerOf(n: int, base: int) -> bool:
    if n == 1:
        return True
    elif n % base != 0 or n <= 0:
        return False
    else:
        return isPowerOf(n/base, base)
        

teste = isPowerOf(n=32, base=2)

print(teste)