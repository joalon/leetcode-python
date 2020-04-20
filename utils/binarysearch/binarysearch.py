import unittest
from typing import List


def binarySearch(num: int, numbers: List[int]) -> int:
    return _binarySearch(num, numbers, 0, len(numbers) - 1)


def _binarySearch(num, numbers, left, right):
    mid = int(left + (right - left) / 2)

    if numbers[mid] == num:
        return mid
    elif numbers[mid] > num:
        return _binarySearch(num, numbers, left, mid)
    elif numbers[mid] < num:
        return _binarySearch(num, numbers, mid, right)
    else:
        pass


class Tester(unittest.TestCase):
    def test_BinarySearch(self):

        indexOf2 = _binarySearch(2, [1, 2, 3, 4, 5], 0, 4)
        indexOf4 = _binarySearch(4, [1, 2, 3, 4, 5], 0, 4)

        self.assertEqual(1, indexOf2)
        self.assertEqual(3, indexOf4)

    def testBinarySearch(self):
        testList = list(range(1, 100))

        indexOf40 = binarySearch(40, testList)

        self.assertEqual(39, indexOf40)


if __name__ == "__main__":
    unittest.main()
