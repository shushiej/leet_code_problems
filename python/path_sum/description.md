### 112. Path Sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

**Note:** A leaf is a node with no children.

**Example:**

Given the below binary tree and `sum = 22`,
```
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
```
return `true`, as there exist a root-to-leaf path `5->4->11->2` which sum is `22`.

### Solution

With sum problems, there is always a remainder value that you need to calculate. If the `sum - remainder = 0` then you know you found your sum.
Since this is a tree problem, you can use recursion to visit each node in the tree, and ask the question does the `sum - remainder = 0` if it does then return True.