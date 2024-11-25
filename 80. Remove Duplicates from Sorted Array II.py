def remove_duplicates_two(nums):
    n = len(nums)
    if n <= 2: return n
    index = 2
    for i in range(2, n):
        if nums[i] != nums[index - 2]:
            nums[index] = nums[i]
            index += 1
    return index


def main():
    nums = [1, 1, 1, 2, 2, 3]
    print(remove_duplicates_two(nums)) # Output: 5, nums = [1, 1, 2, 2, 3, _]


if __name__ == '__main__':
    main()
