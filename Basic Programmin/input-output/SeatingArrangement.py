t = int(input())
for i in range(t):
    j = int(input())
    m = j % 12
    if(j <= 108):
        # calculating window seat
        if(m == 1):
            print(j+11, "WS", end="\n")
        elif(m == 6):
            print(j+1, "WS", end="\n")
        elif(m == 7):
            print(j-1, "WS", end="\n")
        elif(m == 0):
            print(j-11, "WS", end="\n")
        # calculating middle seat
        elif(m == 2):
            print(j+9, "MS", end="\n")
        elif(m == 5):
            print(j+3, "MS", end="\n")
        elif(m == 8):
            print(j-3, "MS", end="\n")
        elif(m == 11):
            print(j-9, "MS", end="\n")
        # calculating aisle seat
        elif(m == 3):
            print(j+7, "AS", end="\n")
        elif(m == 4):
            print(j+5, "AS", end="\n")
        elif(m == 9):
            print(j-5, "AS", end="\n")
        elif(m == 10):
            print(j-7, "AS", end="\n")
