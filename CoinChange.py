class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] * (amount + 1)
        tmp = [0] * len(coins)
        for i in range(1, amount + 1):
            for j in range(len(tmp)):
                newAmount = i - coins[j]
                tmp[j] = dp[newAmount] if newAmount >= 0 else -1
            y = [x for x in tmp if x >= 0]
            dp[i] = min(y) + 1 if y else -1
        return dp[-1]
if __name__ == "__main__":
    s = Solution();
    coins = [1,2,5]
    amount = 11
    print(s.coinChange(coins, amount))
