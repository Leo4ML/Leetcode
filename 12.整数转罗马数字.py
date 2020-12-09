class Solution:
    def intToRoman(self, num: int) -> str:
        arr = list(str(num))
        r = []
        n = len(arr)
        for i in range(len(arr)):
            r.append(int(arr[i])*(10**(n-1-i)))
        def roman(number,num):
            if num == '4' or num == '9':
                if len(str(number)) == 1:
                    res = 'IV' if num == '4' else 'IX'
                if len(str(number)) == 2:
                    res = 'XL' if num == '4' else 'XC'
                if len(str(number)) == 3:
                    res = 'CD' if num == '4' else 'CM'
                if len(str(number)) == 4:
                    res = 'CD' if num == '4' else 'CM'
