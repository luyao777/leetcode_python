#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#


# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        nums1_list = [int(i) for i in num1]
        nums2_list = [int(i) for i in num2]

        result_sum = [0]

        for i in range(1, len(nums1_list) + 1):
            _result = [nums1_list[-i] * x for x in nums2_list]

            d = 0
            for j in range(1, len(_result) + 1):
                if (_result[-j] + d) // 10 > 0:
                    _d = d
                    d = (_result[-j] + d) // 10
                    _result[-j] = (_result[-j] + _d) % 10
                else:
                    _result[-j] += d
                    d = 0
            if d > 0:
                _result.insert(0, d)

            for j in range(i - 1):
                _result.append(0)

            result = _result if len(_result) > len(result_sum) else result_sum

            length = min(len(_result), len(result_sum))
            for j in range(1, length + 1):
                result[-j] = result_sum[-j] + _result[-j]
            result_sum = result

        d = 0
        for i in range(1, len(result_sum) + 1):
            if (result_sum[-i] + d) // 10 > 0:
                _d = d
                d = (result_sum[-i] + d) // 10
                result_sum[-i] = (result_sum[-i] + _d) % 10
            else:
                result_sum[-i] += d
                d = 0
        if d > 0:
            result_sum.insert(0, d)

        result_str = ""
        for i in range(len(result_sum)):
            result_str += str(result_sum[i])

        return result_str


# @lc code=end
