### 155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

* push(x) -- Push element x onto stack.
* pop() -- Removes the element on top of the stack.
* top() -- Get the top element.
* getMin() -- Retrieve the minimum element in the stack.

**Example:**

```
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
```

### Solution
I had two solutions to this problem. One was super slow taking a total of `1368ms` to run this was because I had only one stack which was doing the everything. Performing operations like `getMin()` made it way too slow, because it is done in `O(N)` time. The other solution (the one posted here) had two stacks. One stack is considered the main stack pushing and popping from the list, while the other only get track of the minimum value, so the  `getMin()` function can be done in constant time.