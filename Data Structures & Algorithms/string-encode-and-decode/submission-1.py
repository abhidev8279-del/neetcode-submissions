class Solution:

    def encode(self, strs: List[str]) -> str:
        strs1 = ""
        if not strs:
            return strs1
        for i in strs:
            strs1 += str(len(i)) + '#' + i
        return strs1
    

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        i,j = 0,0
        arr = []
        b = len(s)
        while True:
            if s[j]!= '#':
                j+=1
            elif s[j] == '#':
                length = int(s[i:j])
                arr.append(s[j+1:length+j+1])
                i = j+length+1
                j = i
                if i>=b:
                    return arr

