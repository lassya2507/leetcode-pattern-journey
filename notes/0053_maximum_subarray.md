# Maximum Subarray

## Pattern
Kadane's Algorithm / Greedy DP

## Constraints Thinking
A brute force approach checks many possible subarrays, which can take O(n²) or worse. Since the input can be large, we need a one-pass solution.

## Intuition
At each number, I decide whether to extend the previous subarray or start a new subarray from the current number.

## Brute Force
Try every possible start and end index, calculate each subarray sum, and track the maximum.

## Brute Force Complexity
Time: O(n²) or O(n³), depending on implementation  
Space: O(1)

## Optimized Approach
Use Kadane's Algorithm.

Track:
- `current_sum`, the best subarray sum ending at the current index
- `max_sum`, the best subarray sum found anywhere so far

For each number:
1. Set `current_sum = max(num, current_sum + num)`
2. Set `max_sum = max(max_sum, current_sum)`

## Dynamic Programming Explanation
DP means Dynamic Programming. Here, the current answer depends on the previous state.

The recurrence is:

`dp[i] = max(nums[i], dp[i - 1] + nums[i])`

Instead of storing a full DP array, we only store the previous value in `current_sum`.

## Greedy Explanation
If the previous running sum is negative or harmful, we drop it and start fresh from the current number. This is greedy because we make the best local decision at each index.

## Optimized Complexity
Time: O(n)  
Space: O(1)

## Mistake I Made
I initially tried to use a dictionary and list, but this problem does not need lookup, counting, or previous indices. I also thought about returning the whole subarray, but the problem asks only for the maximum sum.

## Recognition Cue
If the problem asks for the maximum sum of a contiguous subarray, think Kadane's Algorithm.

## Fix / Rule
Use `current_sum` for the best sum ending here and `max_sum` for the best sum anywhere so far.

## Interview Explanation
I use Kadane's Algorithm. At every number, I decide whether to start a new subarray from that number or extend the previous subarray. Then I update the global maximum. This works in O(n) time and O(1) space because I only keep two variables.

## Variation
If the problem asks to return the actual subarray, we also track start and end indices.