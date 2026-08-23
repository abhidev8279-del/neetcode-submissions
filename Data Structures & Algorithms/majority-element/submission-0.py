class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1 = {}
        n = len(nums)//2
        for i in nums:
            if i not in dict1:
                dict1[i] = 1
            else:
                dict1[i]+=1
        for key,value in dict1.items():
            if dict1[key]>n:
                return key
