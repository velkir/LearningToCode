from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Другого варианта, кроме как проходится по каждой Ноде и фиксировать их последовательность (добавляя в список) я не вижу.
        Общий случай - это добавление n-1 элементу ссылку на n+1 элемент.
        Дополнительные случаи - наличие только одной ноды, первая/последняя нода на удаление
        """
        node_list = []
        node = head
        while node is not None:
            node_list.append(node)
            node = node.next
        if len(node_list) == 1:
            return
        elif n == 1:
            node_list[-2].next = None
        elif n == len(node_list):
            return head.next
        else:
            node_list[-n - 1].next = node_list[-n + 1]
        return head

# node5 = ListNode(5, None)
# node4 = ListNode(4, node5)
# node3 = ListNode(3, node4)
# node2 = ListNode(2, node3)
# node1 = ListNode(1, node2)

node2 = ListNode(2, None)
node1 = ListNode(1, node2)

solution = Solution()
result = solution.removeNthFromEnd(node1, 2)
print(result.__dict__)