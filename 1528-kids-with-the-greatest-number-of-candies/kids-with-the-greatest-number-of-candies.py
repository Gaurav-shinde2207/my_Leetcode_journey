class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        sol=[]
        for i in range(len(candies)):
            if (candies[i]+extraCandies>= max(candies)):
                sol.append(True)
            else:
                sol.append(False)

        return sol
            
        