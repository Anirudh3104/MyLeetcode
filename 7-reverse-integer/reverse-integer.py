class Solution:
    def reverse(self, x: int) -> int:
        y=str(x)
        if x<0:
            y=y[:0:-1]
            y=-int(y)
            return y if -2**31<=y<=2**31-1 else 0
        y=int(y[::-1])
        return y if -2**31<=y<=2**31-1 else 0