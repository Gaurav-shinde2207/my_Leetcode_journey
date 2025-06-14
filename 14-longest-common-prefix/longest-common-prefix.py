class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs=sorted(strs)
        sol=''
        f=strs[0]
        l=strs[-1]
        for i in range(len(min(f,l))):
            if (f[i]!=l[i]):
                return sol
            sol+=f[i]
        return sol        
