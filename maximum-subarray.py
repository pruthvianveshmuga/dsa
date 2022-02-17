# https://leetcode.com/problems/maximum-subarray/

import math
import sys
import unittest

# O(n) - greedy
def solution1(nums):
    result = -(sys.maxsize - 1)
    sum = 0
    for num in nums:
        sum += num
        sum = max(sum, num)
        result = max(result, sum)
    return result

# O(n^2) - brute
def solution2(nums):
    result = -(sys.maxsize-1)
    for i in range(len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]
            if sum > result:
                result = sum
    return result

# O(n) - dp
def solution3(nums):
    result, lastSum = -math.inf, 0
    for num in nums:
        lastSum = max(lastSum, 0) + num
        result = max(result, lastSum)
    return result

def leftAndRight(nums, midIndex):
    right, sum = -math.inf, 0
    for num in nums[midIndex:]:
        sum += num
        right = max(right, sum)
    left, sum = -math.inf, 0
    for num in reversed(nums[:midIndex]):
        sum += num
        left = max(left, sum)
    return left + right

# O(nlogn) - divide and conquer
def solution4(nums):
    if len(nums) == 1:
        return nums[0]
    midIndex = int(len(nums)/2)
    left = solution4(nums[:midIndex])
    right = solution4(nums[midIndex:])
    both = leftAndRight(nums, midIndex)
    return max(left, right, both)
    


class Tests(unittest.TestCase):
    cases = [
        {'inp': [-2,1,-3,4,-1,2,1,-5,4], 'out': 6},
        {'inp': [1], 'out': 1},
        {'inp': [5,4,-1,7,8], 'out': 23},
    ]
    solutions = [solution1, solution2, solution3, solution4]
    def test(self):
        for sol in self.solutions:
            for case in self.cases:
                self.assertEqual(sol(case['inp']), case['out'])

if __name__ == '__main__':
    unittest.main()