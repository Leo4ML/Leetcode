'''
给你一个字符串 croakOfFrogs，它表示不同青蛙发出的蛙鸣声（字符串 "croak" ）的组合。由于同一时间可以有多只青蛙呱呱作响，
所以 croakOfFrogs 中会混合多个 “croak” 。请你返回模拟字符串中所有蛙鸣所需不同青蛙的最少数目。

注意：要想发出蛙鸣 "croak"，青蛙必须 依序 输出 ‘c’, ’r’, ’o’, ’a’, ’k’ 这 5 个字母。如果没有输出全部五个字母，
那么它就不会发出声音。
如果字符串 croakOfFrogs 不是由若干有效的 "croak" 字符混合而成，请返回 -1 。

示例 1：
输入：croakOfFrogs = "croakcroak"
输出：1 
解释：一只青蛙 “呱呱” 两次

示例 2：
输入：croakOfFrogs = "crcoakroak"
输出：2 
解释：最少需要两只青蛙，“呱呱” 声用黑体标注
第一只青蛙 "crcoakroak"
第二只青蛙 "crcoakroak"

示例 3：
输入：croakOfFrogs = "croakcrook"
输出：-1
解释：给出的字符串不是 "croak" 的有效组合。

示例 4：
输入：croakOfFrogs = "croakcroa"
输出：-1
 
提示：
1 <= croakOfFrogs.length <= 10^5
字符串中的字符只有 'c', 'r', 'o', 'a' 或者 'k'
'''
# 参考别人的题解
# 多个if 没有多个elif速度快
# 每次遍历过程中当且仅当c>=r>=o>=a>=k时才符合要求。
# now表示当前存在的青蛙个数，即遇到c时加一，叫完以后(遇到k)减一。
# 遍历完后now应为0表示每次叫声都有头有尾，记录now的最大值即为答案。
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        c = r = o = a = k = 0
        now = 0
        result = 0
        for num in croakOfFrogs:
            if num == 'c':
                c += 1
                now += 1
                result = max(now, result)
            elif num == 'r':
                r += 1
            elif num == 'o':
                o += 1
            elif num == 'a':
                a += 1
            elif num == 'k':
                k += 1
                now -= 1
            if not c >= r >= o >= a >= k:
                return -1
        if now != 0:
            return -1
        else:
            return result
                
s = Solution()
croakOfFrogs = "croakcroa"
print(s.minNumberOfFrogs(croakOfFrogs))
