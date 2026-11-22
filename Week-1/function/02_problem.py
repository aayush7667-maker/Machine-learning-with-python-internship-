def convert(n):
    fahre = (n * (9/5)+32) 
    return fahre



n = int(input("Enter the temp in degree celcius to  convert it into fahrenheit:"))
fahrenheit = convert(n)

print(f"{n} degree celcius in fehrenheit is {fahrenheit}")
