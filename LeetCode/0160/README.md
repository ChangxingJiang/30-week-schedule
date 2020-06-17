# LeetCode题解：0160（相交链表）

[题目链接](https://leetcode-cn.com/problems/intersection-of-two-linked-lists/)（简单）

| 解法           | 执行用时        |
| :------------- | --------------- |
| Ans 1 (Python) | 216ms (>25.96%) |
| Ans 2 (Python) | 184ms (>75.53%) |

解法一（使用Python的list直接实现）：

```python
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    hashmap = set()
    while headA:
        hashmap.add(headA)
        headA = headA.next
    while headB:
        if headB in hashmap:
            return headB
        headB = headB.next
```

解法二（双指针；因为双指针经过长度相同，因此一定会同时到达终点）：

```python
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    if headA and headB:
        nodeA = headA
        nodeB = headB
        while nodeA != nodeB:
            nodeA = nodeA.next if nodeA else headB
            nodeB = nodeB.next if nodeB else headA
        return nodeA
```



