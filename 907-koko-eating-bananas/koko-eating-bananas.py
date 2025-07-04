class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        n=len(piles)
        
        while low<high:
            mid=(low+high)//2
            max_hours=0

            for pile in piles:
                max_hours+=ceil(pile/mid)
            if max_hours>h:
                low=mid+1
            else:
                high=mid
        return low


