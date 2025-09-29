class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:return 1
        if n<0:
            x=1/x
            n=abs(n)
            half=self.myPow(x,n//2)
        else:half=self.myPow(x,n//2)
        half*=half
        if n%2:
            return x*half
        return half
        