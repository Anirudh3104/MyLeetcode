class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:return False
        if n==1:return True
        def isit(n,x):
            if 2**x>n:return False
            if 2**x==n:return True
            return isit(n,x+1)
        return isit(n,1)
        




        