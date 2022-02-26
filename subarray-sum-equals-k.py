# https://leetcode.com/problems/subarray-sum-equals-k/

import unittest

# O(n) - using hash map
def solution2(nums, k):
    ans = 0
    sumOccurences = {0: 1}
    currSum = 0
    for num in nums:
        currSum += num
        ans += sumOccurences[currSum - k] if (currSum - k) in sumOccurences else 0
        sumOccurences[currSum] = (sumOccurences[currSum] if currSum in sumOccurences else 0) + 1
    return ans


# O(n^2) - optimized brute - TLE
def solution1(nums, k):
    acc = [0]
    for num in nums:
        acc.append(num + acc[-1])
    count = 0
    for i, start in enumerate(acc):
        for end in acc[i+1:]:
            if end - start == k:
                count += 1
    return count

class Tests(unittest.TestCase):
    cases = [
        {'inp': [[1,1,1], 2], 'out': 2},
        {'inp': [[1,2,3], 3], 'out': 2},
        {'inp': [[1], 0], 'out': 0},
    ]
    solutions = [solution1, solution2]
    def test(self):
        for sol in self.solutions:
            for case in self.cases:
                self.assertEqual(sol(case['inp'][0], case['inp'][1]), case['out'])

if __name__ == '__main__':
    unittest.main()