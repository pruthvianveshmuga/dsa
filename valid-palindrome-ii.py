# https://leetcode.com/problems/valid-palindrome-ii/

import unittest

def isPalindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left, right = left + 1, right - 1
    return True

# O(n^2) - brute
def solution1(s):
    for i in range(len(s)):
        tempStr = s[:i] + s[i+1:]
        if isPalindrome(tempStr):
            return True
    return False

class Tests(unittest.TestCase):
    cases = [
        {'inp': 'aba', 'out': True},
        {'inp': 'abca', 'out': True},
        {'inp': 'abc', 'out': False},
    ]
    solutions = [solution1]
    def test(self):
        for sol in self.solutions:
            for case in self.cases:
                self.assertEqual(sol(case['inp']), case['out'])

if __name__ == '__main__':
    unittest.main()