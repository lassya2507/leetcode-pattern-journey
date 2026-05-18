# Valid Anagram

## Pattern
Frequency Map

## Constraints Thinking
If the strings have different lengths, they cannot be anagrams. If the input only has lowercase English letters, the number of possible characters is fixed.

## Intuition
Two strings are anagrams if they contain the same characters with the same frequencies.

## Brute Force
Sort both strings and compare them.

## Brute Force Complexity
Time: O(n log n)  
Space: O(n), depending on sorting implementation

## Optimized Approach
Use two dictionaries to count character frequencies in both strings. If the dictionaries are equal, the strings are anagrams.

## Optimized Complexity
Time: O(n)  
Space: O(k), where k is the number of unique characters. If only lowercase English letters are allowed, space is O(1).

## Mistake I Made
I forgot that a new character must be initialized with count 1 before it can be incremented.

## Recognition Cue
If the problem asks whether two strings have the same characters or same frequencies, think frequency map.

## Fix / Rule
For frequency counting, either use if/else initialization or `map[ch] = map.get(ch, 0) + 1`.

## Interview Explanation
I first check if the string lengths are different. If they are, they cannot be anagrams. Then I build frequency maps for both strings and compare them. If both maps are equal, every character appears the same number of times in both strings.

## Variation
Group Anagrams uses the same idea, but instead of comparing two strings, we group many strings by their character frequency signature.