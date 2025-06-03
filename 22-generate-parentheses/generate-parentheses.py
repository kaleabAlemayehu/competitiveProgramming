class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def backtrack(oc, cc):
            if oc == n and cc == n:
                res.append("".join(stack)) 
                return 
            if oc < n:
                stack.append("(")
                backtrack(oc+1, cc)
                stack.pop()
            if cc < oc:
                stack.append(")")
                backtrack(oc, cc+1)
                stack.pop()

        backtrack(0,0)
        return res

        