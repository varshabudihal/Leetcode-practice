Problem:
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.
Formally the function should:
Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Solution:

class Solution:
  def increasingTriplet(self, nums):
    first = second= float('inf')
    for n in nums:
      if n<=first:
        first = n
      elif n<=second:
        second=n 
      else:
        return True
        
    return False
