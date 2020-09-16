#
# @lc app=leetcode.cn id=165 lang=python3
#
# [165] 比较版本号
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1_num = list(map(int, version1.split('.')))
        ver2_num = list(map(int, version2.split('.')))

        i = len(ver1_num) - 1
        while(not ver1_num[i]):
            ver1_num.pop(-1)
            i -= 1
            if not len(ver1_num):
                break

        i = len(ver2_num) - 1
        while(not ver2_num[i]):
            ver2_num.pop(-1)
            i -= 1
            if not len(ver2_num):
                break

        ver1_len = len(ver1_num)
        ver2_len = len(ver2_num)

        min_len = min(ver1_len, ver2_len)

        for i in range(min_len):
            if ver1_num[i] > ver2_num[i]:
                return 1
            elif ver1_num[i] < ver2_num[i]:
                return -1

        if ver1_len > ver2_len:
            return 1
        elif ver1_len < ver2_len:
            return -1
        else:
            return 0
# @lc code=end

