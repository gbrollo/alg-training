# https://leetcode.com/problems/k-th-smallest-prime-fraction/

import heapq
import unittest


class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        min_heap = []
        arr_len = len(arr)
        for i in range(arr_len):
            for j in range(i + 1, arr_len):
                heapq.heappush(min_heap, (arr[i] / arr[j], (arr[i], arr[j])))

        numerador, divisor = heapq.nsmallest(k, min_heap)[-1][1]

        return [numerador, divisor]


param_list = [
    [[2, 5], [1, 2, 3, 5], 3],
    [[1, 7], [1, 7], 1],
]


class Test(unittest.TestCase):
    def test(self):
        for expected, arr, k in param_list:
            with self.subTest():
                self.assertEqual(expected, Solution().kthSmallestPrimeFraction(arr, k))


if __name__ == "__main__":
    unittest.main()
