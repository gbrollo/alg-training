# https://leetcode.com/problems/subsets


import unittest


class Solution(object):
    def subsets(self, nums):
        sets = [[]]
        for i in range(len(nums)):
            sets += [sets[j] + [nums[i]] for j in range(len(sets))]
        return sets


param_list = [
    [[[]], []],
    [[[], [1]], [1]],
    [[[], [1], [2], [1, 2]], [1, 2]],
    [[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]], [1, 2, 3]],
]


class Test(unittest.TestCase):
    def test_solution(self):
        for expected, nums in param_list:
            with self.subTest():
                self.assertEqual(
                    expected,
                    Solution().subsets(nums),
                )


if __name__ == "__main__":
    unittest.main()
