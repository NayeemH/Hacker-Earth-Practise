t = int(input())
count = 0
for k in range(t):
    str_a = input()
    str_b = input()
    for i in str_a:
        for j in str_b:
            if(i == j):
                count = count+1
                str_a.replace(i, '')
                str_b.replace(j, '')
                break
print((len(str_a)+len(str_b)-count)-count)
