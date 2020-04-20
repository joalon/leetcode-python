import unittest
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}

        for i, num in enumerate(nums):

            if str(target - num) in index_map:
                return [i, index_map[str(target - num)][0]]

            if str(num) not in index_map:
                index_map[str(num)] = [i]


class Tester(unittest.TestCase):
    def testPrint(self):
        solution = Solution()
        result = solution.twoSum(nums=[2, 7, 11, 15], target=9)
        result.sort()
        self.assertEqual(result, [0, 1])


if __name__ == "__main__":
    unittest.main()
