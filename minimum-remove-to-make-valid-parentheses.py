# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

import unittest

# O(n) - using stack
def solution1(s):
    invalidInd = set()
    stack = []
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == ')':
            if stack:
                stack.pop()
            else:
                invalidInd.add(i)
    invalidInd = invalidInd.union(set(stack))
    return ''.join([c for i, c in enumerate(s) if i not in invalidInd])
            

class Tests(unittest.TestCase):
    cases = [
        {'inp': 'lee(t(c)o)de)', 'out': 'lee(t(c)o)de'},
        {'inp': 'a)b(c)d', 'out': 'ab(c)d'},
        {'inp': '))((', 'out': ''},
    ]
    solutions = [solution1]
    def test(self):
        for sol in self.solutions:
            for case in self.cases:
                self.assertEqual(sol(case['inp']), case['out'])

if __name__ == '__main__':
    unittest.main()