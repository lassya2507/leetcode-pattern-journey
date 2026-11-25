class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {} # k:v is number:index 
        for i in range(len(nums)):
            new = target - nums[i]
            if new in seen:
                return [seen[new],i]
            seen[nums[i]] = i

