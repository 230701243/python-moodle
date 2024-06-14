Write a program to convert strings to an integer and float and display its type.

a=int(input())
b=float(input())
print(a,end=",")
print(type(a))
print(round(b,1),end=",")
print(type(b))

Sample Input:

10

10.9

Sample Output:

10,<class 'int'>

10.9,<class 'float'>

