i = int(input())
l1 = list(map(int, input().split()))
s = 1
for j in range(i):
    s = (s*l1[j]) % (10**9+7)
print(s)
