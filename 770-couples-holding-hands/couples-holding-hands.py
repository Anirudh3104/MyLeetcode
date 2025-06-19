class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        pos={person:index for index,person in enumerate(row)}
        swaps=0
        for i in range(0,len(row),2):
            first=row[i]
            exp_part=first^1
            if row[i+1]!=exp_part:
                part_ind=row.index(exp_part)
                pos[row[i+1]]=part_ind
                pos[row[part_ind]]=i+1
                row[i+1],row[part_ind]=row[part_ind],row[i+1]
                swaps+=1
            else:
                continue
        return swaps
        
            


        