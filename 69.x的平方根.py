'''
实现 int sqrt(int x) 函数。
计算并返回 x 的平方根，其中 x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:
输入: 4
输出: 2
示例 2:
输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
'''


class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        start = 1
        end = x
        while start+1!=end:
            mid = start+(end-start)//2
            if mid**2>x:
                end = mid
            if mid**2<x:
                start = mid
            if mid**2==x:
                break
        return start

s = Solution()
x = 10
print(s.mySqrt(x))
