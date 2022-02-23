# https://leetcode.com/problems/valid-palindrome-ii/

import unittest

def isPalindrome(s, skipsLeft=0):
    if skipsLeft < 0:
        return False
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return isPalindrome(s[left+1:right+1], skipsLeft-1) or isPalindrome(s[left:right], skipsLeft-1)
        left, right = left + 1, right - 1
    return True

# O(n^2) - brute
def solution1(s):
    for i in range(len(s)):
        tempStr = s[:i] + s[i+1:]
        if isPalindrome(tempStr):
            return True
    return isPalindrome(s)

# O(n) - brute optimized
def solution2(s):
    return isPalindrome(s, 1)


class Tests(unittest.TestCase):
    cases = [
        {'inp': 'aba', 'out': True},
        {'inp': 'abca', 'out': True},
        {'inp': 'abc', 'out': False},
    ]
    solutions = [solution1, solution2]
    def test(self):
        for sol in self.solutions:
            for case in self.cases:
                self.assertEqual(sol(case['inp']), case['out'])

if __name__ == '__main__':
    unittest.main()