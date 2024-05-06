# https://leetcode.com/problems/climbing-stairs/

import unittest


class Solution:
    def climbStairs(self, n: int) -> int:
        values = [1] * (n + 1)
        for i in range(2, n + 1):
            values[i] = values[i - 1] + values[i - 2]

        return values[n]


param_list = [
    [2, 2],
    [3, 3],
    [5, 4],
    [8, 5],
]


class Test(unittest.TestCase):
    def test(self):
        for expected, n in param_list:
            with self.subTest():
                self.assertEqual(expected, Solution().climbStairs(n))


if __name__ == "__main__":
    unittest.main()
