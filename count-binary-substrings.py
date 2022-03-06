# https://leetcode.com/problems/count-binary-substrings/

import unittest

# O(n) - grouping
def solution1(s):
    groups = [1]
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            groups[-1] += 1
        else:
            groups.append(1)
    ans = 0
    for i in range(len(groups)-1):
        ans += min(groups[i], groups[i+1])
    return ans


class Tests(unittest.TestCase):
    cases = [
        {'inp': '00110011', 'out': 6},
        {'inp': '10101', 'out': 4},
    ]
    solutions = [solution1]
    def test(self):
        for sol in self.solutions:
            for case in self.cases:
                self.assertEqual(sol(case['inp']), case['out'])

if __name__ == '__main__':
    unittest.main()