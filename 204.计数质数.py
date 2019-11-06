'''
@Author: Yao Lu
@Date: 2019-11-06 20:54:17
@Description: 
'''
#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        # 首先构造 0 到 n-1 的自然数列表，每个元素的下标对应每个自然数，元素值用于标记该元素下标是否为质数
        # 这样一来不用开辟内存用来存放大量的数字
        isPrime = [1] * n
        # 0 和 1 不是质数
        isPrime[0] = isPrime[1] = 0

        # 根据算术基本定理，任何一个合数，即非质数，都可以以唯一形式被写成质数的乘积，即分解质因数。
        # 埃式筛法：找出 2 到 根号n 的范围内的所有质数，将列表中所有它的倍数位设为0
        for i in range(2, int(n ** 0.5) + 1):
            if isPrime[i]:
                # 指定位置切片赋值，从它的平方开始，因为小于平方的倍数已经被之前的质数倍数排除了
                isPrime[i * i:n:i] = [0] * ((n - 1 - i * i) // i + 1)

        # 现在每个质数位的值为1，其余合数位的值为0，返回质数个数
        return sum(isPrime)


        
# @lc code=end

