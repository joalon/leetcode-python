import unittest
from math import ceil

class ListNode:
    def __init__(self, x, n=None):
        self.val = x
        self.next = n

    def __eq__(self, other):
        if other is not None and self.val == other.val and self.next == other.next:
            return True
        return False


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        trav = head
        length = 0
        while trav.next is not None:
            length += 1
            trav = trav.next

        trav = head
        for i in range(ceil(length/2)):
            trav = trav.next

        return trav



class Tester(unittest.TestCase):
    def testMiddleNode(self):
        half = ListNode(4, ListNode(5, ListNode(6, None)))
        test = ListNode(1, ListNode(2, ListNode(3, half)))

        result = Solution().middleNode(test)
        self.assertEqual(half, result)


if __name__ == "__main__":
    unittest.main()
