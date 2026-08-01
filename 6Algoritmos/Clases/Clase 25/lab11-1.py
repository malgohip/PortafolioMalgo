def contone(num):
    if not num:
        return []
    nMax = max(num)
    dp = [0] * (nMax + 1)
    for i in range(1, nMax + 1):
        dp[i] = dp[i >> 1] + (i & 1)
    res = []
    for n in num:
        res.append(dp[:n + 1])
    return res

num = list(map(int, input().split()))
res = contone(num)
print("\n".join(" ".join(map(str, fila)) for fila in res))