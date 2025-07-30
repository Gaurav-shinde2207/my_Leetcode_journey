class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1=len(word1)
        len2=len(word2)
        min_len=min(len1,len2)
        merged=""
        for i in range(min_len):
            merged+=word1[i]+word2[i]
        if len1>len2:
            merged+=word1[min_len:]
        else:
            merged+=word2[min_len:]
        return merged    
