class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        
        rows = len(triangle)
        
        for i in range(1,rows):
            for j in range(len(triangle[i])):
                if j == 0:
                    triangle[i][j]+=triangle[i-1][j]
                elif j == len(triangle[i])-1:
                    triangle[i][j]+=triangle[i-1][len(triangle[i-1])-1]
                else:
                    triangle[i][j] = triangle[i][j]+min(triangle[i-1][j-1], triangle[i-1][j])
                
        return min(triangle[rows-1])
                
Time: O(n)
Space: O(1)
