'''
给定由 N 个小写字母字符串组成的数组 A，其中每个字符串长度相等。
你需要选出一组要删掉的列 D，对 A 执行删除操作，使 A 中剩余的每一列都是 
非降序 排列的，然后请你返回 D.length 的最小可能值。
删除 操作的定义是：选出一组要删掉的列，删去 A 中对应列中的所有字符，形式
上，第 n 列为 [A[0][n], A[1][n], ..., A[A.length-1][n]]）。（可以参见 删除操作范例）


示例 1：
输入：["cba", "daf", "ghi"]
输出：1
解释：
当选择 D = {1}，删除后 A 的列为：["c","d","g"] 和 ["a","f","i"]，均为非降序排列。
若选择 D = {}，那么 A 的列 ["b","a","h"] 就不是非降序排列了。

示例 2：
输入：["a", "b"]
输出：0
解释：D = {}

示例 3：
输入：["zyx", "wvu", "tsr"]
输出：3
解释：D = {0, 1, 2}
 

提示：
1 <= A.length <= 100
1 <= A[i].length <= 1000
 
删除操作范例：
比如，有 A = ["abcdef", "uvwxyz"]，
要删掉的列为 {0, 2, 3}，删除后 A 为["bef", "vyz"]， A 的列分别为["b","v"], ["e","y"], ["f","z"]。
'''

# 这一题不论是否先转换为数字矩阵，运行时间和内存占用都一样的
# 笔记
# 1. python中字母之间是可以直接比大小的，所以这里不用ord函数转ascii码来比较大小，很多余；
# 2. 学会用any和zip语法，使代码更简洁；
# 
# class Solution(object):
#     def minDeletionSize(self, A):
#         ans = 0
#         for col in zip(*A):
#             if any(col[i] > col[i+1] for i in xrange(len(col) - 1)):
#                 ans += 1
#         return ans
from typing import List


class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        # matrix = self.letter2Num(A)
        matrix = A
        r = 0
        for i in range(len(matrix[0])):
            cur = 0
            for j in range(len(matrix)):
                if ord(matrix[j][i]) >= cur:
                    cur = ord(matrix[j][i])
                else:
                    r += 1
                    break
        return r

    # def letter2Num(self, arr):
    #     matrix = []
    #     for s in arr:
    #         tmp = []
    #         for i in s:
    #             tmp.append(ord(i))
    #         matrix.append(tmp)
    #     return matrix


s = Solution()
A = ["zyx", "wvu", "tsr"]
print(s.minDeletionSize(A))
