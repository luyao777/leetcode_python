#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d_dict={
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        ans_a = []
        ans_b = []
        for d in digits:
            if ans_a == []:      
                for s in d_dict[d]:
                    ans_a.append(s)
            else:
                for s in d_dict[d]:
                    for i in range(len(ans_a)):
                        ans_b.append(ans_a[i] + s)
            if ans_b != []:
                ans_a = ans_b
                ans_b = []
        return ans_a


# @lc code=end

