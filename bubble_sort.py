from typing import List


def sort(arr: List[int]) -> List[int]:
    length = len(arr)
    for i in range(length):
        for j in range(length - 1 - i):
            if arr[j] > arr[j + 1]:
                tmp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = tmp

    return arr


def main():
    arr = [5, 20, 6, 1, 12, 2, 10, 11, -4, 3]
    sorted = sort(arr)
    assert [-4, 1, 2, 3, 5, 6, 10, 11, 12, 20] == sorted, sorted


if __name__ == "__main__":
    main()
