class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        openings = {'(', '{', '['}
        hm = {
            '(':')',
            '{': '}',
            '[':']'
        }
        stack = []
        for c in s:
            if c in openings:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if c != hm[stack[-1]]:
                    return False
                stack = stack[:len(stack)- 1]
        if len(stack) != 0:
            return False
        return True

        