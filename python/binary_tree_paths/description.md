### 257. Binary Tree Paths

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

**Example:**
```
Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]
Explanation: All root-to-leaf paths are: 1->2->5, 1->3
```

### Solution
Using recursion you can traverse each path and append the string value to the array. [This Video](https://www.youtube.com/watch?v=xqS8dyexaNM) explains it really well.