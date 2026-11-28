class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if stack == []:
                    return False
                if stack[-1] == matching[char]:
                    stack.pop()
                else:
                    return False
        return not stack