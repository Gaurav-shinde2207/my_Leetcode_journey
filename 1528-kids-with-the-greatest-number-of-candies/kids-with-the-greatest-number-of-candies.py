class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        sol=[]
        for i in range(len(candies)):
            sol.append(candies[i]+extraCandies>= max(candies))
        

        return sol
            
        