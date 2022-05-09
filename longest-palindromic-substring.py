# https://leetcode.com/problems/longest-palindromic-substring/

import unittest

def expandAroundCenter(s, left, right):
    maxPalindrome = ''
    while left >= 0 and right < len(s):
        if s[left] != s[right]:
            break
        curr = s[left:right+1]
        maxPalindrome = curr if len(curr) > len(maxPalindrome) else maxPalindrome
        left, right = left - 1, right + 1
    return maxPalindrome

# O(n^2) -> expand around the center
def solution2(s):
    maxPalindrome = ''
    for center in range(len(s)):
        curr = expandAroundCenter(s, center, center)
        if len(curr) > len(maxPalindrome):
            maxPalindrome = curr
        curr = expandAroundCenter(s, center, center + 1)
        if len(curr) > len(maxPalindrome):
            maxPalindrome = curr
    return maxPalindrome


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
    solutions = [solution1, solution2]
    def test(self):
        for sol in self.solutions:
            for case in self.cases:
                self.assertEqual(sol(case['inp']), case['out'])

if __name__ == '__main__':
    unittest.main()