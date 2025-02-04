class Solution:
    def zeroOnePackMethod1(self, value, W):
        size = len(value)
        dp = [0 for _ in range(W+1)]
        for i in range(size):
            for w in range(W, value[i], -1):
                dp[w] += dp[w-value[i]]
                dp[value[i]]+=1
        return dp[W]
        
def main():
    n=int(input())
    W=int(input())
    value = []
    for i in range(n):
        v=int(input())
        value.append(v)
    print(Solution().zeroOnePackMethod1(value, W))

if __name__ == '__main__':
    main()