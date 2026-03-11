

coins = [50, 25, 20, 10, 5]

target = 40

coins_change = {}

for coin in coins:
    coins_change[coin] = 0

change = 0

while change < target:
    for coin in coins:
        if coin <= target - change:
            coins_change[coin] += 1
            change += coin
            break

print(change, coins_change)






