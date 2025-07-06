class Solution:
    def climbStairs(self, n: int) -> int:
        from functools import lru_cache
        k=n
        @lru_cache(maxsize=None)
        def stairs(k):
            if k==0 or k==1:
                return 1
            else:
                return stairs(k-1)+stairs(k-2)
        return stairs(n)
        