# https://leetcode.com/problems/merge-intervals/

from operator import itemgetter
import unittest

def solution1(intervals):
    sortedInts = sorted(intervals, key=itemgetter(0))
    result = []
    prevStart, prevEnd = sortedInts[0]
    for interval in sortedInts:
        start, end = interval
        if start > prevEnd:
            result.append([prevStart, prevEnd])
            prevStart, prevEnd = start, end
        else:
            prevEnd = max(end, prevEnd)
    result.append([prevStart, prevEnd])
    return result
        

class Tests(unittest.TestCase):
    cases = [
        {'inp': [[1,3],[2,6],[8,10],[15,18]], 'out': [[1,6],[8,10],[15,18]]},
        {'inp': [[1,4],[4,5]], 'out': [[1,5]]},
    ]
    solutions = [solution1]
    def test(self):
        for sol in self.solutions:
            for case in self.cases:
                self.assertEqual(sol(case['inp']), case['out'])

if __name__ == '__main__':
    unittest.main()