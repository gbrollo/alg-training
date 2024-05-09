# https://leetcode.com/problems/maximize-happiness-of-selected-children/description/

import unittest


class Solution:
    def maximumHappinessSum(self, happiness, k):
        happiness = sorted(happiness, reverse=True)

        happiness_saved = 0

        for i in range(k):
            happiness_saved += max(happiness[i] - i, 0)

        return happiness_saved


param_list = [
    [4, [1, 2, 3], 2],
    [1, [1, 1, 1, 1], 2],
    [5, [2, 3, 4, 5], 1],
    [53, [12, 1, 42], 3],
]


class Test(unittest.TestCase):
    def test_solution(self):
        for expected, happiness, k in param_list:
            with self.subTest():
                self.assertEqual(expected, Solution().maximumHappinessSum(happiness, k))


if __name__ == "__main__":
    unittest.main()
