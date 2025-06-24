class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        right=n-1
        left=0
        sum=0
        while left<right:
            sum=numbers[left]+numbers[right]
            if(sum==target):
                return (left+1,right+1)
            elif (sum<target):
                left+=1
            else:
                right-=1
        return []
            
                