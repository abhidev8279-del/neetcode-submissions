class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        if target > max(nums):
            return len(nums)
        elif target < min(nums):
            return 0
        else:
            while low<=high:
                mid = low+(high-low)//2
                if nums[mid]<target<nums[mid+1]:
                    return mid+1
                if nums[mid-1]<target<nums[mid]:
                    return mid
                elif nums[mid]==target:
                    return mid
                elif nums[mid] > target:
                    high = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
        return len(nums)

