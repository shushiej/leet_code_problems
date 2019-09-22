## Test if a Binary Tree is Balanced.

If a BST is balanced, then at every node the **absolute difference** between the left subtree and the right subtree cannot be more than 1.

```
|left_subtree - right_subtree| <= 1
```

### Approach
One approach for this problem would be to drill down to each node and check if the left and right subtree are balanced.
Each node should return it's height back up to it's parent node until it gets to the root. At each parent node we `max(left_subtree, right_subtree) + 1` and bubble up to the parent until we get the total height of each subtree.

## Big O
Time: O(n) - we visit all nodes to get the height.
Space: O(h) - we traverse the height of the whole tree.

### Acknowledgements
Check out this wonderful video by `Back to Back SWE` on the [Balanced Binary Tree](https://www.youtube.com/watch?v=LU4fGD-fgJQ), with code samples. 