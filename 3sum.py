# https://leetcode.com/problems/3sum/

import unittest

# O(n^2) - hashing
def solution2(nums):
    n = len(nums)
    ans_set = set()
    numToInd = { num:i for i, num in enumerate(nums)}
    for i in range(n):
        for j in range(i+1, n):
            val = -(nums[i]+nums[j])
            if val in numToInd and numToInd[val] not in [i, j]:
                ans_set.add(tuple(sorted((nums[i], nums[j], val))))
    return [list(x) for x in ans_set]

# O(n^3) - brute - TLE
def solution1(nums):
    n = len(nums)
    ans_set = set()
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    ans_set.add(tuple(sorted((nums[i], nums[j], nums[k]))))
    return [list(x) for x in ans_set]

class Tests(unittest.TestCase):
    cases = [
        {'inp': [-1,0,1,2,-1,-4], 'out': [[-1,0,1],[-1,-1,2]]},
        {'inp': [], 'out': []},
        {'inp': [0], 'out': []},
    ]
    solutions = [solution1,solution2]
    def test(self):
        for sol in self.solutions:
            for case in self.cases:
                self.assertEqual(sol(case['inp']), case['out'])

if __name__ == '__main__':
    unittest.main()