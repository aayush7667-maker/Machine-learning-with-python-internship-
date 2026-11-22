def pattern(n):
    for i in range(1, n+1):
        print("*" * (4-i))

n = int(input("Enter the number:"))
pattern(n)