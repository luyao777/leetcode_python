#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#


# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for str_i in strs:
            _ = sorted(str_i)
            strs_key = ""
            for i in _:
                strs_key += i

            if strs_key not in result.keys():
                result[strs_key] = [str_i]
            else:
                result[strs_key].append(str_i)
        total_result = []
        for key in result.keys():
            total_result.append(result[key])
        return total_result


# @lc code=end
