# https://leetcode.com/problems/valid-parentheses/

import unittest

def solution1(s):
    stack = []
    openTags = ['(', '[', '{']
    closeTag = {')': '(', ']': '[', '}': '{'}
    for c in s:
        if c in openTags:
            stack.append(c)
        elif len(stack) != 0 and stack[-1] == closeTag[c]:
            stack.pop()
        else:
            return False
    return len(stack) == 0


class Tests(unittest.TestCase):
    cases = [
        {'inp': '()', 'out': True},
        {'inp': '()[]{}', 'out': True},
        {'inp': '(]', 'out': False},
    ]
    solutions = [solution1]
    def test(self):
        for sol in self.solutions:
            for case in self.cases:
                self.assertEqual(sol(case['inp']), case['out'])

if __name__ == '__main__':
    unittest.main()