class Node(object):
    """单链表的节点"""
    def __init__(self, item):
        # item存放数据元素
        self.item = item
        # next是下一个节点的标识
        self.next = None


"""定义链表"""
class SingleLinklist(object):
    """单链表"""

    def __init__(self):
        self._head = None

# 示例，创建链表
if __name__ == "__main__":
    # 创建链表
    link_list = SingleLinklist()
    # 创建节点
    node1 = Node(1)
    node2 = Node(2)

    # 将节点添加到链表
    link_list._head = node1
    # 将第一个节点的next指针指向下一节点
    node1.next = node2
    # 访问链表
    print(link_list._head.item) # 访问第一个节点数据
    print(link_list._head.next.item) # 访问第二个节点数据