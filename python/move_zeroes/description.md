### 283. Move Zeroes

Given an array `nums`, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

**Example:**
```
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
```

**Note:**
1. You must do this in-place without making a copy of the array.
2. Minimize the total number of operations.

### Solution
If you go through each element in the array that is not equal to 0, there are one of two positions it can be in, either stay where it is or move one position to the left. If you keep moving all non-zero elements to the left, they will eventually be replaced by 0's.

