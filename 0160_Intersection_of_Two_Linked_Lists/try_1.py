# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        countA = headA
        countB  = headB
        lenA = lenB = 0
        while countA:
            countA = countA.next
            lenA = lenA + 1
        while countB:
            countB = countB.next
            lenB = lenB + 1
        gap = 0
        if lenA >= lenB:
            gap = lenA - lenB
            while gap!=0:
                headA = headA.next
                gap = gap - 1
        else:
            gap = lenB - lenA
            while gap!=0:
                headB = headB.next
                gap = gap - 1
        while(1):
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next