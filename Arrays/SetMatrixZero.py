Problem:
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Solution:

class Solution:
  def SetZeros(self, matrix: List[List[int]]) -> None:
  
  R = len(matrix)
  C = len(matrix[0])
  rows, cols = set(), set()
  
  # Essentially, we mark the rows and columns that are to be made zero
  for i in range(R):
    for j in range(C):
      if matrix[i][j] == 0:
        rows.add(i)
        cols.add(j)
   # Iterate over the array once again and using the rows and cols sets, update the elements
   
   for i in range(R):
    for j in range(C):
      if i in rows or j in cols:
        matrix[i][j]=0
