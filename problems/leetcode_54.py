class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        dir = {1: "right", 2: "down", 3: "left", 4: "up"}
        flag = dir[1]
        res = []
        m, n = len(matrix), len(matrix[0])
        i, j = 0, 0
        biao = [[0 for _ in range(n)] for _ in range(m)]
        while len(res) < m * n:
            res.append(matrix[i][j])
            biao[i][j] = 1
            if flag == "right":
                if j + 1 == n or biao[i][j + 1] == 1:
                    flag = dir[2]
                    i += 1
                else:
                    j += 1
            elif flag == "down":
                if i + 1 == m or biao[i + 1][j] == 1:
                    flag = dir[3]
                    j -= 1
                else:
                    i += 1
            elif flag == "left":
                if j - 1 == -1 or biao[i][j - 1] == 1:
                    flag = dir[4]
                    i -= 1
                else:
                    j -= 1
            elif flag == "up":
                if i - 1 == -1 or biao[i - 1][j] == 1:
                    flag = dir[1]
                    j += 1
                else:
                    i -= 1
        return res

# 测试代码
def test_spiral_order():
    solution = Solution()
    
    
    # 测试1x1矩阵
    print("Test 1x1 matrix:", solution.spiralOrder([[1]]))  # 应该返回[1]
    
    # 测试2x2矩阵
    print("Test 2x2 matrix:", solution.spiralOrder([[1, 2], [3, 4]]))  # 应该返回[1, 2, 3, 4]
    
    # 测试3x3矩阵
    print("Test 3x3 matrix:", solution.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # 应该返回[1, 2, 3, 6, 9, 8, 7, 4, 5]
    
    # 测试非方形矩阵
    print("Test non-square matrix:", solution.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))

test_spiral_order()