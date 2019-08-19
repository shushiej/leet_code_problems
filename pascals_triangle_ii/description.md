### 119. Pascals' Triangle II

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.

![gif](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

**Example:**
```
Input: 3
Output: [1,3,3,1]
```

**Follow up:**
Could you optimize your algorithm to use only O(k) extra space?


#### Solution
This solution is similar to the way I solved the previous pascals triangle problem, and it uses O(K) space, because it traverses the array once to get the values needed. 