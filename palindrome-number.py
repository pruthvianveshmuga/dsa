# https://leetcode.com/problems/palindrome-number/

import unittest

# Life is short
def solution2(x):
    return str(x) == str(x)[::-1]


# O(1) time, O(1) space
def solution1(x):
    inp = str(x)
    mid = len(inp)//2
    if len(inp)%2 != 0:
        inp = inp[:mid] + inp[mid+1:]
    return (inp[:mid] + inp[mid:]) == (inp[:mid] + inp[:mid][::-1])

class Tests(unittest.TestCase):
    cases = [
        {'inp': 121, 'out': True},
        {'inp': -121, 'out': False},
        {'inp': 10, 'out': False},
    ]
    solutions = [solution1, solution2]
    def test(self):
        for sol in self.solutions:
            for case in self.cases:
                self.assertEqual(sol(case['inp']), case['out'])

if __name__ == '__main__':
    unittest.main()