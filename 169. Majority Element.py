def majority(nums):
    count = 0
    result = float('-inf')
    for num in nums:
        if count == 0:
            result = num
            count += 1
        elif num == result:
            count += 1
        else:
            count -= 1
    return result


def main():
    nums_1 = [3, 2, 3]
    nums_2 = [2, 2, 1, 1, 1, 2, 2]
    print(majority(nums_1)) # Output: 3
    print(majority(nums_2)) # Output: 2


if __name__ == '__main__':
    main()
