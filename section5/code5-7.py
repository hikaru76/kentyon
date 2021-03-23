def solve(i):
    if dp[i] != -1:
        return dp[i]
    tmp = 0
    for j in range(i-1):
        if weight - dp[j] + w[i]

n,weight = int(input())
w = []
v = []
for i in range(n):
    a,b = map(int,input().split())
    w.append(a)
    v.append(b)
dp = [-1] * n
