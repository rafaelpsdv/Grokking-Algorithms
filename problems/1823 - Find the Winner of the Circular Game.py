

def findTheWinner(n: int, k: int, act:int = 0, circle:list = []) -> int:
    if len(circle) == 0:
        circle = [i for i in range(1, n + 1)]

    if n == 1:
        return circle[0]

    loser = (act + k - 1) % n

    circle.pop(loser)
    act = loser % n
    
    print(circle)

    return findTheWinner(n-1, k, act, circle)


findTheWinner(6, 5)
        