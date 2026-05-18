# Product of Array Except Self

## Pattern
Prefix / Suffix Product

## Constraints Thinking
The problem asks for O(n) time and usually says not to use division. Brute force checks every index against every other index, which is O(n²), so we need prefix and suffix products.

## Intuition
For each index, the answer is:

product of everything before it * product of everything after it

## Brute Force
For each index `i`, scan the full array and multiply every `nums[j]` where `j != i`.

## Brute Force Complexity
Time: O(n²)  
Space: O(n) for output

## Optimized Approach
Use the output array to first store prefix products. Then scan from right to left with a running suffix product and multiply it into the output.

First pass:
- `answer[i] = prefix`
- `prefix *= nums[i]`

Second pass:
- `answer[i] *= suffix`
- `suffix *= nums[i]`

The order matters because the product should exclude `nums[i]`.

## Optimized Complexity
Time: O(n)  
Space: O(1) extra, O(n) including output

## Mistake I Made
I initially tried to multiply into the answer list instead of the running product variable. I also used the wrong backward loop step and treated `prefix` and `suffix` as arrays, even though they are single running product variables in the optimized version.

## Recognition Cue
If each index needs information from the left side and the right side, think prefix/suffix.

## Fix / Rule
Use the running product before multiplying by the current value. This keeps `nums[i]` excluded from its own answer.

## Interview Explanation
I avoid division by using prefix and suffix products. I first store the product of all elements before each index in the answer array. Then I scan from right to left while keeping a suffix product and multiply it into each answer position. This gives the product of all elements except the current one in O(n) time.

## Variation
If division were allowed and there were no zeros, we could multiply all numbers and divide by each value. But this problem forbids division and zeros make division unsafe.