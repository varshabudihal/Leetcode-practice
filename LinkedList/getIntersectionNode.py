Problem:
Write a program to find the node at which the intersection of two singly linked lists begins.
For example, the following two linked lists:

Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2

Solution:

class Solution:
  def getIntersectionNode(self, headA, headB):
    if headA is None and headB is None:
    return None
    
    pa, pb, headA, headB
    
    while pa is not pb:
      if pa:
        pa = pa.next
      else:
        pa = headB
      if pb:
        pb = pb.next
      else:
        pb = headA
        
    return pa
      
