class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        sol=[]
        candidates.sort()
        def backtrack(comb,i,summ):
            if summ==target:
                sol.append(comb[:])
                return 
            if summ>target or i==n:return 
            comb.append(candidates[i])
            backtrack(comb,i+1,summ+candidates[i])
            comb.pop()
            while i+1<n and candidates[i+1]==candidates[i]:
                i+=1
            backtrack(comb,i+1,summ)
        backtrack([],0,0)
        return sol
                
                        
            
            
        