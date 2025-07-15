class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        house1=0
        house2=0
        for i in nums:
            rob=house2+i
            skip=house1
            house2=house1
            house1=max(rob,skip)
        return house1
        