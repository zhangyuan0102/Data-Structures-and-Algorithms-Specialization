def dp(n):
    # 基础情况
    if n == 0:
        return 0
    if n < 0:
        return -1
    
    res = float('INF')
    for coin in coins:
        subproblem = dp(n - coin)
        # 子问题无解，跳过
        if subproblem == -1:
            continue
        res = min(res, 1 + subproblem)
    
    return res if res != float('INF') else -1

def coinChange(coins, amount):
    # 数组大小为 amount + 1，初始值也为 amount + 1
    dp = [amount + 1] * (amount + 1)
    # base case
    dp[0] = 0
    
    # 外层 for 循环在遍历所有状态的所有取值
    for i in range(amount + 1):
        # 内层 for 循环在求所有选择的最小值
        for coin in coins:
            # 子问题无解，跳过
            if i - coin < 0:
                continue
            dp[i] = min(dp[i], 1 + dp[i - coin])
    
    return -1 if dp[amount] == amount + 1 else dp[amount]
#1.【二维DP，三层循环】
#动态规划的基础代码如下
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n = len(coins)
        dp = [[amount+1] * (amount+1) for _ in range(n+1)]    # 初始化为一个较大的值，如 +inf 或 amount+1
        # 合法的初始化
        dp[0][0] = 0    # 其他 dp[0][j]均不合法
        
        # 完全背包：套用0-1背包【遍历硬币数目k】
        for i in range(1, n+1):                     # 第一层循环：遍历硬币
            for j in range(amount+1):               # 第二层循环：遍历背包
                for k in range(j//coins[i-1]+1):    # 第三层循环：当前硬币coin取k个 (k*coin<=amount)
                    dp[i][j] = min( dp[i][j], dp[i-1][j-k*coins[i-1]] + k )

        ans = dp[n][amount] 
        return ans if ans != amount+1 else -1
#2.【二维DP，两层循环】
#基于优化后的状态转移方程，可省去第三层循环，代码如下：
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n = len(coins)
        dp = [[amount+1] * (amount+1) for _ in range(n+1)]    # 初始化为一个较大的值，如 +inf 或 amount+1
        # 合法的初始化
        dp[0][0] = 0    # 其他 dp[0][j]均不合法
        
        # 完全背包：优化后的状态转移
        for i in range(1, n+1):             # 第一层循环：遍历硬币
            for j in range(amount+1):       # 第二层循环：遍历背包
                if j < coins[i-1]:          # 容量有限，无法选择第i种硬币
                    dp[i][j] = dp[i-1][j]
                else:                       # 可选择第i种硬币
                    dp[i][j] = min( dp[i-1][j], dp[i][j-coins[i-1]] + 1 )

        ans = dp[n][amount] 
        return ans if ans != amount+1 else -1
#3.【一维DP，两层循环】 动态规划的滚动数组优化

#在上面的状态转移方程中，每一行的 dp[i][j]dp[i][j]dp[i][j] 状态值都只与上一行（正上方）的 dp[i−1][j]dp[i-1][j]dp[i−1][j] 和 本行（左方）的dp[i][j−∗]dp[i][j-*]dp[i][j−∗] 状态值有关，因此可基于滚动数组的思想进行对状态空间 dpdpdp 进行优化而省去第一维度：
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n = len(coins)
        dp = [amount+1] * (amount+1)    # 初始化为一个较大的值，如 +inf 或 amount+1
        dp[0] = 0        # 合法的初始化
        
        # 完全背包：优化后的状态转移
        for i in range(1, n+1):             # 第一层循环：遍历硬币
            dp2 = [amount+1] * (amount+1)   # 滚动数组
            for j in range(amount+1):       # 第二层循环：遍历背包
                if j < coins[i-1]:          # 容量有限，无法选择第i种硬币
                    dp2[j] = dp[j]
                else:                       # 可选择第i种硬币
                    dp2[j] = min( dp[j], dp2[j-coins[i-1]] + 1 )
            dp = dp2

        ans = dp[amount] 
        return ans if ans != amount+1 else -1
#4.【一维DP，两层循环】 内层循环正序，省去滚动数组：
#在状态转移过程中，每一行的 dpdpdp 状态值都只与其正上方和左方的状态值有关，因此可对状态空间 dpdpdp 进一步优化而省去滚动数组 dp2dp2dp2：考虑到我我们在更新 dp[j]dp[j]dp[j] 时，使用的其实是上一行的 dp[j]dp[j]dp[j] 和 本行已更新过的 dp[j−wi]dp[j-w_i]dp[j−w i] 的值；因此在第二层循环中，通过从小到大正序计算即可保证在计算 dp[j]dp[j]dp[j] 时所用到的 dp[j]dp[j]dp[j] 来自上一行，而 dp[j−wi]dp[j-w_i]dp[j−w i] 则来自本行。
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [amount+1] * (amount+1)    # 初始化为一个较大的值，如 +inf 或 amount+1
        dp[0] = 0        # 合法的初始化；其他 dp[j]均不合法
        
        # 完全背包：优化后的状态转移
        for coin in coins:                      # 第一层循环：遍历硬币
            for j in range(coin, amount+1):     # 第二层循环：遍历背包【正序】
                dp[j] = min( dp[j], dp[j-coin] + 1 )    # 可选择当前硬币

        ans = dp[amount] 
        return ans if ans != amount+1 else -1
