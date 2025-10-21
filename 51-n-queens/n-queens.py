class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        maze=[["." for _ in range(n)]for _ in range(n)]
        colset=set()
        lud,rud=set(),set()
        ans=[]
        def backtrack(row):
            if row==n:
                ans.append([''.join(r) for r in maze])
                return 
            for col in range(n):
                if col in colset or row-col in lud or row+col in rud:
                    continue
                maze[row][col]='Q'
                colset.add(col)
                lud.add(row-col)
                rud.add(row+col)
                backtrack(row+1)

                maze[row][col]='.'
                colset.remove(col)
                lud.remove(row-col)
                rud.remove(row+col)
        backtrack(0)
        return ans

            

                
