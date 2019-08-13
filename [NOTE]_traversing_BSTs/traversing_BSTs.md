## Three methods to traverse a Binary Search Tree

Given the Graph:
```
                  F
                /   \
              B      G
            /   \      \
          A      D      I
               /   \    /
             C      E  H
```

### Preorder
Preorder traversals follow this order `root > left > right`. So it starts at the root follows the root node first before traversing the whole left node, and then the whole right node.
The result of traversal for the preorder would be: `[F, B, A, D, C, E, G, I, H]`

### Inorder
Inorder traversals follow this order `left > root > right`. So it starts at the root follows the left node first before traversing the root node, and finally the right node.
The result of traversal for the Inorder would be: `[A, B, C, D, E, F, G, H, I]`

### Postorder
Inorder traversals follow this order `left > right > root`. So it starts at the root follows the left node first before traversing the whole right node.
The result of traversal for the Inorder would be: `[A, B, C, D, E, G, H, I, F]`