# 1)Write a Python program to get the Fibonacci series between 0 to 50

#input from user.
range = int(input("Enter the range for the Fibonacci series")) #here our given range is 0 to 50.

# first two terms of series.
a, b = 0, 1

print("Fibonacci series between 0 to 50")
while a <= range:
    print(a, end=" ")
    a, b = b, a + b
