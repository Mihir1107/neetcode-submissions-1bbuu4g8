class Solution:
    def isValid(self, s: str) -> bool:
        x = {
            "]":"[",
            "}":"{",
            ")":"("
        }
        stack = []
        for i in s:
            if i in x:
                top = stack.pop() if stack else "#"
                if x[i] != top:
                    return False
            else: stack.append(i)
        return len(stack) == 0