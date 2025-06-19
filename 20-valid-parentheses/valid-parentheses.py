class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        par_map={')':'(',']':'[','}':'{'}
        for par in s:
            if par in par_map.values():
                stack.append(par)
            elif par in par_map:
                if not stack or stack.pop() != par_map[par]:
                    return False
        return not stack

        