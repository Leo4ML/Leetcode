class Solution:
    def validPalindrome(self, s: str) -> bool:
        def huiwen(start, end, cnt):
            while start <= end:
                if s[start] == s[end]:
                    start += 1
                    end -= 1
                else:
                    cnt += 1
                    if cnt > 1:
                        return False
                    return huiwen(start, end-1, cnt) or huiwen(start+1, end, cnt)
            return True
        return huiwen(0, len(s)-1, 0)


s = Solution()
ss = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
print(s.validPalindrome(ss))
