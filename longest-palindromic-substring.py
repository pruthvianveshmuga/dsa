# https://leetcode.com/problems/longest-palindromic-substring/

import unittest

def isPalindrome(s):
    left, right = 0, len(s)-1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# O(n^3) - brute
def solution1(s):
    maxPalindrome = ''
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if isPalindrome(s[i:j]) and len(s[i:j]) > len(maxPalindrome):
                maxPalindrome = s[i:j]
    return maxPalindrome

class Tests(unittest.TestCase):
    cases = [
        {'inp': 'babad', 'out': 'bab'},
        {'inp': 'cbbd', 'out': 'bb'},
    ]
    solutions = [solution1]
    def test(self):
        for sol in self.solutions:
            for case in self.cases:
                self.assertEqual(sol(case['inp']), case['out'])

if __name__ == '__main__':
    unittest.main()