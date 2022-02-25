# https://leetcode.com/problems/roman-to-integer/

import unittest

# O(1) - First run
def solution1(s):
    def isNegative(s):
        after = {'I': ['V', 'X'], 'X': ['L', 'C'], 'C': ['D', 'M']}
        if len(s) == 2 and s[0] in after.keys() and s[1] in after[s[0]]:
            return True
        return False

    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    return sum([values[c]*(-1 if isNegative(s[i:i+2]) else 1) for i, c in enumerate(s)])

class Tests(unittest.TestCase):
    cases = [
        {'inp': 'III', 'out': 3},
        {'inp': 'LVIII', 'out': 58},
        {'inp': 'MCMXCIV', 'out': 1994},
    ]
    solutions = [solution1]
    def test(self):
        for sol in self.solutions:
            for case in self.cases:
                self.assertEqual(sol(case['inp']), case['out'])

if __name__ == '__main__':
    unittest.main()