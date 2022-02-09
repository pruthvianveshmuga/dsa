# https://leetcode.com/problems/

import unittest

class Solutions:
    def solution1(inp):
        return ''

class Tests(unittest.TestCase):
    cases = [
        {'inp': '', 'out': ''},
    ]
    solutions = [Solutions.solution1]
    def test(self):
        for sol in self.solutions:
            for case in self.cases:
                self.assertEqual(sol(case['inp']), case['out'])

if __name__ == '__main__':
    unittest.main()