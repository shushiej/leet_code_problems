### 167. Two Sum II - Input Array is sorted

Given an array of integers that is already **sorted in ascending order**, find two numbers such that they add up to a specific target number.
The function `twoSum` should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

**Note:**

* Your returned answers (both index1 and index2) are not zero-based.
* You may assume that each input would have exactly one solution and you may not use the same element twice.

**Example:**
```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
```

### Solution
There are a few ways to solve this, one would be to create a map and keep track of the sum of the integers and return the map. 
Or you could use a while loop to iterate over the list from both ends. You keep adding the numbers from the list until the left pointer equals the right pointer. 