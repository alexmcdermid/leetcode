# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create new list node of -1 and set to prev pointer
        listR = ListNode(-1)
        prev = listR
        
        #if list1 and list2 not None
        while list1 and list2:
            #if the current val of list 1 is less or equal to list 2 prev pointer next item is list1 val
            #set the list1 val as the next val in the linked list
            if list1.val<=list2.val:
                prev.next=list1
                list1=list1.next
            #we do the same thing as above but in the case where the current val of list 2 is less than list 1
            else:
                prev.next=list2
                list2=list2.next
            #set the prev pointer after every iteration of the loop so we know what to connect the next result to
            prev = prev.next
            
        #when we run out of one list, the other list is not always empty, so we connect it as everything else will be in order and larger
        prev.next = list1 if list1 is not None else list2
        
        return listR.next