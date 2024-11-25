def merge(n1, n2, m, n):
    last = m + n - 1
    while m > 0 and n > 0:
        if n1[m - 1] > n2[n - 1]:
            n1[last] = n1[m - 1]
            m -= 1
        else:
            n1[last] = n2[n - 1]
            n -= 1
        last -= 1

    while n > 0:
        n1[last] = n2[n - 1]
        n -= 1
        last -= 1

    return n1


def main():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(merge(nums1, nums2, m, n)) # Output: [1,2,2,3,5,6]


if __name__ == '__main__':
    main()
