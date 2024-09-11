from itertools import combinations
def merge_and_count(array, temp_array, left, mid, right):
    i = left    # Starting index for the left subarray
    j = mid + 1 # Starting index for the right subarray
    k = left    # Starting index to be sorted
    inv_count = 0

    # Conditions are checked to ensure that i doesn't exceed mid and j doesn't exceed right
    while i <= mid and j <= right:
        if array[i] <= array[j]:
            temp_array[k] = array[i]
            i += 1
        else:
            # There are mid - i inversions because all elements left to i in the left subarray
            # are greater than array[j]
            temp_array[k] = array[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1

    # Copy the remaining elements of left subarray, if any
    while i <= mid:
        temp_array[k] = array[i]
        i += 1
        k += 1

    # Copy the remaining elements of right subarray, if any
    while j <= right:
        temp_array[k] = array[j]
        j += 1
        k += 1

    # Copy the sorted subarray into the original array
    for i in range(left, right + 1):
        array[i] = temp_array[i]

    return inv_count

def merge_sort_and_count(array, temp_array, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

        inv_count += merge_sort_and_count(array, temp_array, left, mid)
        inv_count += merge_sort_and_count(array, temp_array, mid + 1, right)
        inv_count += merge_and_count(array, temp_array, left, mid, right)

    return inv_count
def count_inversions(elements):
    temp_array = [0] * len(elements)
    return merge_sort_and_count(elements, temp_array, 0, len(elements) - 1)

if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print( count_inversions(elements))
