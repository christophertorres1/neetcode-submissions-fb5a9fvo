# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge2Lists(self, list1: ListNode, list2: ListNode) -> ListNode:
        temp_node = curr_node = ListNode()

        while list2:
            if not list1:
                curr_node.next = list2
                return temp_node.next
            else:
                if list1.val <= list2.val:
                    curr_node.next = list1
                    list1 = list1.next
                else:
                    curr_node.next = list2
                    list2 = list2.next
                curr_node = curr_node.next
        curr_node.next = list1

        return temp_node.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        else:
            m = len(lists) // 2
            return self.merge2Lists(
                self.mergeKLists(lists[:m]), 
                self.mergeKLists(lists[m:]))
