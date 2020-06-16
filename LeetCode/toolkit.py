class ListNode:
    """
    LeetCode官方ListNode类仿写（模拟官方功能）
    主要用于本地IDE调试

    参考：https://leetcode-cn.com/problems/add-two-numbers/solution/python3ti-jie-fang-leetcodeguan-fang-lei-listnoded/
    """

    def __init__(self, val):
        """
        构造器
        :param val: 构造对象
        """
        if isinstance(val, list):
            if len(val) == 1:
                self.val = val[0]
                self.next = None
            else:
                self.val = val[0]
                self.next = ListNode(val[1:])
        elif isinstance(val, int) or isinstance(val, str):
            self.val = val
            self.next = None

    def gatherAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
        return self.__class__.__name__ + "{" + "{}".format(self.gatherAttrs()) + "}"


class TreeNode:
    """
    LeetCode官方TreeNode类仿写（模拟官方功能）
    主要用于本地IDE调试
    """

    def __init__(self, val):
        if isinstance(val, list):
            if len(val) == 0:
                self.val = None
            else:
                self.val = val[0]
        elif isinstance(val, int) or isinstance(val, str):
            self.val = val
        self.left = None
        self.right = None

    def gatherAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
        return self.__class__.__name__ + "{" + "{}".format(self.gatherAttrs()) + "}"


def build_TreeNode(val):
    if val is None:
        return None
    elif isinstance(val, list):
        if len(val) == 0:
            return None
        else:
            head = TreeNode(val[0])
            wait_node_list = [head]
            left = False
            for i in range(1, len(val)):
                node = TreeNode(val[i])
                if not left:
                    if val[i] is not None:
                        wait_node_list[0].left = node
                        wait_node_list.append(node)
                    left = True
                else:
                    if val[i] is not None:
                        wait_node_list[0].right = node
                        wait_node_list.append(node)
                    left = False
                    wait_node_list.pop(0)
            return head
    elif isinstance(val, int) or isinstance(val, str):
        return TreeNode(val)
    else:
        return None


if __name__ == "__main__":
    print(ListNode([1, 3, 5]))  # ListNode{val: 1, next: ListNode{val: 3, next: ListNode{val: 5, next: None}}}
    print(build_TreeNode([1, None, 2, 3, 4]))
