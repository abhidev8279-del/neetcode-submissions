class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        temp = arr[-1]
        for i in range(len(arr)-2,-1,-1):
            if temp>=arr[i+1]:
                if arr[i]>temp:
                    arr[i],temp = temp,arr[i]
                else:
                    arr[i] = temp
        arr[-1] = -1
        return arr