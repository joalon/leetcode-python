import unittest


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        left_parens = ['[', '(', '{']

        depth = 0
        for c in s:
            if c in left_parens:
                stack.append(c)
                depth += 1
            else:
                if len(stack) == 0 or c != getOtherParen(stack.pop()):
                    return False
                else:
                    depth -= 1

        return depth == 0


def getOtherParen(char):
    left_parens = ['[', '(', '{']
    right_parens = [']', ')', '}']
    for i in range(len(right_parens)):
        if char == left_parens[i]:
            return right_parens[i]


class Tester(unittest.TestCase):
    def test(self):
        string = "()()"
        self.assertEqual(True, Solution().isValid(string))
        string = ""
        self.assertEqual(True, Solution().isValid(string))
        string = "]"
        self.assertEqual(False, Solution().isValid(string))
        string = "("
        self.assertEqual(False, Solution().isValid(string))
        string = "([])"
        self.assertEqual(True, Solution().isValid(string))
        string = "([]"
        self.assertEqual(False, Solution().isValid(string))


if __name__ == '__main__':
    unittest.main()
