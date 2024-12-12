# Write a program that will give you the sum of three digits.

num = int(input("Enter the  number: "))
s=0
while num!=0:
    s+=num%10
    num=num//10


print(s)