class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            return True
        elif x < 100 and x % 11 == 0:
            return True
        
        y = str(x)
        a = 0
        b = len(y) - 1
        
        while b > a:
            if y[a] != y[b]:
                return False
            b -= 1
            a += 1
        return True
        