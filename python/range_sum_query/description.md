### 303. Range Sum Query - Immutable

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

**Example:**
```
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
```

**Note:**
1. You may assume that the array does not change.
2. There are many calls to sumRange function.

### Solution
The brute force solution for this will work but it was be very slow to run around 1016ms, this is because everytime we call the `sumRange` function a lot of the grunt work is done here, such as slicing the list and then summing the list. With a large array this requires a lot of work.
The more efficient solution would be to do the summing in the `__init__` function where you can create a new array containing the sums of the list elements. This is only done once when the `NumArray` instance is initialized, which leave the `sumRange` to just get the correct sum from the list. We can reduce the time from 1016ms to 64ms this way. 