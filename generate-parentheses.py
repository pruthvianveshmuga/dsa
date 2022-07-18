# https://leetcode.com/problems/generate-parentheses/

import unittest

def solution1(n):
    def dfs(str, openRem, unclosed, result):
        if not openRem and not unclosed:
            result.append(str)
            return
        if openRem:
            dfs(str + "(", openRem-1, unclosed+1, result)
        if unclosed:
            dfs(str + ")", openRem, unclosed-1, result)
    result = []
    dfs("", n, 0, result)
    return result

class Tests(unittest.TestCase):
    cases = [
        {'inp': 3, 'out': ["((()))","(()())","(())()","()(())","()()()"]},
        {'inp': 1, 'out': ["()"]},
    ]
    solutions = [solution1]
    def test(self):
        for sol in self.solutions:
            for case in self.cases:
                self.assertEqual(sol(case['inp']), case['out'])

if __name__ == '__main__':
    unittest.main()