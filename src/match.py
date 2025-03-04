def match(nums: list[int]) -> bool:
    s = nums[0]
    for i in nums[1::]:
        if i == s:
            return True
        s = i


def match1(nums: list[int]) -> bool:
    s = []
    s.append(nums[0])
    for i in nums[1::]:
        if i in s:
            return True
        s.append(i)


if __name__ == '__main__':
    nums = list(range(10))
    nums1 = [0, 1, 2, 3, 4, 5, 5]
    ans = match(nums1)
    print(ans)
    ans1 = match1(nums1)
    print(ans1)
