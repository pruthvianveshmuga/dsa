# https://leetcode.com/problems/search-in-rotated-sorted-array/

import unittest

# two pass - O(logN)
def solution1(nums, target):
    def getPivot(nums):
        left, right = 0, len(nums) - 1
        if nums[left] <= nums[right]:
            return left
        while(left <= right):
            mid = (left+right)//2
            if nums[mid] > nums[mid+1]:
                return mid+1
            if nums[mid] >= nums[left]:
                left = mid+1
            else:
                right = mid-1
        return -1
    def findTarget(nums, left, right, target):
        while(left <= right):
            mid = (left+right)//2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                right = mid-1
            else:
                left = mid+1
        return -1
    pivot = getPivot(nums)
    if target <= nums[-1]:
        return findTarget(nums, pivot, len(nums)-1, target)
    else:
        return findTarget(nums, 0, pivot-1, target)

class Tests(unittest.TestCase):
    cases = [
        # {'inp': [[4,5,6,7,0,1,2], 0], 'out': 4},
        # {'inp': [[4,5,6,7,8,0,1,2], 3], 'out': -1},
        # {'inp': [[1], 1], 'out': 0},
        {'inp': [[4,5,1,2,3], 1], 'out': 2},
    ]
    solutions = [solution1]
    def test(self):
        for sol in self.solutions:
            for case in self.cases:
                self.assertEqual(sol(case['inp'][0], case['inp'][1]), case['out'])

if __name__ == '__main__':
    unittest.main()