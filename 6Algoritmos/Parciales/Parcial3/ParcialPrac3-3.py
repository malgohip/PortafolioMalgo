def mejoresVueltas(denominaciones, cantidades):
	maximas=max([a for a in cantidades if a>=0], default=0)
	INF=10**18
	dp=[INF]*(maximas + 1)
	dp[0]=0
	denominaciones=sorted(set(denominaciones))
	for a in range(1, maximas+1):
		best=INF
		for d in denominaciones:
			if d>a:
				break
			cand=dp[a-d]+1
			if cand<best:
				best=cand
		dp[a]=best
	resultados=[]
	for a in cantidades:
		if a<0:
			resultados.append(None)
		elif a==0:
			resultados.append(0)
		else:
			resultados.append(dp[a])
	return resultados


denominaciones = list(map(int, input().strip().split()))
cantidades = list(map(int, input().strip().split()))
resultados = mejoresVueltas(denominaciones, cantidades)
print(" ".join(f"{r}" for r in resultados))
