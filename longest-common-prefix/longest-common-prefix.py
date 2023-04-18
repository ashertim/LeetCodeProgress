class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        short = strs[0]
        for s in strs:
            if len(s) < len(short):
                short = s
        
        l = len(short)
        while l > 0:
            pref = short[0:l]
            for s in range(len(strs)):
                if pref not in strs[s][0:l]:
                    l -= 1
                    break
                if s == len(strs)-1 and pref in strs[s][0:l]:
                    return pref
        return ''
            