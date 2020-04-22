import unittest
from typing import List


class Solution:
    def countingElements(self, nums: List[int]) -> int:
        existing = {}
        result = 0

        for num in nums:
            strNum = str(num)

            if strNum in existing:
                existing[strNum] += 1
            else:
                existing[strNum] = 1

        for strNum in existing.keys():
            numberOfNums = existing[strNum]
            for i in range(int(numberOfNums)):
                incStr = str(int(strNum)+1)
                if incStr in existing.keys():
                    if existing[incStr]:
                        result += 1

        return result


class Tester(unittest.TestCase):
    def testCountingElements(self):
        testList = [1, 1, 2, 2]
        result = Solution().countingElements(testList)
        self.assertEqual(2, result)

    def testCountingElements2(self):
        testList = [1, 1, 3, 3, 5, 5, 7, 7]
        result = Solution().countingElements(testList)
        self.assertEqual(0, result)

    def testCountingElements3(self):
        testList = [1, 3, 2, 3, 5, 0]
        result = Solution().countingElements(testList)
        self.assertEqual(3, result)

    def testCountingElements4(self):
        testList = [1, 2, 3]
        result = Solution().countingElements(testList)
        self.assertEqual(2, result)


if __name__ == "__main__":
    unittest.main()
