import random


def quick_sort(n: list[int]) -> list[int]:
    if len(n) < 1:
        return n
    pivot = n.pop(0)
    left = [i for i in n if i <= pivot]
    right = [i for i in n if i > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == '__main__':
    nums = [random.randint(1, 100) for _ in range(10)]
    print(nums)
    print(quick_sort(nums))
