# https://leetcode.com/problems/valid-word-abbreviation

import unittest

def solution1(word, abbr):
    i_abbr, i_word = 0, 0
    while i_abbr < len(abbr):
        if abbr[i_abbr:i_abbr+1].isnumeric():
            if int(abbr[i_abbr:i_abbr+1]) == 0:
                return False
            start, end = i_abbr, i_abbr+1
            while end <= len(abbr) and abbr[start:end].isnumeric():
                end += 1
            end -= 1
            abbr_len = int(abbr[start:end]) 

            i_word += abbr_len
            i_abbr = end
        else:
            if i_word >= len(word) or word[i_word] != abbr[i_abbr]:
                return False
            i_word += 1
            i_abbr += 1
    if i_word != len(word):
        return False
    return True


class Tests(unittest.TestCase):
    cases = [
        {'inp': ['internationalization', 'i12iz4n'], 'out': True},
        {'inp': ['apple', 'a2e'], 'out': False},
        {'inp': ['a', '01'], 'out': False},
        {'inp': ['a', '1'], 'out': True},
    ]
    solutions = [solution1]
    def test(self):
        for sol in self.solutions:
            for case in self.cases:
                self.assertEqual(sol(case['inp'][0], case['inp'][1]), case['out'])

if __name__ == '__main__':
    unittest.main()