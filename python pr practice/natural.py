'''num=int(input("Enter a number:"))

if num<0:
    print("please enter positive number")
else :
    sum=0
    while num>0:
        sum += num # sum=sum+num returns the sum of all numerical values provided in an iterable. 
        num -=1  #num= num-1
print(sum) '''

array=[1,3,4,5,6]

ans=sum(array)
print("sum of array is",ans)