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
        self._cycle = False
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

    def set_cycle(self, pos):
        """
        设置循环

        :param pos:
        :return:
        """
        if pos >= 0:
            self._cycle = True

            node = self
            num = 0
            pos_node = None
            last_node = None
            while node:
                if num == pos:
                    pos_node = node
                last_node = node
                node = node.next
                num += 1
            last_node.next = pos_node
        return self

    def set_next(self, next_node):
        """
        设置最后一个结点的指针

        :param node:
        :return:
        """
        node = self
        last_node = None
        while node:
            last_node = node
            node = node.next
        last_node.next = next_node

    def gatherAttrs(self):
        return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())

    def __str__(self):
        if self._cycle:
            return "Error - Found cycle in the ListNode"
        else:
            return self.__class__.__name__ + "{" + "{}".format(self.gatherAttrs()) + "}"


def build_ListNode_with_pos(val, pos=-1):
    """
    构造循环链表

    :param val: 链表
    :param pos: 链表最后一个结点指针对应的节点编号
    :return:
    """
    return ListNode(val).set_cycle(pos)


def build_ListNode_with_skip(val, list1, list2, skip1, skip2):
    """
    构造相交链表

    :param val: 相较交点
    :param list1: 链表1
    :param list2: 链表2
    :param skip1: 链表1交点位置
    :param skip2: 链表2交点位置
    :return:
    """
    list_node_1 = ListNode(list1[0:skip1])
    list_node_2 = ListNode(list2[0:skip2])
    if skip1 == len(list1):
        return list_node_1, list_node_2
    if skip2 == len(list2):
        return list_node_1, list_node_2
    list_merge = ListNode(list1[skip1:])
    list_node_1.set_next(list_merge)
    list_node_2.set_next(list_merge)
    return list_node_1, list_node_2


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
    print(ListNode([3, 2, 0, -4]).set_cycle(pos=1))
    # print(build_TreeNode([1, None, 2, 3, 4]))
