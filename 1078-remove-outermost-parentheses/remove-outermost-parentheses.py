class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        s_open=0
        res=[]
        for i in range(len(s)):
            if s[i]=="(":
                if s_open>0:
                    res.append("(")
                s_open+=1
            elif s[i]==")":
                s_open-=1
                if s_open>0:
                    res.append(")")
        return "".join(res)
