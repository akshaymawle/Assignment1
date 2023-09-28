#3) Write a Python program to count the number of even and odd numbers from a series of numbers.

# input from user,list as an input
numbers = int(input("enter a number of  elements of list"))
list=[]
for i in range (numbers):
    elements = int(input("enter elements"))
    list.append(elements)

print("input list given by user",list)
even = 0
odd = 0

# for loop
for num in list:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("number of even numbers:", even)
print("number of odd numbers:", odd)