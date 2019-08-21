### 125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

**Example 1:**
```
Input: "A man, a plan, a canal: Panama"
Output: true
```

**Example 2:**

```
Input: "race a car"
Output: false
```

### Solution
My first solution was very slow, because it was doing an expensive join, while checking each string is not a punctuation. Applying regex is a much faster solution.