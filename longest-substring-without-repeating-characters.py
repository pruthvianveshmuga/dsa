# https://leetcode.com/problems/longest-substring-without-repeating-characters/

import unittest

# O(n) - hashmap on the fly
def solution1(s):
    index = {}
    maxLen = 0
    start = -1
    for end, c in enumerate(s):
        if c in index.keys():
            start = max(start, index[c])
        maxLen = max(maxLen, end - start)
        index[c] = end
    return maxLen


class Tests(unittest.TestCase):
    cases = [
        {'inp': 'abcabcbb', 'out': 3},
        {'inp': 'bbbbb', 'out': 1},
        {'inp': 'pwwkew', 'out': 3},
    ]
    solutions = [solution1]
    def test(self):
        for sol in self.solutions:
            for case in self.cases:
                self.assertEqual(sol(case['inp']), case['out'])

if __name__ == '__main__':
    unittest.main()