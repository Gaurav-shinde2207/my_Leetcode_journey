class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        n=len(nums)
        sol=[]
        def backtrack(start,path):
            sol.append(path[:])
            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrack(i+1,path)
                path.pop()

        backtrack(0,[])  
        return sol      
            

        