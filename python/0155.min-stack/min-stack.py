
"""
Core Idea:
1.Minimum value is always followed by the second minimum value (duplicate value of the second minimum value, to ensure that when pop function removes the 2nd min, it does not disrupt the stack order).
2.And while popping you pop min and 2nd min so that, you get the correct min value for the remaining stack and the remaining stack top also points to the right place.
"""


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = sys.maxint


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if (x <= self.min):
            self.stack.append(self.min)
            self.min = x
        self.stack.append(x)


    def pop(self):
        """
        :rtype: None
        """
        if self.stack.pop() == self.min:
            self.min = self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.min



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

