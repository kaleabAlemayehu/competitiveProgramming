class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = ('-', '+', '/', '*')
        stack = []
        for t in tokens:
            if t in op:
                rhs = stack.pop() 
                lhs = stack.pop() 
                res = 0
                match t:
                    case '+':
                        res = lhs + rhs
                    case '-':
                        res = lhs - rhs
                    case '/':
                        res = lhs / rhs
                    case '*':
                        res = lhs * rhs
                stack.append(int(res))
                continue
            stack.append(int(t))
        return stack.pop()

        