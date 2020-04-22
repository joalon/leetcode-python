import unittest
from typing import List


class Solution:
    def moveZeroesNew(self, nums: List[int]) -> None:
        numZeroes = 0
        newArray = []
        for i, num in enumerate(nums):
            if nums[i] == 0:
                numZeroes += 1
            else:
                newArray.append(num)

        for i in range(numZeroes):
            newArray.append(0)

        return newArray

    def moveZeroes(self, nums: List[int]) -> None:
        endIndex = len(nums) - 1
        for i in range(len(nums)):
            if nums[i] == 0 and i < endIndex:
                j = i
                while nums[j] == 0 and j < endIndex:
                    j += 1
                nums[i] = nums[j]
                nums[j] = 0


class Tester(unittest.TestCase):
    def testMoveZeroes(self):
        testList = [0, 1, 0, 3, 12]
        expectedResult = [1, 3, 12, 0, 0]

        Solution().moveZeroes(testList)

        self.assertEqual(testList, expectedResult)

    def testShortInput(self):
        testList = [0, 1]
        expected = [1, 0]

        Solution().moveZeroes(testList)

        self.assertEqual(testList, expected)


if __name__ == "__main__":
    unittest.main()
