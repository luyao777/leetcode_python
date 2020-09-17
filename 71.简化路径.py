#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        if len(path) == 0:
            return path
        elif len(path) == 1:
            return '/'

        result_stack = []
        contents = path.split('/')

        for i in range(len(contents)):
            if contents[i] == '':
                continue
            elif contents[i] == '.':
                continue
            elif contents[i] == '..':
                if len(result_stack) == 0:
                    continue
                result_stack.pop()
            else:
                result_stack.append(contents[i])

        result = '/'
        if len(result_stack) > 0:
            for c in result_stack[:-1]:
                result += c+'/'
            result += result_stack[-1]
        return result

# @lc code=end