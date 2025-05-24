class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        closings = {
            ')':'(',
            '}': '{',
            ']':'['
        }
        stack = []
        for c in s:
            if c in closings:
                if stack and stack[-1] == closings[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if stack:
            return False
        return True

        