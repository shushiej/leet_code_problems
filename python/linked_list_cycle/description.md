## 141. Linked List Cycle

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer `pos` which represents the position (0-indexed) in the linked list where tail connects to. If `pos` is -1, then there is no cycle in the linked list.

**Example 1:**
```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.
```
![loop_1](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

**Example 2:**
```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.
```

![loop_2](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png)

**Example 3:**
```
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```
![loop_3](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png)


### Solution

This is an interesting problem and solution. [This Video](https://www.youtube.com/watch?v=MFOAbpfrJ8g) explains it brilliantly. Imagine you have two cars racing around the linked list. If one car is going twice the speed as the other car, then, if the linked list has a cycle they will eventually catch up. 
You can code this in python, by having two pointers on that starts at `head.next` (fast) and the other that starts at `head` (slow). You continue incrementing the pointers and checking whether at any point the fast and the slow are equal. 