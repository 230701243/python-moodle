Write a program that returns the last digit of the given number. Last digit is being referred to the least significant digit i.e. the digit in the ones (units) place in the given number.

The last digit should be returned as a positive number.

n=int(input())
if(n>0):
    a=n%10
    print(abs(a))
else:
        a=n%10
        a+=4
        print(a)

Input	Result
197
7
-197
7
