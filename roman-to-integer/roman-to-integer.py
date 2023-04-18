class Solution:
    def romanToInt(self, s: str) -> int:
        tot = 0
        for i in range(len(s)):
            num = self.numeral(s[i])
            if i == len(s) - 1:
                tot += num
                break
            elif num < self.numeral(s[i+1]):
                tot -= num
                continue
            else:
                tot += num
        return tot
    
    def numeral(self, l: str) -> int:
        if l == 'I':
            return 1
        elif l == 'V':
            return 5
        elif l == 'X':
            return 10
        elif l == 'L':
            return 50
        elif l == 'C':
            return 100
        elif l == 'D':
            return 500
        return 1000
        