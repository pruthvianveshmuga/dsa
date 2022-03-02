# https://leetcode.com/problems/next-permutation/

import unittest

# O(n)
def solution2(nums):
    for i in reversed(range(len(nums)-1)):
        if nums[i] < nums[i+1]:
            break
    else:
        nums.sort()
        return nums
    for j in reversed(range(i+1, len(nums))):
        if nums[j] > nums[i]:
            nums[i], nums[j] = nums[j], nums[i]
            break
    nums[i+1:] = reversed(nums[i+1:])
    return nums

# O(nlogn)
def solution1(nums):
    for i in reversed(range(len(nums)-1)):
        if nums[i] < nums[i+1]:
            break
    else:
        nums.sort()
        return nums
    for j in reversed(range(i+1, len(nums))):
        if nums[j] > nums[i]:
            nums[i], nums[j] = nums[j], nums[i]
            break
    nums[i+1:] = sorted(nums[i+1:])
    return nums

class Tests(unittest.TestCase):
    
    solutions = [solution1, solution2]
    def test(self):
        for sol in self.solutions:
            cases = [
                {'inp': [4,3,2,1], 'out': [1,2,3,4]},
                {'inp': [1,4,3,2], 'out': [2,1,3,4]},
                {'inp': [2,1,5,4,3], 'out': [2,3,1,4,5]},
                {'inp': [1,2,5,4,3], 'out': [1,3,2,4,5]},
                {'inp': [1,2,3], 'out': [1,3,2]},
                {'inp': [3,2,1], 'out': [1,2,3]},
                {'inp': [1,1,5], 'out': [1,5,1]},
            ]
            for case in cases:
                self.assertEqual(sol(case['inp']), case['out'])

if __name__ == '__main__':
    unittest.main()