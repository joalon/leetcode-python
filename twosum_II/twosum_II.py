"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

    Your returned answers (both index1 and index2) are not zero-based.
    You may assume that each input would have exactly one solution and you may not use the same element twice.

Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""
import unittest
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i1, i2 = 0, len(numbers)-1

        currentTarget = numbers[i1] + numbers[i2]

        while currentTarget != target:
            if currentTarget > target:
                i2 -= 1
            elif  currentTarget < target:
                i1 += 1
            currentTarget = numbers[i1] + numbers[i2]

        return [i1+1, i2+1]


class TestSolution(unittest.TestCase):
    def testTwoSum(self):
        solution = Solution()
        result = solution.twoSum(numbers=[2, 7, 11, 15], target=9)
        self.assertEqual(result, [1, 2])


if __name__ == "__main__":
    unittest.main()
