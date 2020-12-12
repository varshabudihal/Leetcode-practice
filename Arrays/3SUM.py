Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero. 
Notice that the solution set must not contain duplicate triplets.

Solution:

In order to solve this question, I first reduced it to 2SUM problem by doing a+b = -c and the duplicates are handled by - let's say there is s and e index. 
Now given nums[s] there is a unique nums[e] such that nums[s]+nums[e]=Target. Therefore, if nums[s+1] is the same as nums[s], then searching in range s+1 to e will give us a duplicate solution. 
Thus we must move s till nums[s] != nums[s-1] to avoid getting duplicates.
                        while s<e and nums[s] == nums[s-1]:
                            s = s+1

Handling Duplicates in 3SUM

Imagine we are at index i and we have invoked the 2SUM problem from index i+1 to end of the array. Now once the 2SUM terminates, we will have a list of all triplets which include nums[i]. To avoid duplicates, we must skip all nums[i] where nums[i] == nums[i-1].
            if i > 0 and nums[i] == nums[i-1]:
                continue
             
class Solution:
def threeSum (self, nums:List [int]) -> List [List[int]]:
  nums.sort()
  N, result = len(nums), []
  for i in range(N):
    if i=0 and nums[i]==nums[i-1]:
      continue
     target = nums[i]*-1
     s,e = i+1, N-1
     while s<e:
      if nums[s] +nums[e] = target:
        result.append(nums[i], nums[s], nums[e])
        s = s+1
        while s<e and nums[s] == nums[s-1]
          s = s+1
      elif nums[s] + nums[e]< target:
        s = s+1
      else:
      e = e-1
  return result
