# BOTTOM-UP
def rec_coin_dp2(target, coins):
    min_coins = [target + 1] * (target + 1)
    min_coins[0] = 0

    for change in range(1, target + 1):
        for coin in coins:
            if coin <= change:
                min_coins[change] = min(
                    1 + min_coins[change - coin], min_coins[change])

    return min_coins[target]


# TOP-DOWN
def rec_coin(target, coins):
    min_coins = target

    if target in coins:
        return 1

    for i in [c for c in coins if c <= target]:
        num_coins = 1 + rec_coin(target - i, coins)
        if num_coins < min_coins:
            min_coins = num_coins

    return min_coins


# TOP-DOWN
def rec_coin_dp(target, coins, known_results=None):
    if known_results == None:
        known_results = [0] * (target + 1)

    min_coins = target

    if target in coins:
        known_results[target] = 1
        return 1

    if known_results[target] > 0:
        return known_results[target]

    for i in [c for c in coins if c <= target]:
        num_coins = 1 + rec_coin_dp(target-i, coins, known_results)
        if num_coins < min_coins:
            min_coins = num_coins
            known_results[target] = min_coins

    return min_coins


# print('O/P : ', rec_coin_dp2(75, [1, 5, 10, 25]))
# print('O/P : ', rec_coin(75, [1, 5, 10, 25]))
print('O/P : ', rec_coin_dp(75, [1, 5, 10, 25]))
