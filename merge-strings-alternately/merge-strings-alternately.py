class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge = ""
        i = 0
        while i < len(word1):
            merge += word1[i]
            if i < len(word2):
                merge += word2[i]
            i += 1
        while i < len(word2):
            merge += word2[i]
            i += 1
        return merge
        