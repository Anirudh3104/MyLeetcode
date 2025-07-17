class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos=[[p,s] for p,s in zip(position,speed)]
        pos=sorted(pos,key=lambda x:x[0],reverse=True)
        stack=[]
        for p,s in pos:
            time=(target-p)/s
            stack.append(time)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)
        