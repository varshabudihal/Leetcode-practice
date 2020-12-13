Problem:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Eg:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Solution:
#This solution is based on hash by sorted string 
class Solution:
  def groupAnagrams(self, strs):
  anagrams = collections.defaultdict(list)
  for s in strs:
    anagrams[''.join(sorted(s))].append(s)
  return anagrams.values()
  
#Solution 2: this is based on hash by alphabetical order
class Solution:
def groupAnagrams(self, strs):
  anagrams = collections.defaultdict(list)
  for s in strs:
    hashkey = [0]*26
    for c in s: hashkey [ord(c)-97] +=1
      anagrams[''.join(sorted(s))].append(s)
   return anagrams.values()
