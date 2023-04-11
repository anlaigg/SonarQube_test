def maxSatisfiedCustomer(cooks):
    tasks = sorted(cooks, key=lambda x: x[1]) # 按照截止时间进行排序
    n = len(tasks)
    tmax = max([task[1] for task in tasks])
    dp = [[0 for _ in range(tmax+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, tmax+1):
            cookTime, deadline = tasks[i-1]
            if j >= cookTime and j <= deadline:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-cookTime]+1)
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][tmax]

inputstr = input().strip()
cooks = eval(inputstr)
print(maxSatisfiedCustomer(cooks))
