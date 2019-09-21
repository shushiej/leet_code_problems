###  107. Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree `[3,9,20,null,null,15,7]`,

```
         3
       /   \
      9     20
           /   \
         15     7
```

should return:

```
[
    [15, 7],
    [9, 20],
    [3]
]
```


### Solution
This is a BFS problem, as we traverse layer by layer appending the nodes to an array. 