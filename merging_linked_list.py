# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)    #create a dummy empty node
        curr = dummy      

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1                  #first node will be lesser element among the two linked list
                list1 = list1.next                 #increment the linked list element to the next element in the list
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 or list2       #add remaining element in the linked list which is not empty


        return dummy.next                   #return one element after the dummy node


         