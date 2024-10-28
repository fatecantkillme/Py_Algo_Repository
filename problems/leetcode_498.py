class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        if not mat or not mat[0]:  # 检查矩阵是否为空
            return []

        is_up = True  # 方向标志，向上或向下
        x, y = 0, 0  # 初始化坐标
        res = []
        m, n = len(mat), len(mat[0])  # 获取矩阵的行列数

        while len(res) < m * n:  # 当结果列表未填满时
            res.append(mat[x][y])  # 将当前元素添加到结果中

            if is_up:  # 向上移动
                if x == 0 and y < n - 1:  # 到达顶部边界
                    y += 1
                    is_up = False
                elif y == n - 1:  # 到达右侧边界
                    x += 1
                    is_up = False
                else:  # 继续向上斜着移动
                    x -= 1
                    y += 1
            else:  # 向下移动
                if y == 0 and x < m - 1:  # 到达左侧边界
                    x += 1
                    is_up = True
                elif x == m - 1:  # 到达底部边界
                    y += 1
                    is_up = True
                else:  # 继续向下斜着移动
                    x += 1
                    y -= 1

        return res
