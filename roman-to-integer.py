# https://leetcode.com/problems/roman-to-integer/

import unittest

# reverse - life is short
def solution3(s):
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    return sum([values[s[i]] * (-1 if i < len(s)-1 and values[s[i]] < values[s[i+1]] else 1) for i in reversed(range(len(s)))])


def solution2(s):
    values = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900, 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ans = 0
    while s:
        item = [k for k in values.keys() if s.startswith(k)][0]
        ans += values[item]
        s = s[len(item):]
    return ans

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
    solutions = [solution1, solution2, solution3]
    def test(self):
        for sol in self.solutions:
            for case in self.cases:
                self.assertEqual(sol(case['inp']), case['out'])

if __name__ == '__main__':
    unittest.main()