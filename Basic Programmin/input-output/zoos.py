s = input()
if(len(s) <= 20):
    x = s.count("z")
    y = s.count("o")
    if(x*2 == y):
        print("Yes")
    else:
        print("No")
