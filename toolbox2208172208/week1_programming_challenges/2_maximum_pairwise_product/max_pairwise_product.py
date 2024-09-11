def max_pairwise_product(numbers):
    n = len(numbers)
    index1 = -1
    index2 = -1
    for i in range(n):
        if index1 == -1 or numbers[i] > numbers[index1]:
            index1 = i
    for i in range(n):
        if i != index1 and (index2 == -1 or numbers[i] > numbers[index2]):
            index2 = i

    return numbers[index1] * numbers[index2]


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx, second_mx = 0, 0
        for num in nums:
            if num > mx:
                mx, second_mx = num, mx
            elif num > second_mx:
                second_mx = num
        return (mx - 1) * (second_mx - 1)




