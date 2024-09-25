# program1.py

class Solution:
    def isValid(self, s: str) -> bool:
        # Map of closing to opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []

        # Iterate through each character in the string
        for char in s:
            if char in bracket_map:  # Closing bracket
                top_element = stack.pop() if stack else None
                if bracket_map[char] != top_element:
                    return False
            else:  # Opening bracket
                stack.append(char)

        # If the stack is empty, all brackets are matched properly
        return not stack

# test_program1.py

import unittest
from program1 import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_valid_parentheses(self):
        self.assertTrue(self.solution.isValid("()"))
        self.assertTrue(self.solution.isValid("()[]{}"))
        self.assertTrue(self.solution.isValid("{[()]}"))

    def test_invalid_parentheses(self):
        self.assertFalse(self.solution.isValid("(]"))
        self.assertFalse(self.solution.isValid("([)]"))

    def test_empty_string(self):
        self.assertTrue(self.solution.isValid(""))

    def test_mixed_parentheses(self):
        self.assertFalse(self.solution.isValid("(){"))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


    



  






    



  

