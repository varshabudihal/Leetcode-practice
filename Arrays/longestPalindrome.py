Problem:
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Solution:

class Solution:
  def longestPalindrome(self, s:str):
    if not s:
      return ""
      
    for i in range(len(s), 0, -1):
      for j in range(len(s)-i-1):
        if s[j:j+i] == s[j:j+i][::-1]:
          return s[j:j+i]
