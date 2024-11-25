def best_time_one(prices):
    left, right = 0, 1
    max_profit = 0
    while right < len(prices):
        if prices[right] > prices[left]:
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
        else:
            left = right
        right += 1
    return max_profit


def main():
    prices = [7, 1, 5, 3, 6, 4]
    print(best_time_one(prices)) # Output: 5


if __name__ == '__main__':
    main()
