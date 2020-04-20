"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next_in=None):
        self.val = x
        self.next = next_in

    def __eq__(self, other):
        if other is not None:
            return False
        return self.val == other.val and self.next == other.next


def reverseLinkedList(root: ListNode) -> ListNode:
    lastNode = None
    currentNode = root
    nextNode = root.next
    while currentNode.next is not None:
        nextNode = currentNode.next

        # Reverse
        currentNode.next = lastNode

        # Save current nodes
        lastNode = currentNode

        # Step to nextNode
        currentNode = nextNode

    return currentNode


#def _reverseLinkedList(currentNode: ListNode, lastNode: ListNode) -> ListNode:
#    if currentNode.next == None:
#        currentNode.next = lastNode
#        return currentNode
#
#    newHead = _reverseLinkedList(currentNode.next, currentNode)
#    currentNode.next = lastNode
#    return currentNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pass


class TestSolution(unittest.TestCase):
    def testAddTwoNumbers(self):
        solution = Solution()
        list1 = ListNode(2, ListNode(4, ListNode(3)))
        list2 = ListNode(5, ListNode(6, ListNode(4)))
        result = solution.addTwoNumbers(l1=list1, l2=list2)

        expected = ListNode(7, ListNode(0, ListNode(8)))

        self.assertEqual(result, expected)

    def testEqual(self):
        list1 = ListNode(2, ListNode(4, ListNode(3)))
        list2 = ListNode(2, ListNode(4, ListNode(3)))

        self.assertEqual(list1, list2)

    def testReverse(self):
        list1 = ListNode(2, ListNode(4, ListNode(3)))
        reversedll = reverseLinkedList(list1)
        self.assertEqual(True, list1 == reverseLinkedList(reversedll))


if __name__ == "__main__":
    unittest.main()
