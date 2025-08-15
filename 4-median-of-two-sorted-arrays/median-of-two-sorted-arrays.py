class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float: 
        m,n=len(nums1),len(nums2)
        def solve(k,a_start,a_end,b_start,b_end):
            if a_start>a_end:
                return nums2[k-a_start]
            if b_start>b_end:
                return nums1[k-b_start]
            a_index,b_index=(a_start+a_end)//2,(b_start+b_end)//2
            a_mid,b_mid=nums1[a_index],nums2[b_index]
            if a_index+b_index<k:
                if a_mid<=b_mid:
                    return solve(k,a_index+1,a_end,b_start,b_end)
                else:
                    return solve(k,a_start,a_end,b_index+1,b_end)
            else:
                if a_mid<=b_mid:
                    return solve(k,a_start,a_end,b_start,b_index-1)
                else:
                    return solve(k,a_start,a_index-1,b_start,b_end)
        if (m+n)%2:
            return solve((m+n)//2,0,m-1,0,n-1)
        else:
            return ( solve((m+n)//2-1,0,m-1,0,n-1)+solve((m+n)//2,0,m-1,0,n-1))/2
        # p1,p2=0,0
        # def get_min():
        #     nonlocal p1,p2
        #     if p1<m and p2<n:
        #         if nums1[p1]<nums2[p2]:
        #             ans=nums1[p1]
        #             p1+=1
        #         else:
        #             ans=nums2[p2]
        #             p2+=1
        #     elif p2==n:
        #         ans=nums1[p1]
        #         p1+=1
        #     else:
        #         ans=nums2[p2]
        #         p2+=1
        #     return ans
        # if (m+n)%2==0:
        #     for _ in range((m+n)//2-1):
        #         _=get_min()
        #     return (get_min()+get_min())/2
        # else:
        #     for _ in range((m+n)//2):
        #         _=get_min()
        #     return get_min()
