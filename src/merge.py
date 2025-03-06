import random


def merge_sort(n: list[int]) -> list[int]:
    if len(n) <= 1:
        return n
    mid = len(n) // 2
    left = n[:mid]
    right = n[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(left: list[int], right: list[int]) -> list[int]:
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged += left[i:]
    merged += right[j:]
    return merged


if __name__ == '__main__':
    nums = [random.randint(1, 100) for _ in range(10)]
    print(nums)
    print(merge_sort(nums))
