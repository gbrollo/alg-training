# https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/

import unittest


class ListNode(object):
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def toLinkedList(values):
    head = None

    for i in range(len(values) - 1, -1, -1):
        head = ListNode(values[i], head)

    return head


def toList(head):
    values = []

    while head is not None:
        values += [head.val]
        head = head.next

    return values


class Solution(object):
    def doubleItRec(self, head):
        if head is None:
            return head, 0

        result, overflow = self.doubleItRec(head.next)

        double = head.val * 2 + overflow
        overflow = double // 10

        return (ListNode(double % 10, result), overflow)

    def doubleIt(self, head):
        result, overflow = self.doubleItRec(head)

        if overflow:
            return ListNode(overflow, result)

        return result


param_list = [
    [[3, 7, 8], [1, 8, 9]],
    [[1, 9, 9, 8], [9, 9, 9]],
    [[1, 0], [5]],
    [[0], [0]],
]


class Test(unittest.TestCase):
    def test(self):
        for expected, values in param_list:
            with self.subTest():
                self.assertEqual(
                    expected,
                    toList(Solution().doubleIt(toLinkedList(values))),
                )


if __name__ == "__main__":
    unittest.main()
