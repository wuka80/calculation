# 题2：200级台阶，每次可以爬1级、2级、或3级台阶，爬到顶端有多少种爬法

def climbStairs(n):
    if (n == 1): return 1
    if (n == 2): return 2
    if (n == 3): return 4

    oneStep = 4
    twoStep = 2
    threeStep = 1
    allWays = 0

    for i in range(3, n):
        allWays = oneStep + twoStep + threeStep
        threeStep = twoStep
        twoStep = oneStep
        oneStep = allWays

    # count = climbStairs(n - 1) + climbStairs(n - 2) + climbStairs(n - 3)
    # print(n.__str__() + ',' + count.__str__())
    return allWays


n = int(input('请输入台阶总数：'))
count = climbStairs(n)
print("爬到山顶方法总数：" + count.__str__())
