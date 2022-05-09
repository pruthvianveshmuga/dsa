# https://leetcode.com/problems/meeting-rooms-ii/

from functools import cmp_to_key
from operator import itemgetter
import unittest

# O(nlogn) - sorting
def solution1(intervals):
    temp = []
    for interval in intervals:
        temp.append(('start', interval[0]))
        temp.append(('end', interval[1]))
    precedence = {'end': 0, 'start': 1}
    temp.sort(key=lambda item: precedence[item[0]])
    events = [timing[0] for timing in sorted(temp, key=itemgetter(1))]
    maxRoomsUsed, currRoomsUsed = 0, 0
    for event in events:
        currRoomsUsed += (1 if event == 'start' else -1)
        maxRoomsUsed = max(maxRoomsUsed, currRoomsUsed)
    return maxRoomsUsed


class Tests(unittest.TestCase):
    cases = [
        {'inp': [[0,30],[5,10],[15,20]], 'out': 2},
        {'inp': [[7,10],[2,4]], 'out': 1},
        {'inp': [[13,15],[1,13]], 'out': 1},
    ]
    solutions = [solution1]
    def test(self):
        for sol in self.solutions:
            for case in self.cases:
                self.assertEqual(sol(case['inp']), case['out'])

if __name__ == '__main__':
    unittest.main()