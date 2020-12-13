Problem:

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Solution:

class Solution:
  def addTwoNumbers(self, L1: ListNode, L2: ListNode):
    carry = 0 
    res = n =ListNode(0)
    
    while l1 or l2 or carry:
      if l1:
        carry += l1.val
        l1 = l1.next
        
      if l2:
        carry +=l2.val
        l2 = l2.next
        
      carry, val = divmod(carry, 10)
      n.next = n = ListNode(val)
      
    return res.next
