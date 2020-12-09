'''
给定一个字符串，逐个翻转字符串中的每个单词。
示例 1：
输入: "the sky is blue"
输出: "blue is sky the"
示例 2：
输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
示例 3：
输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
 
说明：

无空格字符构成一个单词。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
'''


class Solution:
    def reverseWords(self, s: str) -> str:
        s = s[::-1].replace('  ', ' ').strip()
        r = ''
        count = 0
        cur = 0
        part=''
        while cur < len(s):
            if s[cur] != ' ':
                count += 1
            elif s[cur] == ' ' and r == '':
                r = r+s[cur-1::-1]+' '
                count = 0
            elif s[cur] == ' ' and r != '':
                r = r+s[cur-1:cur-1-count:-1]+' '
                count = 0
            cur += 1
        if count != 0:
            part += s[len(s)-1:len(s)-1-count:-1]
            if part == '':
                part += s[len(s)-1::-1]
        r += part
        return r.replace('  ', ' ').strip()



s = Solution()
ss = "a good   example"
print(s.reverseWords(ss))
