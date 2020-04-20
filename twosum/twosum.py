"""
Given an array of integers, return indices of the two numbers such that they
add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
import unittest
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, number1 in enumerate(nums):
            for j, number2 in enumerate(nums[i: len(nums) + 1]):
                if i == i + j:
                    break
                if number1 + number2 == target:
                    return [j, i]


class Test(unittest.TestCase):
    def testExample(self):
        solution = Solution()
        result = solution.twoSum(nums=[2, 7, 11, 15], target=9)

        self.assertEqual(result, [0, 1])


if __name__ == "__main__":
    unittest.main()
