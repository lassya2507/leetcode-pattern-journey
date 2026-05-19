from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(sol.maxSubArray([1]))                               # 1
    print(sol.maxSubArray([5, 4, -1, 7, 8]))                  # 23
    print(sol.maxSubArray([-3, -2, -5]))                      # -2
