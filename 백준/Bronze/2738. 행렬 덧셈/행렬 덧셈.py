N, M =map(int, input().split())
A, B=[], []
for _ in range(N):
    row=list(map(int, input().split()))
    A.append(row)
for _ in range(N):
    row=list(map(int, input().split()))
    B.append(row)

for i in range(N):
    for j in range(M):
        print(A[i][j]+B[i][j], end=' ')
    print()
