### 206. Reverse Linked Lise

Reverse a singly linked list.

**Example:**
```
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
```

**Follow up:**
A linked list can be reversed either iteratively or recursively. Could you implement both ?

### Solution
Using the iterative approach we keep a track of the prev node and iteratively reverse the direction of the linked list. 

**example**
```
1->2->3->NULL

prev = None
cur = head
        
while(cur != None):
    nextTemp = cur.next
    cur.next = prev
    prev = cur
    cur = nextTemp

return prev
             prev  cur     nextTemp
initially:    x      1   --->  2   --->  3 --->  NULL

                   prev     cur      nextTemp 
iteration_1 : x <--- 1        2   --->   3 --->  NULL

                              prev      cur       nextTemp
iteration_2:  x <--- 1  <---   2         3 --->  NULL

                                        prev   cur, nextTemp
iteration_3:  x <--- 1  <---   2   <---   3    NULL
```

Notice how prev takes the head of the list at the very end and cur and NextTemp both become null.