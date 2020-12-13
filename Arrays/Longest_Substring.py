Problem:
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Solution:

class Solution:
  def lengthOfLongestSubstring(self,s:str):
    left, ans = 0,0 
    for right in range(len(s)):
      while s[right] in s[left:right]:
        left = left+1
      else:
      ans = max(ans, right-left+1)
    return ans
