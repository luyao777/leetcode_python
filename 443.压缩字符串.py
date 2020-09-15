#
# @lc app=leetcode.cn id=443 lang=python3
#
# [443] 压缩字符串
#

# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1
        pre_char = chars[0]
        same_num = 1
        i = 1
        while(i < len(chars)):
            if chars[i] == pre_char:
                chars.pop(i)
                same_num += 1
            else:
                pre_char = chars[i]
                if same_num == 1:
                    i += 1
                    continue
                num_str = str(same_num)
                for j in range(len(num_str)-1, -1, -1):
                    chars.insert(i, num_str[j])
                same_num = 1
                i += len(num_str) + 1
        if same_num > 1:
            num_str = str(same_num)
            for j in range(len(num_str)-1, -1, -1):
                chars.insert(i, num_str[j])
        return len(chars)

# @lc code=end

