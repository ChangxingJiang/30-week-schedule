# LeetCode题解：0021（合并两个有序链表）

[题目链接](https://leetcode-cn.com/problems/merge-two-sorted-lists/)（简单）

| 解法           | 执行用时       | 内存消耗        |
| -------------- | -------------- | --------------- |
| Ans 1 (Python) | 36ms (>97.41%) | 13.6MB (>7.14%) |
| Ans 2 (Python) | 48ms (>54.92%) | 13.7MB (>7.14%) |
| Ans 3 (Python) | 40ms (>90.66%) | 13.7MB (>7.14%) |
| Ans 4 (Python) | 54ms (>31.14%) | 13.7MB (>7.14%) |

解法一（遍历两个链表并比较排序）：

```python
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    ans = node = ListNode(0)

    while l1 or l2:
        if l1 and (l2 is None or l1.val <= l2.val):
            node.next = ListNode(l1.val)
            l1 = l1.next
        else:
            node.next = ListNode(l2.val)
            l2 = l2.next
        node = node.next

    return ans.next
```

解法二（在解法一中，增加当链表为空时的处理）：

```python
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    ans = node = ListNode(0)

    while l1 or l2:
        if not l1:
            node.next = l2
            break
        if not l2:
            node.next = l1
            break

        if l1.val <= l2.val:
            node.next = ListNode(l1.val)
            l1 = l1.next
        else:
            node.next = ListNode(l2.val)
            l2 = l2.next
        
        node = node.next

    return ans.next
```

解法三（在解法二中，直接转移节点）：

```python
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    ans = node = ListNode(0)

    while l1 or l2:
        if not l1:
            node.next = l2
            break
        if not l2:
            node.next = l1
            break

        if l1.val <= l2.val:
            node.next = l1
            l1 = l1.next
        else:
            node.next = l2
            l2 = l2.next

        node = node.next

    return ans.next
```

解法四（将解法三中，修改循环逻辑）：

```python
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    ans = node = ListNode(0)

    while l1 and l2:

        if l1.val <= l2.val:
            node.next = l1
            l1 = l1.next
        else:
            node.next = l2
            l2 = l2.next

        node = node.next

    if l1 or l2:
        node.next = l1 or l2

    return ans.next
```