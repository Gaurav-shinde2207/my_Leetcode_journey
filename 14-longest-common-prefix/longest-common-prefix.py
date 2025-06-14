class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs=sorted(strs)
        f=strs[0]
        l=strs[-1]
        sol=''
        for i in range (min(len(f),len(l))):
            if f[i]!=l[i]:
                return sol
            sol=sol+f[i]
        return sol        
