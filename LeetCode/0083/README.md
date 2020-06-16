# LeetCode题解：0083（删除排序链表中的重复元素）

[题目链接](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/)（简单）

| 解法           | 执行用时       |
| :------------- | -------------- |
| Ans 1 (Python) | 44ms (>92.02%) |
| Ans 2 (Python) | 44ms (>92.02%) |

解法一（生成新的无重复链表）：

```python
def deleteDuplicates(self, head: ListNode) -> ListNode:
    ans = node = ListNode(0)
    while head:
        if head.next:
            if head.val != head.next.val:
                node.next = ListNode(head.val)
                node = node.next
        else:
            node.next = ListNode(head.val)
            node = node.next
        head = head.next
    return ans.next
```

解法二（在原链表中转移节点）：

```python
def deleteDuplicates(self, head: ListNode) -> ListNode:
    node = head
    while node and node.next:
        if node.val == node.next.val:
            node.next = node.next.next
        else:
            node = node.next
    return head
```