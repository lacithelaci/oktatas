def max_arany(N, arany):
    if N == 0:
        return 0
    if N == 1:
        return arany[0]

    dp = [0] * N
    dp[0] = arany[0]
    dp[1] = max(arany[0], arany[1])

    for k in range(2, N):
        dp[k] = max(dp[k - 2] + arany[k], dp[k - 1])

    return dp[N - 1]


N = int(input())
a = input().split()
arany = [int(i) for i in a]
eredmeny = max_arany(N, arany)
print(eredmeny)
