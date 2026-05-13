# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
1. Merge two linked lists. 
2. Have to decide of if statements
3. Sorted? Compare the val of two linked list nodes and decide whci one is next.
4. Progress pointers
5. Fill up with teh rest of the reamining list. 
6. Watch for edge cases
"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next 
        
        node.next = list1 or list2

        return dummy.next
