class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ''
        c = ''
        i = 0
        for ch in s:
            if ch != c:
                res += ch
                c = ch
                i = 1
            elif ch == c and i < 2:
                res += ch
                i += 1
        return res