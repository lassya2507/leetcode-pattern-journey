# Valid Palindrome

## Pattern
Two Pointers

## Constraints Thinking
The string can contain letters, numbers, spaces, and punctuation. We only compare alphanumeric characters and ignore case.

## Intuition
A palindrome reads the same forward and backward, so we compare characters from both ends and move inward.

## Brute Force
Build a cleaned lowercase string with only alphanumeric characters, then compare it with its reverse.

## Brute Force Complexity
Time: O(n)  
Space: O(n)

## Optimized Approach
Use two pointers:
- `left` starts at the beginning
- `right` starts at the end

While `left < right`:
1. Move `left` until it points to an alphanumeric character
2. Move `right` until it points to an alphanumeric character
3. Compare lowercase characters
4. If they differ, return `False`
5. Move both pointers inward

Return `True` after the full scan finishes.

## Optimized Complexity
Time: O(n)  
Space: O(1)

## Mistake I Made
I returned `True` after checking only one matching pair. I also placed the skip logic outside the main loop and forgot to move both pointers after a successful comparison, which caused Time Limit Exceeded.

## Recognition Cue
If the problem asks to compare characters from both ends or check palindrome behavior, think two pointers.

## Fix / Rule
Return `False` immediately on mismatch. Return `True` only after the whole loop finishes. Every two-pointer loop must move a pointer or return.

## Interview Explanation
I use two pointers from both ends of the string. I skip non-alphanumeric characters, compare the lowercase characters, and move both pointers inward after a match. If any pair does not match, I return `False`. If the scan finishes, the string is a valid palindrome.

## Variation
If the problem allows deleting one character, we can use the same two-pointer idea and try skipping either the left or right character on the first mismatch.