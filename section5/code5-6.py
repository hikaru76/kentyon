inf = float('INF')
n = int(input())
h = list(map(int,input().split()))
dp = [inf] * n

def rec(i):
    if dp[i] < inf:
        return dp[i]
    if i == 0:
        return 0
    res = inf
    res = min(res, rec(i-1) + abs(h[i] - h[i-1]))
    if i > 1:
        res = min(res, rec(i-2) + abs(h[i] - h[i-2]))
    dp[i] = res
    return res

print(rec(n-1))