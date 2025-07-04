class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        sol=[]
       
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1
            while j<k:
                curr=nums[i]+nums[j]+nums[k]
                if (curr==0):
                    sol.append([nums[i],nums[j],nums[k]])
                    while j<k and (nums[j]==nums[j+1]):
                        j+=1
                    while j<k and (nums[k]==nums[k-1]):
                        k-=1
                    j+=1
                    k-=1
                elif curr<0:
                    j+=1
                else:
                    k-=1
        return sol

            