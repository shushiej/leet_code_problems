### 203. Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

**Example:**
```
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
```

### Solution
When removing elements from a linked list, you must check whether the val is the head of the list, or in the middle and end. These two cases need to be seperated out. 