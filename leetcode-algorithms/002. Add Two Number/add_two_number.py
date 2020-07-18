
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def nextnode(l,s):
            s = str(l.val) + s
            if l.next:
                nextnode(l,s)
            return s
        s1 = nextnode(l1,'')
        s2 = nextnode(l2,'')
        sums = str(int(s1)+int(s2))
        sums = sums[::-1]
        return [int(x) for x in sums]