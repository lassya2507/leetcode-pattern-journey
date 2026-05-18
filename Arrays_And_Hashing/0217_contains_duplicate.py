from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                return True

            seen.add(nums[i])

        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.containsDuplicate([1, 2, 3, 1]))  # True
    print(sol.containsDuplicate([1, 2, 3, 4]))  # False
    print(sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True
