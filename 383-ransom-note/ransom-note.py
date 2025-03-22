class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        if ransomNote in magazine:
            return True
        for s in ransomNote:
            if s not in magazine:
                return False
            magazine = magazine.replace(s, "", 1)
        return True
        