'''
@Author: Yao Lu
@Date: 2019-11-06 14:49:56
@Description: 
'''
#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:
    import sys
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []


    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.min_stack == []:
            self.min_stack.append(x)
        elif x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        num = self.stack.pop()
        if num == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

