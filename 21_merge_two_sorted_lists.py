# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        # faster way
        head = ListNode()
        current = head
        
        while (list1 and list2):
            if (list1.val < list2.val):
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next # move on to next element
        
        current.next = list1 if list1 else list2
        return head.next
    
    def mergeTwoLists(self, list1, list2):
        # my original way, still fast
        head, current = None, None
        vals = []

        while (list1 is not None or list2 is not None):
            if list1 is not None and list2 is not None:
                vals.extend([min(list1.val, list2.val), max(list1.val, list2.val)])
                list1, list2 = list1.next, list2.next

            elif list1 is not None:
                vals.append(list1.val)
                list1 = list1.next
            else:
                vals.append(list2.val)
                list2 = list2.next
        
        for val in sorted(vals):
            if head is None:
                head = ListNode(val)
                current = head
            else:
                current.next = ListNode(val)
                current = current.next
        
        return head

print(min([50, 100, 200], [30, 20, 50]))
