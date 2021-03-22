n,w = map(int,input().split())
a = list(map(int,input().split()))
for i in range(2**n):
	cnt = 0	
	for j in range(n):
		if (i>>j) & 1:
			cnt += a[j]
	if cnt == w:
		print('Yes')
		exit()
print('No')