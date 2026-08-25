class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        if not nums:
            return nums
        for i in nums:
            dict1[i] = dict1.get(i,0) + 1
        arr = [[] for i in range(len(nums)+1)]

        for c,v in dict1.items():
            arr[v].append(c)
        top = []

        for i in range(len(arr)-1,0,-1):
            for num in arr[i]:
                top.append(num)
                if len(top) == k:
                    return top