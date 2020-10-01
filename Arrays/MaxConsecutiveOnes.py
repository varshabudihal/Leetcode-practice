
#Given a binary array, find the maximum number of consecutive 1s in this array.

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        sum = 0
        m = 0
        for i in nums:
            sum = sum + i
            if i != 1 :
                if m < sum: 
                    m = sum
                sum = 0
                
        return max(sum, m)
