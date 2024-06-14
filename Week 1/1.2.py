Ramesh’s basic salary is input through the keyboard. His dearness allowance is 40% of his basic salary, and his house rent allowance is 20% of his basic salary. Write a program to calculate his gross salary.

a=int(input())
basicpay=a*(0.4)
hra=a*(0.2)
e=int(round(basicpay+hra,1))
grosspay=e+a
print(grosspay)

Sample Input:

10000

Sample Output:

16000
