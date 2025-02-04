def knapsack01(values, weights, W):
    n = len(values)
    # 创建一个二维数组，初始化为0
    dp = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # 构建dp数组
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            # 如果当前物品的重量大于当前背包的承重，则不放入背包
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                # 比较不放入和放入当前物品时的最大价值，取较大者
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])

    # dp[n][W]存储了最大价值
    return dp[n][W]

# 物品的价值
values = [3, 4, 5]
# 物品的重量
weights = [2, 3, 4]
# 背包的最大承重
W = 5

# 调用函数并打印结果
max_value = knapsack01(values, weights, W)
print("最大价值为:", max_value)