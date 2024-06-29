def coinChange(coins,amount):
    dp=[0]*(amount+1)
    dp[0]=0
    for i in coins:
        for j in range(i,amount+1):
            dp[j]=1+dp[j-i]
            print(dp)
    print("final",dp)
    return dp[amount]
coins=[1,2,5]
amount=7
print(coinChange(coins,amount))