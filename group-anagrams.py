# https://leetcode.com/problems/group-anagrams/

import unittest

def solution1(strs):
    hashMap = {}
    for str in strs:
        key = ''.join(sorted(str))
        if key not in hashMap.keys():
            hashMap[key] = []
        hashMap[key].append(str)
    print(list(hashMap.values()))
    return list(hashMap.values())


class Tests(unittest.TestCase):
    cases = [
        {'inp': ["eat","tea","tan","ate","nat","bat"], 'out': [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]},
        {'inp': [""], 'out': [[""]]},
    ]
    solutions = [solution1]
    def test(self):
        for sol in self.solutions:
            for case in self.cases:
                self.assertEqual(sol(case['inp']), case['out'])

if __name__ == '__main__':
    unittest.main()