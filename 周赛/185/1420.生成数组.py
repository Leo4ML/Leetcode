'''
给你三个整数 n、m 和 k 。下图描述的算法用于找出正整数数组中最大的元素。
maximum_value = -1
maximum_index = -1
search_cost = 0
n = arr.length
for (i = 0; i < n; i++){
    if (maximum_value < arr[i]){
        maximum_value = arr[i]
        maximum_index = i
        search_cost = search_cost + 1
    }
}
return maximum_index
请你生成一个具有下述属性的数组 arr ：

arr 中有 n 个整数。
1 <= arr[i] <= m 其中 (0 <= i < n) 。
将上面提到的算法应用于 arr ，search_cost 的值等于 k 。
输入：n = 5, m = 2, k = 3
输出：0
解释：没有数组可以满足上述条件

示例 3：
输入：n = 9, m = 1, k = 1
输出：1
解释：可能的数组只有 [1, 1, 1, 1, 1, 1, 1, 1, 1]

示例 4：
输入：n = 50, m = 100, k = 25
输出：34549172
解释：不要忘了对 1000000007 取余

示例 5：
输入：n = 37, m = 17, k = 7
输出：418930126
 
提示：
1 <= n <= 50
1 <= m <= 100
0 <= k <= n
'''
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        