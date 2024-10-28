# leetcode_48 旋转图像
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

 

示例 1：


输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[7,4,1],[8,5,2],[9,6,3]]
示例 2：


输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 

提示：

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000

```python
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
```
这个算法的基本思路是先将矩阵的每一行进行反转，然后将矩阵进行转置。
 **注意在对称轴进行翻转时，注意y轴的取值范围不然会反转两次**
