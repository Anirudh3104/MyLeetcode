class Solution:
    def myAtoi(self, s: str) -> int:
        n=len(s)
        def check(s,i,num):
            if i>=n:return num
            if s[i]==" ":
                if num:return num
                return check(s,i+1,num) 
            elif  s[i]=="-":
                if not num:
                    return check(s,i+1,num+s[i])
                else:return num
            elif s[i]=="+":
                if not num:
                    return check(s,i+1,num+s[i])
                return num
            elif s[i].isdigit():
                return check(s,i+1,num+s[i])
            else:return num
             
        x=check(s,0,'')
        if not x or x in ('+','-'):
            return 0
        minn,maxx=-2**31,2**31-1
        x=int(x)
        if x>maxx:return maxx
        if x<minn:return minn
        return x      

        