# https://leetcode.com/problems/boats-to-save-people/

import unittest


class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()

        boats = 0
        left = 0
        right = len(people) - 1

        while left <= right:
            if people[left] + people[right] <= limit:
                boats += 1
                left += 1
                right -= 1

            elif people[right] <= limit:
                right -= 1
                boats += 1

        return boats


param_list = [
    [1, [1, 2], 3],
    [3, [3, 2, 2, 1], 3],
    [4, [3, 5, 3, 4], 5],
    [3, [3, 8, 7, 1, 4], 9],
]


class Test(unittest.TestCase):
    def test_numRescueBoats(self):
        for expected, people, limit in param_list:
            with self.subTest():
                self.assertEqual(expected, Solution().numRescueBoats(people, limit))


if __name__ == "__main__":
    unittest.main()
