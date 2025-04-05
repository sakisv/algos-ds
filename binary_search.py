import math

def search(haystack: list[int], needle: int) -> bool:
    print(f"Haystack: {haystack} | Needle: {needle}")
    start = 0
    end = len(haystack)

    while start < end:
        mid = math.floor((end - start) / 2) + start
        # print(f"Start: {start} | End {end} | Mid {mid}")
        if needle == haystack[mid]:
            return True
        elif needle > haystack[mid]:
            start = mid+1
        else: # needle < haystack[mid]
            end = mid

    return False



if __name__ == "__main__":
    # odd length
    assert search([1, 2, 3, 4, 5, 6, 7], 4) is True
    assert search([1, 2, 3, 4, 5, 6, 7], 7) is True
    assert search([1, 2, 3, 4, 5, 6, 7], 1) is True
    assert search([1, 2, 3, 4, 5, 6, 7], 100) is not True
    assert search([1, 2, 3, 4, 5, 6, 7], -100) is not True

    # even length
    assert search([1, 2, 3, 4, 5, 6], 3) is True
    assert search([1, 2, 3, 4, 5, 6], 6) is True
    assert search([1, 2, 3, 4, 5, 6], 1) is True
    assert search([1, 2, 3, 4, 5, 6], 100) is not True
    assert search([1, 2, 3, 4, 5, 6], -100) is not True
