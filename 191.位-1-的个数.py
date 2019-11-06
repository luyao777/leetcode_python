'''
@Author: Yao Lu
@Date: 2019-11-06 19:35:17
@Description: hammingWeight
'''
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n)[2:].zfill(32).count('1')