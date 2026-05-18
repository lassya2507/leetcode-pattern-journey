# Best Time to Buy and Sell Stock

## Pattern
Greedy / Running Minimum

## Constraints Thinking
A brute force solution checks every buy and sell pair, which takes O(n²) time. If the input size is large, this will be too slow. We need a one-pass solution.

## Intuition
For each day, if I sell today, the best buy day is the cheapest price seen before or on today.

## Brute Force
Try every buy day `i` and every sell day `j` after it. Calculate `prices[j] - prices[i]` and keep the maximum profit.

## Brute Force Complexity
Time: O(n²)  
Space: O(1)

## Optimized Approach
Scan the prices once while tracking:
- `min_price`, the lowest price seen so far
- `max_profit`, the best profit seen so far

For each price:
1. Update `min_price` if the current price is lower
2. Calculate `profit = price - min_price`
3. Update `max_profit`

## Optimized Complexity
Time: O(n)  
Space: O(1)

## Mistake I Made
I confused loop value with index. In `for price in prices`, `price` is already the actual value, so I should not use `prices[price]`.

I also calculated profit each iteration but forgot to update `max_profit` inside the loop, which made the code return the final day's profit instead of the best profit.

## Recognition Cue
If the problem asks for max profit from one buy before one sell, think running minimum.

## Fix / Rule
When scanning prices, keep the cheapest price so far and update the best profit at every step.

## Interview Explanation
I use one pass through the prices. At each price, I treat it as a possible sell price. To maximize profit, I need the cheapest buy price seen so far. I update the minimum price first, calculate the current profit, and update the maximum profit. This gives O(n) time and O(1) space.

## Variation
If multiple transactions are allowed, the strategy changes. Instead of one global best profit, we add every positive price difference between consecutive days.