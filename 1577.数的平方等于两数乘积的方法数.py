#
# @lc app=leetcode.cn id=1577 lang=python3
#
# [1577] 数的平方等于两数乘积的方法数
#

# @lc code=start
class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        num11 = []  #nums1的平方数
        num22 = []  #nums2的平方数
        num111 = {}  #nums1的任意两元素的乘积，key为乘积值，value为内部元素乘积相等的次数
        num222 = {}  #num2的任意两元素的乘积，key为乘积值，value为内部元素乘积相等的次数
        res = 0  #记录次数
        for i in nums1:
            num11.append(i**2)
        for j in nums2:
            num22.append(j**2)
        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                num111[nums1[i] *
                       nums1[j]] = num111.get(nums1[i] * nums1[j], 0) + 1
        for i in range(len(nums2)):
            for j in range(i + 1, len(nums2)):
                num222[nums2[i] *
                       nums2[j]] = num222.get(nums2[i] * nums2[j], 0) + 1
        for i in range(len(num11)):
            if num11[i] in num222.keys():
                res += num222[num11[i]]
        for i in range(len(num22)):
            if num22[i] in num111.keys():
                res += num111[num22[i]]
        return res
# @lc code=end
