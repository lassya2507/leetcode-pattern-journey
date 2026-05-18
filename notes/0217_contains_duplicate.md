# Contains Duplicate

## Pattern
Set

## Constraints Thinking
If the input size is large, brute force pair comparison is too slow because it takes O(n²) time. A set is better because lookup is O(1) on average.

## Intuition
We need to know whether a number has appeared before. If it has appeared before, then the array contains a duplicate.

## Brute Force
Compare every pair of numbers using two nested loops. If `nums[i] == nums[j]`, return `True`.

## Brute Force Complexity
Time: O(n²)  
Space: O(1)

## Optimized Approach
Use a set to store numbers already seen.

For each number:
1. Check if it is already in the set
2. If yes, return `True`
3. Otherwise, add it to the set
4. After checking all numbers, return `False`

## Optimized Complexity
Time: O(n)  
Space: O(n)

## Mistakes I Made
- Compared `nums[i]` against `range(i + 1, len(nums))`, which checks a value against indices
- Initially thought brute force was O(n), but pair comparison is O(n²)
- Put `return False` too early inside the loop
- Did not know set insertion syntax at first
- Learned to use `seen.add(nums[i])`

## Recognition Cue
If the problem asks whether a value appears more than once, think set.

## Fix / Rule
Use a set when I only need to know whether something exists. Return `False` only after the full loop finishes.

## Interview Explanation
I use a set to track numbers I have already seen. As I scan the array, if the current number is already in the set, I return `True` because that means it appeared before. If not, I add it to the set. If the loop finishes, no duplicates were found, so I return `False`.

## Variation
If the problem asks for the duplicate value itself, the same set approach can return the number instead of `True`.