# https://leetcode.com/problems/maximum-subarray/

import math
import sys
import unittest

# O(n)
def solution1(nums):
    result = -(sys.maxsize - 1)
    sum = 0
    for num in nums:
        sum += num
        sum = max(sum, num)
        result = max(result, sum)
    return result

# O(n^2)
def solution2(nums):
    result = -(sys.maxsize-1)
    for i in range(len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]
            if sum > result:
                result = sum
    return result


class Tests(unittest.TestCase):
    cases = [
        {'inp': [-2,1,-3,4,-1,2,1,-5,4], 'out': 6},
        {'inp': [1], 'out': 1},
        {'inp': [5,4,-1,7,8], 'out': 23},
    ]
    solutions = [solution1, solution2]
    def test(self):
        for sol in self.solutions:
            for case in self.cases:
                self.assertEqual(sol(case['inp']), case['out'])

if __name__ == '__main__':
    unittest.main()