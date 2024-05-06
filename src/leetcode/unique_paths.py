# https://leetcode.com/problems/unique-paths/description/

import unittest


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                paths[i][j] = paths[i - 1][j] + paths[i][j - 1]

        return paths[-1][-1]


param_list = [
    [28, 3, 7],
    [3, 3, 2],
]


class Test(unittest.TestCase):
    def test(self):
        for expected, m, n in param_list:
            with self.subTest():
                self.assertEqual(expected, Solution().uniquePaths(m, n))


if __name__ == "__main__":
    unittest.main()
