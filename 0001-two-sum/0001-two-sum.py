class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # number --> index 
        for i in range(len(nums)):
            new = target - nums[i]
            if new in seen:
                return [seen[new],i]
            seen[nums[i]]=i