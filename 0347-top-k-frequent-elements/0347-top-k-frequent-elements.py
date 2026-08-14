class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {} # num -->count
        for i in range(len(nums)):
            if nums[i] in seen:
                seen[nums[i]]+=1
            else:
                seen[nums[i]]=1
        pairs = sorted(seen.items(), key=lambda x: x[1], reverse = True)
        result = []
        for pair in pairs[0:k]: # 1-3,2-2
            result.append(pair[0]) 
        return result