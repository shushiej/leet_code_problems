### 171. Excel Sheet Column Number

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:
```
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
```

**Example 1:**
```
Input: "A"
Output: 1
```

**Example 2:**
```
Input: "AB"
Output: 28
```

**Example 3:**
```
Input: "ZY"
Output: 701
```

### Solution
This was similar to the other excel question, but we are now converting the letter back to base 10. This is done by multiplying a count value by 26. We use the `ordinal` method to return the difference between the current character and `'A'`. 