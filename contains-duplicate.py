# https://leetcode.com/problems/contains-duplicate/

import unittest

# sets - O(n) - Life is short
def solution2(nums):
    return len(set(nums)) != len(nums)

# sorting - O(nlogn)
def solution1(nums):
    sorted = nums[:]
    sorted.sort()
    for i in range(len(sorted)-1):
        if sorted[i] == sorted[i+1]:
            return True
    return False


class Tests(unittest.TestCase):
    cases = [
        {'inp': [1,2,3,1], 'out': True},
        {'inp': [1,2,3,4], 'out': False},
        {'inp': [1,1,1,3,3,4,3,2,4,2], 'out': True},
    ]
    solutions = [solution1, solution2]
    def test(self):
        for sol in self.solutions:
            for case in self.cases:
                self.assertEqual(sol(case['inp']), case['out'])

if __name__ == '__main__':
    unittest.main()