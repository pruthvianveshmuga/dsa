# https://leetcode.com/problems/binary-search/

import unittest

# Recursion
def binarySearch(nums, target, start, end):
    if start >= end:
        return -1
    mid = (start + end)//2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binarySearch(nums, target, mid+1, end)
    else:
        return binarySearch(nums, target, start, mid)

def solution1(nums, target):
    return binarySearch(nums, target, 0, len(nums))

class Tests(unittest.TestCase):
    cases = [
        {'inp': [[-1,0,3,5,9,12], 9], 'out': 4},
        {'inp': [[-1,0,3,5,9,12], 2], 'out': -1},
    ]
    solutions = [solution1]
    def test(self):
        for sol in self.solutions:
            for case in self.cases:
                self.assertEqual(sol(case['inp'][0], case['inp'][1]), case['out'])

if __name__ == '__main__':
    unittest.main()