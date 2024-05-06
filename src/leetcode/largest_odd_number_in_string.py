# https://leetcode.com/problems/largest-odd-number-in-string

import unittest


class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 != 0:
                return num[: i + 1]

        return ""


param_list = [["5", "52"], ["", "4206"], ["35427", "35427"], ["1013389", "10133890"]]


class Test(unittest.TestCase):
    def test(self):
        for expected, num in param_list:
            with self.subTest():
                self.assertEqual(expected, Solution().largestOddNumber(num))


if __name__ == "__main__":
    unittest.main()
