import unittest
from typing import List
from enum import Enum


class SearchFor(Enum):
    FIRST = 0
    LAST = 1


def binarySearch(num: int, numbers: List[int]) -> int:
    firstIndex = _binarySearch(num, numbers, 0, len(numbers) - 1, SearchFor.FIRST)
    if firstIndex is None:
        return []

    lastIndex = _binarySearch(num, numbers, 0, len(numbers) - 1, SearchFor.LAST)
    return list(range(firstIndex, lastIndex+1))


def _binarySearch(num, numbers, left, right, searchFor):
    mid = int(left + (right - left) / 2)

    if mid < left or mid > right:
        return None

    if numbers[mid] == num:
        if searchFor is SearchFor.FIRST and numbers[mid - 1] == num:
            return _binarySearch(num, numbers, left, mid - 1, searchFor)
        elif searchFor is SearchFor.LAST and numbers[mid + 1] == num:
            return _binarySearch(num, numbers, mid + 1, right, searchFor)
        else:
            return mid
    elif numbers[mid] < num:
        return _binarySearch(num, numbers, mid + 1, right, searchFor)
    elif numbers[mid] > num:
        return _binarySearch(num, numbers, left, mid - 1, searchFor)
    else:
        pass


class Tester(unittest.TestCase):
    def test_BinarySearchFirst(self):
        testList = [1, 2, 2, 2, 3, 4, 5]
        indexOf2 = _binarySearch(2, testList, 0, len(testList) - 1, SearchFor.FIRST)
        self.assertEqual(1, indexOf2)

    def test_BinarySearchLast(self):
        indexOf2 = _binarySearch(2, [1, 2, 2, 2, 3, 4, 5], 0, 5, SearchFor.LAST)
        self.assertEqual(3, indexOf2)

    def testBinarySearch(self):
        testList = list(range(1, 100))
        indexOf40 = binarySearch(40, testList)
        self.assertEqual([39], indexOf40)

    def testListOfOccurrences(self):
        testList = [1, 4, 4, 7, 7, 7, 7, 9, 10]
        result = binarySearch(7, testList)
        self.assertEqual([3, 4, 5, 6], result)

    def testNumberNotInList(self):
        testList = [1, 2, 3]
        indexOf10 = binarySearch(10, testList)
        self.assertEqual(indexOf10, [])


if __name__ == "__main__":
    unittest.main()
