'''
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

进阶：

如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

示例：

输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 8 -> 0 -> 7
'''
from typing import List

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def transint(l):
            cur = l
            r = [str(cur.val)]
            while cur.next is not None:
                r.append(str(cur.next.val))
                cur = cur.next
            return int(''.join(r))
        result = transint(l1)+transint(l2)
        result = list(str(result))
        head = ListNode(int(result[0]))
        cur = head
        for i in range(1, len(result)):
            cur.next = ListNode(int(result[i]))
            cur = cur.next
        return head

s=Solution()
