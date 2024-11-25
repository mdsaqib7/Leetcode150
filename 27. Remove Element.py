def remove_element(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


def main():
    nums = [3, 2, 2, 3]
    val = 3
    print(remove_element(nums, val)) # Output: 2, nums = [2,2,_,_]


if __name__ == '__main__':
    main()
