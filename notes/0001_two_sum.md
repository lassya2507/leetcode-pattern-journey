# Two Sum

## Pattern
Hash Map

## Intuition
For each number, I need another number that adds with it to reach the target. That needed number is the complement.

## Brute Force
Check every pair using two nested loops. If `nums[i] + nums[j] == target`, return `[i, j]`.

## Brute Force Complexity
Time: O(n²)  
Space: O(1)

## Optimized Approach
Use a dictionary to store numbers already seen with their indices.

The dictionary stores:

`number -> index`

For each number:
1. Calculate `other = target - nums[i]`
2. Check if `other` is already in the dictionary
3. If yes, return `[seen[other], i]`
4. Otherwise, store the current number with its index

## Optimized Complexity
Time: O(n)  
Space: O(n)

## Mistakes I Made
- Confused `num` and `nums`
- Used `i` before defining it
- Initially checked only adjacent elements
- Returned a tuple instead of a list
- Confused complement value with index
- Wanted to store the complement instead of the current number
- Did not fully understand `seen[nums[i]] = i`

## Recognition Cue
If the problem asks for two values that add to a target and asks for indices, think hash map.

## Fix / Rule
Store what I have already seen, not what I am looking for.

## Interview Explanation
I use a hash map to store numbers I have already seen with their indices. For each number, I compute the complement needed to reach the target. If the complement already exists in the map, I return its stored index and the current index. Otherwise, I store the current number and continue. This gives O(n) time because each lookup is O(1) on average.

## Variation
If the input array is sorted, the problem can be solved using two pointers instead of a hash map.