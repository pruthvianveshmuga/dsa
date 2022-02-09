# https://leetcode.com/problems/string-to-integer-atoi/

import unittest

def solution1(s):
    sign = 1
    result = 0
    n = len(s)

    INT_MAX = pow(2, 31) - 1
    INT_MIN = -pow(2, 31)

    i = 0
    while i < n and s[i] == ' ':
        i += 1
    if i < n and s[i] == '+':
        i += 1
    elif i < n and s[i] == '-':
        sign = -1
        i += 1
    while i < n and s[i].isdigit():
        digit = int(s[i])
        # result * 10 + digit <= INT_MAX
        # result * 10 - digit >= INT_MIN
        if sign == 1 and int((INT_MAX - digit)/10) < result:
            return INT_MAX
        if sign == -1 and int((INT_MIN + digit)/10) > -result:
            return INT_MIN
        result = result*10 + digit
        i += 1
    return result * sign



class Tests(unittest.TestCase):
    cases = [
        {'inp': '+-12', 'out': 0},
        {'inp': '91283472332', 'out': 2147483647},
        {'inp': '-91283472332', 'out': -2147483648},
        {'inp': '   -42', 'out': -42},
        {'inp': '42', 'out': 42},
        {'inp': '4193 with words', 'out': 4193},
    ]
    solutions = [solution1]
    def test(self):
        for sol in self.solutions:
            for case in self.cases:
                self.assertEqual(sol(case['inp']), case['out'])

if __name__ == '__main__':
    unittest.main()