class Solution:
    def sortColors(self, nums: List[int]) -> None:
        res = [0,0,0]
        for i in nums:
            res[i] +=1
        j=0
        for i,v in enumerate(res):
            for x in range(v):
                nums[j] = i
                j+=1
        return nums