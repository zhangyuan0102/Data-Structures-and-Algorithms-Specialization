from random import randint


def partition3(array, left, right):
    pivot = array[left]
    lt = left  # We initiate lt to be the part that is less than the pivot
    i = left   # We scan the array from left to right
    gt = right # The part that is greater than the pivot
    while i <= gt:
        if array[i] < pivot:
            array[lt], array[i] = array[i], array[lt]
            lt += 1
            i += 1
        elif array[i] > pivot:
            array[gt], array[i] = array[i], array[gt]
            gt -= 1
        else:
            i += 1
    return lt, gt


def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
