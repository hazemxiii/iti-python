a = input("String A: ")
b = input("String B: ")

def divide_string(s,isFront):
    length = len(s)
    if length%2==0:
        if isFront:
            return s[0:int(length/2)]
        else:
            return s[int(length/2):]
    else:
        if isFront:
            return s[0:int(length/2)+1]
        else:
            return s[int(length/2)+1:]


print(divide_string(a,True)+divide_string(b,True),divide_string(a,False)+divide_string(b,False))