'''
@Author: Yao Lu
@Date: 2019-11-06 19:29:19
@Description: 
'''
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int(bin(n)[2:].zfill(32)[::-1], base=2)