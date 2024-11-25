def remove_duplicates(nums):
    left, right = 1, 1
    while right < len(nums):
        if nums[right] != nums[left - 1]:
            nums[left] = nums[right]
            left += 1
        right += 1
    return left


def main():
    nums = [1, 1, 2]
    print(remove_duplicates(nums))


if __name__ == '__main__':
    main()
