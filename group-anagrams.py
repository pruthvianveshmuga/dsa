# https://leetcode.com/problems/group-anagrams/

import collections
import unittest
# sorted str as key
def solution1(strs):
    hashMap = {}
    for str in strs:
        key = ''.join(sorted(str))
        if key not in hashMap.keys():
            hashMap[key] = []
        hashMap[key].append(str)
    return hashMap.values()

# char count as key
def solution2(strs):
    hashMap = collections.defaultdict(list)
    for str in strs:
        count = [0] * 26
        for c in str:
            count[ord(c)-ord('a')] += 1
        hashMap[tuple(count)].append(str)
    return hashMap.values()


class Tests(unittest.TestCase):
    cases = [
        {'inp': ["eat","tea","tan","ate","nat","bat"], 'out': [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]},
        {'inp': [""], 'out': [[""]]},
    ]
    solutions = [solution1, solution2]
    def test(self):
        for sol in self.solutions:
            for case in self.cases:
                self.assertEqual(sol(case['inp']), case['out'])

if __name__ == '__main__':
    unittest.main()