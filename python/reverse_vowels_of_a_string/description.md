### 345. Reverse Vowels of a String

Write a function that takes a string as input and reverse only the vowels of a string.

**Example 1:**
```
Input: "hello"
Output: "holle"
```

**Example 2:**
```
Input: "leetcode"
Output: "leotcede"
```

**Note:**
The vowels does not include the letter "y".

### Solution
Use two pointers one starting from the left and the other from right, go through each checking if it is a vowel, if both pointers are vowels, then switch them over.