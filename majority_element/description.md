### 169. Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears **more than** `⌊ n/2 ⌋` times.

You may assume that the array is non-empty and the majority element always exist in the array.

**Example 1:**
```
Input: [3,2,3]
Output: 3
```

**Example 2:**
```
Input: [2,2,1,1,1,2,2]
Output: 2
```

### Solution
I kept a hashmap which kept a record of the number and the count, and I returned it once the count was `>= len(nums) / 2`. This took around `156ms`
I also kept a record of the other solutions compared to mine. The fastest was a simple two liner which sorts the array at get the index at `len(nums) /2`.