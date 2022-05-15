# https://leetcode.com/problems/container-with-most-water/

import unittest

from template import solution1

# brute - O(n^2)
def solution1(height):
	maxWater = 0
	for i in range(len(height)):
		for j in range(i+1, len(height)):
			water = (j-i) * min(height[i], height[j])
			maxWater = max(maxWater, water)
	return maxWater

# greedy - O(n)
def solution2(height):
	def calc(i, j, height):
		return (j-i) * min(height[i], height[j])
	maxWater = 0
	i, j = 0, len(height) - 1
	while i < j:
		maxWater = max(maxWater, calc(i, j, height))
		if height[i] < height[j]:
			i += 1
		else:
			j -= 1
	return maxWater
		

class Tests(unittest.TestCase):
	cases = [
		{'inp': [1,8,6,2,5,4,8,3,7], 'out': 49},
		{'inp': [1,1], 'out': 1},
		{'inp': [1,3,2,5,25,24,5], 'out': 24}
	]
	solutions = [solution1, solution2]
	def test(self):
		for sol in self.solutions:
			for case in self.cases:
				self.assertEqual(sol(case['inp']), case['out'])

if __name__ == '__main__':
	unittest.main()

