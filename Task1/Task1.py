

coins = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount):
    result = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count

    return result


def find_min_coins(amount):
    min_coins = [float('inf')] * (amount + 1)
    coin_used = [0] * (amount + 1)

    min_coins[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                if min_coins[i - coin] + 1 < min_coins[i]:
                    min_coins[i] = min_coins[i - coin] + 1
                    coin_used[i] = coin

    result = {}
    current_amount = amount

    while current_amount > 0:
        coin = coin_used[current_amount]

        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1

        current_amount -= coin

    return dict(sorted(result.items()))


def main():
    amount = 113

    print("Жадібний алгоритм:")
    print(find_coins_greedy(amount))

    print("\nДинамічне програмування:")
    print(find_min_coins(amount))


if __name__ == "__main__":
    main()