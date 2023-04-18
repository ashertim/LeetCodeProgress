class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = current = i = 0
        sub = ""

        for c in s:
            i += 1
            if c not in sub:
                sub += c
                current += 1
                if current > longest:
                    longest += 1
            else:
                sub += c
                sub = sub[sub.find(c)+1:]
                current = len(sub)
        
        return longest

        