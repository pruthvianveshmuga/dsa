# https://leetcode.com/problems/fizz-buzz

import unittest

def solution1(n):
    result = []
    for i in range(1, n+1):
        if i % 15 == 0:
            val = 'FizzBuzz'
        elif i % 3 == 0:
            val = 'Fizz'
        elif i % 5 == 0:
            val = 'Buzz'
        else:
            val = str(i)
        result.append(val)
    return result

class Tests(unittest.TestCase):
    cases = [
        {'inp': 3, 'out': ['1','2','Fizz']},
        {'inp': 5, 'out': ['1','2','Fizz','4','Buzz']},
        {'inp': 15, 'out': ['1','2','Fizz','4','Buzz','Fizz','7','8','Fizz','Buzz','11','Fizz','13','14','FizzBuzz']},
    ]
    solutions = [solution1]
    def test(self):
        for sol in self.solutions:
            for case in self.cases:
                self.assertEqual(sol(case['inp']), case['out'])

if __name__ == '__main__':
    unittest.main()