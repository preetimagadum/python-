#number is divisible by 1 and itself is known as prime number
'''num = 11
flag = 0
for i in range(2,num):
  if num%i==0:   #‘%’ gives you the remainder part of the division.
    flag = 1
    break
if flag == 1:
  print("Not Prime number")
else:
  print("Prime number")'''

n=int(input("enter number:"))

for i in range(2,n):
  if n%i == 0:
    print(n,"number is not prime number")
    break
else:
  print(n,"number is prime number")