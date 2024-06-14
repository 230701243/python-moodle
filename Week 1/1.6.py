Justin is a carpenter who works on an hourly basis. He works in a company where he is paid Rs 50 for an hour on weekdays and Rs 80 for an hour on weekends. He works 10 hrs more on weekdays than weekends. If the salary paid for him is given, write a program to find the number of hours he has worked on weekdays and weekends.

  s=int(input())
x=(s-500)/130
absolute=abs(x)
print("weekdays",format(10+absolute,".2f"))
print("weekend",format(absolute,".2f"))

Sample Input:

450

Sample Output:

weekdays 10.38

weekend 0.38
