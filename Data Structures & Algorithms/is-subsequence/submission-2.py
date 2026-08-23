class Solution:
    def isSubsequence(self, s: str, t: str) -> bool: 
        k=0
        if s == "": return True
        else:
            for c in t:
                if k==len(s): return True
                if s[k]==c: k+=1
        return k==len(s)