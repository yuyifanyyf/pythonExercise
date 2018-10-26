# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def printNode(self, node):
        while node:
            print(node.val, end="")
            node = node.next
        print()
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        index, odd, last, first = 2, head, head, head.next
        while first:
            if index % 2 == 0:
                first = first.next
                last = last.next
            else:
                odd.next = first
                last.next = first.next
                first.next = last
                first = last.next
                odd = odd.next

                # tmp = first
                # first = first.next
                # last.next = tmp.next
                # tmp.next = odd.next
                # odd.next = tmp
                # odd = odd.next
            self.printNode(head)
            index += 1
        return head
if __name__ == "__main__":
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    s.oddEvenList(head)
