def sum(n):
    if(n==1):
        return 1
    else:
        return n+sum(n-1)

n = int(input("Enter the no of number:"))

sum = sum(n)

print(f"The sum of first {n} natural number is {sum}")