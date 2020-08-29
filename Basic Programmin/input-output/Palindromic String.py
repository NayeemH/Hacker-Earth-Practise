s = input()


def str_Reverse(x):
    return x[::-1]


s_s = str_Reverse(s)
if(s == s_s):
    print("YES")
else:
    print("NO")
