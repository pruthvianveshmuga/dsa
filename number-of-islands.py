# https://leetcode.com/problems/number-of-islands/

import unittest


def dfs(grid, visited, row, col):
    if (not 0 <= row < len(grid)) or (not 0 <= col < len(grid[row])) or grid[row][col] != '1' or visited[row][col]:
        return
    visited[row][col] = True
    neighbours = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for neighbour in neighbours:
        dfs(grid, visited, row + neighbour[0], col + neighbour[1])
    

def solution1(grid):
    visited = [[False for el in row] for row in grid]
    islands = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '1' and not visited[row][col]:
                islands += 1
                dfs(grid, visited, row, col)
    return islands


class Tests(unittest.TestCase):
    cases = [
        {
            'inp': [
                ["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]
            ],
            'out': 1
        },
        {
            'inp': [
                ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]
            ],
            'out': 3
        },
    ]
    solutions = [solution1]
    def test(self):
        for sol in self.solutions:
            for case in self.cases:
                self.assertEqual(sol(case['inp']), case['out'])

if __name__ == '__main__':
    unittest.main()