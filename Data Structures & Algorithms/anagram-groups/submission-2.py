class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return list(strs)
        else:
            s1 = [''.join(sorted(i)) for i in strs]
            dict1 = {}
            for i in s1:
                dict1[i] = []
            for i,v in enumerate(s1):
                if v in dict1:
                    dict1[v].append(strs[i])
            s2 = [value for key,value in dict1.items()]
            return s2