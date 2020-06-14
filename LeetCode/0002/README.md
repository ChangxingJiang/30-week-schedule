# LeetCode题解：0002（两数相加）

[题目链接](https://leetcode-cn.com/problems/add-two-numbers/)（中等）

| 解法           | 执行用时       | 内存消耗        |
| -------------- | -------------- | --------------- |
| Ans 1 (Python) | 76ms (>60.58%) | 13.8MB (>5.13%) |
| Ans 2 (Python) | 68ms (>88.91%) | 13.8MB (>5.13%) |

首先，我们先了解一下ListNode的结构：```["ListNode{val: 2, next: ListNode{val: 4, next: ListNode{val: 3, next: None}}}"]```

参考[“娃哈哈店长”的题解](https://leetcode-cn.com/problems/add-two-numbers/solution/python3ti-jie-fang-leetcodeguan-fang-lei-listnoded/)，我们得到如下ListNode类的代码：

```python
class ListNode():
    def __init__(self, val):
        if isinstance(val,int):
            self.val = val
            self.next = None
            
        elif isinstance(val,list):
            self.val = val[0]
            self.next = None
            cur = self
            for i in val[1:]:
                cur.next = ListNode(i)
                cur = cur.next
    
    def gatherAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
            return self.__class__.__name__+" {"+"{}".format(self.gatherAttrs())+"}"
```

解法一（按位依次相加）：

```python
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    ans = ListNode(0)  # 返回结果
    carry = 0  # 进位计数
    node = ans  # 当前位
    while True:
        value = carry
        if l1:
            value += l1.val
            l1 = l1.next
        if l2:
            value += l2.val
            l2 = l2.next
        node.val = value % 10
        carry = value // 10
        if l1 or l2 or carry == 1:
            node.next = ListNode(0)
            node = node.next
        else:
            break
    return ans
```

解法二（优化代码结构）：

```python
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    ans = node = ListNode(None)  # 返回结果 当前节点
    now = 0  # 进位计数
    while l1 or l2 or now:
        now += (l1.val if l1 else 0) + (l2.val if l2 else 0)
        node.next = ListNode(now % 10)
        node = node.next
        now //= 10
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return ans.next
```

[Github](https://github.com/ChangxingJiang/LeetCode_Solution/tree/master/0002)

