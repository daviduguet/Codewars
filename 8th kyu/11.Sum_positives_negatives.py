
"""
Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

If the input is an empty array or is null, return an empty array.
"""

def count_positives_sum_negatives(arr):
    positives = 0
    negatives = 0
    for i in arr:
        if i > 0:
            positives += 1
        else:
            negatives += i
    return [positives, negatives]

    


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]

numbers2 = [0, 0]

print(count_positives_sum_negatives(numbers2))
