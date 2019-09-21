### 118. Pascal's Triangle

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

![gif](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

Example:
```
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
```

### Solution

After doing some googling, I found the formula for calculating each row of the triangle without having to look at the row above.

```
n! / k!(n - k)!
```
However the submission for this result was quite slow, compared to the standard approach. I just hate array indexing it gets too confusing so I tried to avoid it. 