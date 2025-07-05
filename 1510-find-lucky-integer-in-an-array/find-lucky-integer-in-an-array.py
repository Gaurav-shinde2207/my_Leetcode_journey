class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq={}
        max_lucky=-1
        n=len(arr)
        for num in arr:
            freq[num]=freq.get(num,0)+1
            k=freq[num]
            max_lucky=max([k for k in freq if k==freq[k]],default=-1)

        return max_lucky        
