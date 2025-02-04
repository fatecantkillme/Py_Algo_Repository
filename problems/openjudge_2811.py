def main():
    # 读取初始状态
    grid = [list(map(int, input().split())) for _ in range(5)]
    
    # 枚举第一行的所有可能操作（6位二进制）
    for i in range(64):
        first_row = [(i >> j) & 1 for j in range(6)]
        current_grid = [row.copy() for row in grid]
        steps = [first_row]
        
        # 应用第一行的操作
        toggle(current_grid, 0, first_row)
        
        # 依次处理后续行
        valid = True
        for row in range(1, 5):
            # 根据上一行的状态生成当前行的操作
            current_op = []
            for col in range(6):
                if current_grid[row-1][col] == 1:
                    current_op.append(1)
                else:
                    current_op.append(0)
            steps.append(current_op)
            toggle(current_grid, row, current_op)
        
        # 检查最后一行是否全灭
        if all(cell == 0 for cell in current_grid[4]):
            # 输出结果
            for step in steps:
                print(' '.join(map(str, step)))
            return
    
    print("NO SOLUTION")

def toggle(grid, row, operation):
    # 根据操作翻转灯的状态
    for col in range(6):
        if operation[col]:
            # 翻转当前位置
            grid[row][col] ^= 1
            # 翻转左侧
            if col > 0:
                grid[row][col-1] ^= 1
            # 翻转右侧
            if col < 5:
                grid[row][col+1] ^= 1
            # 翻转上方（仅当不是第一行时）
            if row > 0:
                grid[row-1][col] ^= 1
            # 翻转下方（仅当不是最后一行时）
            if row < 4:
                grid[row+1][col] ^= 1

if __name__ == "__main__":
    main()