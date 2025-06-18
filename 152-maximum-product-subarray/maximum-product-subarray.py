class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        min_pro=nums[0]
        max_pro=nums[0]
        result=nums[0]

        for num in nums[1:]:
            temp_max=max(num,max_pro*num,min_pro*num)
            temp_min=min(num,max_pro*num,min_pro*num)
            max_pro=temp_max
            min_pro=temp_min
            result=max(result,max_pro)
        return result
