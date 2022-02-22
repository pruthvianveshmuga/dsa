# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

import unittest

def solution1(prices):
    maxProfit, minPrice = 0, prices[0]
    for price in prices:
        minPrice = min(minPrice, price)
        maxProfit = max(maxProfit, price - minPrice)
    return maxProfit


class Tests(unittest.TestCase):
    cases = [
        {'inp': [7,1,5,3,6,4], 'out': 5},
        {'inp': [7,6,4,3,1], 'out': 0},
    ]
    solutions = [solution1]
    def test(self):
        for sol in self.solutions:
            for case in self.cases:
                self.assertEqual(sol(case['inp']), case['out'])

if __name__ == '__main__':
    unittest.main()