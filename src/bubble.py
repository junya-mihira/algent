import random


def bubble(n: list[int]) -> list[int]:
    for i in range(len(n)):
        change = False
        for j in range(len(n)-i-1):  # -iはソート済み部分を除外するため
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
                change = True
        if not change:
            break
    return n


if __name__ == '__main__':
    nums = [random.randint(1, 100) for _ in range(10)]
    print(nums)
    print(bubble(nums))
