class Solution(object):
    def reverse(self, matrix, i):
        n=len(matrix[0])
        for j in range(0,n//2):
            matrix[j][i],matrix[n-j-1][i]=matrix[n-j-1][i],matrix[j][i]
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix[0])):
            self.reverse(matrix,i)  
        for x in range(len(matrix[0])):
            for y in range(x,len(matrix)):
                matrix[y][x],matrix[x][y]=matrix[x][y],matrix[y][x]

           