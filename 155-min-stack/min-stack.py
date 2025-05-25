class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minstack = []

        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.stack) == 0:
            self.stack.append(val)
            self.minstack.append(val)
        elif val < self.minstack[len(self.minstack)-1]:
            self.stack.append( val)
            self.minstack.append(val)
        else:
            self.stack.append(val)
            self.minstack.append(self.minstack[len(self.minstack)-1])

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minstack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack) - 1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[len(self.minstack) - 1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()