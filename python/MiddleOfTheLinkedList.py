# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

# Example 1:

# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.


# Example 2:

# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

# Constraints:

# The number of nodes in the list is in the range [1, 100].
# 1 <= Node.val <= 100


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#first attempt
#returns part of the linked list
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = 0
        r = head
        while head:
            l+=1
            head=head.next
        
        for i in range(l):
            if l%2 == 0:
                if i<(l/2):
                    r = r.next
            else :
                if i<(l/2)-1:
                    r = r.next
                
        return r
    
#combining the two ideas above together into a single loop
#didn't realize the problem didn't care if the returned list was not linked
#slightly faster but not a linked list returned
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         #new array containing head node
#         arr = [head]
#         #while the last item in the array has a next item that is not null continue
#         while arr[-1].next:
#             #append the not null next item to the list
#             arr.append(arr[-1].next)
#         #return the middle point of the created array
#         return arr[len(arr) // 2]