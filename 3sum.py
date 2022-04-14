# https://leetcode.com/problems/3sum/

from typing import List
import unittest

def twoSum(arr, reqSum, ans: List):
    left, right = 0, len(arr)-1
    while(left < right):
        sum = arr[left] + arr[right]
        if sum < reqSum or (left > 0 and arr[left] == arr[left-1]):
            left += 1
        elif sum > reqSum or (right < len(arr)-1 and arr[right] == arr[right+1]):
            right -= 1
        else:
            ans.append([-reqSum, arr[left], arr[right]])
            left += 1
            right -= 1
    return


# O(n^2) - two pointer
def solution3(nums):
    nums.sort()
    n = len(nums)
    ans = []
    for i in range(n):
        if nums[i] > 0:
            break
        elif i > 0 and nums[i] == nums[i-1]:
            continue
        else:
            twoSum(nums[i+1:], -nums[i], ans)
    return ans


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


# Note: Tests might fail as the order of list elements might not match. Need a testing func.
class Tests(unittest.TestCase):
    cases = [
        {'inp': [-1,0,1,2,-1,-4], 'out': [[-1,0,1],[-1,-1,2]]},
        {'inp': [], 'out': []},
        {'inp': [0], 'out': []},
    ]
    solutions = [solution1, solution2, solution3]
    def test(self):
        for sol in self.solutions:
            for case in self.cases:
                self.assertEqual(sol(case['inp']), case['out'])

if __name__ == '__main__':
    unittest.main()