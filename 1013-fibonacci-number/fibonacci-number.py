class Solution:
    def fib(self, n: int) -> int:
        a=0
        b=1
        next=0
        if n==0:
            return a
        for _ in range (2,n+1):
            next=a+b
            a=b
            b=next
            
        return b if n>0 else a
        