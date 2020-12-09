'''
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n==0:
            return []
        if n==1:
            return ['()']
        tmp=[['(',')']]
        def insertp(n,tmp):
            if n==0:
                return tmp
            arr=[]
            for i in range(len(tmp)):
                for j in range(len(tmp[i])):
                    tmp[i].insert(j,')')
                    tmp[i].insert(j,'(')
                    if tmp[i] not in arr:
                        arr.append(list(tmp[i]))
                    tmp[i].pop(j)
                    tmp[i].pop(j)
                    tmp[i].insert(j,'(')
                    tmp[i].insert(j+2,')')
                    if tmp[i] not in arr:
                        arr.append(list(tmp[i]))
                    tmp[i].pop(j+2)
                    tmp[i].pop(j)
            return insertp(n-1,arr)
        r = insertp(n-1,tmp)
        result=[]
        for i in r:
            result.append(''.join(i))
        return result

s = Solution()
print(s.generateParenthesis(4))



# print(permutations([1,2,3],0,3))
