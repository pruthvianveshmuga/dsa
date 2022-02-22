# https://leetcode.com/problems/longest-common-prefix/

import unittest

# Optimized brute - O(n*l) where l is the length of shortest string
def solution1(strs):
    maxLen = min([len(str) for str in strs])
    for i in range(maxLen):
        char = strs[0][i]
        for str in strs:
            if str[i] != char:
                return str[:i]
    return strs[0][:maxLen]


class Tests(unittest.TestCase):
    cases = [
        {'inp': ["flower","flow","flight"], 'out': 'fl'},
        {'inp': ["dog","racecar","car"], 'out': ''},
    ]
    solutions = [solution1]
    def test(self):
        for sol in self.solutions:
            for case in self.cases:
                self.assertEqual(sol(case['inp']), case['out'])

if __name__ == '__main__':
    unittest.main()