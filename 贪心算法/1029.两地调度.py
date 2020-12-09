'''
公司计划面试 2N 人。第 i 人飞往 A 市的费用为 costs[i][0]，飞往 B 市的费用为 costs[i][1]。
返回将每个人都飞到某座城市的最低费用，要求每个城市都有 N 人抵达。

示例：
输入：[[10,20],[30,200],[400,50],[30,20]]
输出：110
解释：
第一个人去 A 市，费用为 10。
第二个人去 A 市，费用为 30。
第三个人去 B 市，费用为 50。
第四个人去 B 市，费用为 20。
最低总费用为 10 + 30 + 50 + 20 = 110，每个城市都有一半的人在面试。
 
提示：
1 <= costs.length <= 100
costs.length 为偶数
1 <= costs[i][0], costs[i][1] <= 1000
'''
# 题解tips：
# 二维数组按某种方法排序（这里是按差值排序）costs.sort(key = lambda x : x[0] - x[1])

from typing import List


# class Solution:
#     def twoCitySchedCost(self, costs: List[List[int]]) -> int:
#         diff = [abs(d[0]-d[1]) for d in costs]
#         arr = []
#         for _ in range(len(costs)):
#             index = diff.index(max(diff))
#             arr.append(costs[index])
#             del diff[index]
#             del costs[index]
#         res = 0
#         a_counts = 0
#         for i in range(len(arr)):
#             if arr[i][0] <= arr[i][1] and a_counts < len(arr)//2:
#                 res += arr[i][0]
#                 a_counts += 1
#             else:
#                 res += arr[i][1]
#             if a_counts == len(arr)//2 or i+1-a_counts == len(arr)//2:
#                 break
#         if a_counts == len(arr)//2:
#             res += sum([d[1] for d in arr[i+1:]])
#         else:
#             res += sum([d[0] for d in arr[i+1:]])
#         return res


# 简化代码
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0]-x[1])
        res = sum([d[1] for d in costs])
        for i in range(len(costs)//2):
            res += costs[i][0]-costs[i][1]
        return res

s = Solution()
costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
print(s.twoCitySchedCost(costs))
