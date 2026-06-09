def fibonacci(x):
    if x in [0,1]:
        return x
    return fibonacci(x-1)+fibonacci(x-2)

def print_fibonacci(stop_at):
    n=1
    result=0
    while result <= stop_at:
        print(result,end=", ")
        result = fibonacci(n)
        n+=1

print_fibonacci(50)