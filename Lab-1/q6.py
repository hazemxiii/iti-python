for i in range(1,10):
    if i > 5:
        for j in range(0,10-i):
            print("*",end="")
    else:
        for j in range(0,i):
            print("*",end="")
        
    print()