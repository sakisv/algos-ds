import random
from typing import List


def merge_lists(arr_l: List[int], arr_r: List[int]) -> List[int]:
    end_l = []
    l_index = 0
    r_index = 0
    while l_index < len(arr_l) and r_index < len(arr_r):
        if arr_l[l_index] <= arr_r[r_index]:
            end_l.append(arr_l[l_index])
            l_index += 1
        else:
            end_l.append(arr_r[r_index])
            r_index += 1

    end_l.extend(arr_l[l_index:])
    end_l.extend(arr_r[r_index:])

    return end_l


def ms(arr: List[int]) -> List[int]:
    length = len(arr)

    if length == 1:
        return arr

    mid = length // 2

    left = arr[:mid]
    right = arr[mid:]

    left = ms(left)
    right = ms(right)

    return merge_lists(left, right)


def main():
    arr = [5, 20, 6, 1, 12, 2, 10, 11, -4, 3]
    s = ms(arr)
    assert [-4, 1, 2, 3, 5, 6, 10, 11, 12, 20] == s, s
    ls = random.choices([x for x in range(25_000)], k=20_000)
    ls = ms(ls)
    assert all(ls[i] <= ls[i + 1] for i in range(len(ls) - 1))


if __name__ == "__main__":
    main()
