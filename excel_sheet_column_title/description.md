### 168. Excel Sheet Column Title

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

```
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
```
**Example 1:**
```
Input: 1
Output: "A"
```

**Example 2:**
```
Input: 28
Output: "AB"
```

**Example 3:**
```
Input: 701
Output: "ZY"
```

### Solution
Initially I had no idea how to solve this question. I read about the [ascii table](http://www.asciitable.com/) and noticed python has a `chr` function which converts numbers to ASCII notation. So I can build up a string converting `n` into a character. This is more of a base problem. The purpose is to convert from base 10 (`n`) to base 26 (the alphabet). So every 26 characters you add on a new letter. 