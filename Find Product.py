n = int(input())
s = 1
arr = list(map(int, input().split()))
for i in range(n):
    s = (s*arr[i]) % (10**9+7)
print(s)
