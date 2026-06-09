input_string = input("String to process: ")
alpha=0
digits=0
for c in input_string:
    if c.isdigit():
        digits+=1
    elif c.isalpha():
        alpha+=1

print("Alphabet: ",alpha)
print("Digits: ",digits)