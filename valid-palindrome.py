# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/

import unittest

def solution1(s):
    filtered = "".join(c for c in s.lower() if c.isalnum())
    reversed = filtered[::-1]
    return filtered == reversed

def solution2(s):
    i, j = 0, len(s) - 1
    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1
        if i != j and s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True

class Tests(unittest.TestCase):
    cases = [
        {'inp': 'A man, a plan, a canal: Panama', 'out': True},
        {'inp': 'race a car', 'out': False},
        {'inp': ' ', 'out': True},
    ]
    solutions = [solution1, solution2]
    def test(self):
        for sol in self.solutions:
            for case in self.cases:
                self.assertEqual(sol(case['inp']), case['out'])

if __name__ == '__main__':
    unittest.main()