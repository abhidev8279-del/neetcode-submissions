class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i,v in enumerate(nums):
            tar = target - v
            if tar in dict1:
                return [dict1[tar],i]
            dict1[v] = i