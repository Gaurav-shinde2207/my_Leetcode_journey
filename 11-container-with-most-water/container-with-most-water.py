class Solution:
    def maxArea(self, height: List[int]) -> int:
        L=0
        R=len(height)-1
        max_area=0
        while L<R:
            H=min(height[L],height[R])
            W=R-L
            area=H*W
            max_area=max(max_area,area)
            if height[L]<height[R]:
                L+=1
            else:
                R-=1
        return max_area

        