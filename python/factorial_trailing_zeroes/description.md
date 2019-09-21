### 172. Factorial Trailing Zeroes

Given an integer n, return the number of trailing zeroes in n!.

**Example 1:**
```
Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
```

**Example 2:**
```
Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
```

*Note: Your solution should be in logarithmic time complexity.*

### Solution
This problem title is a bit of an illusion, when we see the word factorial we immediately start thinking about creating a method to calculate the factorial.
But for this problem they only want the number of trailing zeroes in a factorial. So we don't need to calculate the factorial, we just need to calculate the number of times the number `n` can be divided by 5 without any decimals. 