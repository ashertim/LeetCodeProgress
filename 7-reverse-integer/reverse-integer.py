class Solution:
    def reverse(self, x: int) -> int:
        y = str(x)
        y = y[::-1]
        if x < 0:
            y = y[:-1]
            y = "-" + y
        try:
            y = int(y)
        except:
            return 0
        if y > pow(2, 31) - 1 or y < -(pow(2,31)):
            return 0
        return y
        