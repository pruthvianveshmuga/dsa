# https://leetcode.com/problems/valid-anagram/

import collections
import unittest


def solution1(s, t):
    return collections.Counter(s) == collections.Counter(t)

def solution2(s, t):
    return sorted(s) == sorted(t) 

class Tests(unittest.TestCase):
    cases = [
        {'inp': ["anagram", "nagaram"], 'out': True},
        {'inp': ["rat", "car"], 'out': False},
    ]
    solutions = [solution1, solution2]
    def test(self):
        for sol in self.solutions:
            for case in self.cases:
                self.assertEqual(sol(case['inp'][0], case['inp'][1]), case['out'])

if __name__ == '__main__':
    unittest.main()