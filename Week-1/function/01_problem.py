def greatest():
    a = int(input("Enter 1st number:"))
    b = int(input("Enter 2st number:"))
    c = int(input("Enter 3st number:"))
    if(a>b and a>c):
        print(f"The greatest number is {a}")
    elif(b>a and b>c):
        print(f"The greatest number is {b}")
    else:
         print(f"The greatest number is {c}")

greatest()