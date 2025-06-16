class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sol=[]
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for i in range (0,k):
            max_key=max(freq,key=freq.get)
            sol.append(max_key)
            freq.pop(max_key)
        return sol

            