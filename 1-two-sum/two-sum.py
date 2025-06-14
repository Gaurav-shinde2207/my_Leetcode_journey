class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #declaring n as the length of the string
        n=len(nums)
        # i and j
        for i in range(n-1):
            for j in range (i+1,n):
                while nums[i] + nums[j]==target:
                    return [i,j]
        return[]                    