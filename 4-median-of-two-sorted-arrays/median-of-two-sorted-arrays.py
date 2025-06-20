class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sol=nums1+nums2
        sol=sorted(sol)
        n=len(sol)
        mid=n//2
        if n%2==1:
            return sol[mid]
        else:
            return (sol[mid-1]+sol[mid])/2

        



        