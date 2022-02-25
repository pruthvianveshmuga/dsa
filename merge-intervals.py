# https://leetcode.com/problems/merge-intervals/

from operator import itemgetter
import unittest

# edit result in every iteration instead of appending the finalised item
def solution2(intervals):
    intervals.sort(key=itemgetter(0))
    merged = []
    for interval in intervals:
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged
            

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
    solutions = [solution1, solution2]
    def test(self):
        for sol in self.solutions:
            for case in self.cases:
                self.assertEqual(sol(case['inp']), case['out'])

if __name__ == '__main__':
    unittest.main()