def maxnum(x,y):
    if(x>y):
        return x
    else:
        return y

a=int(input("Enter a number"))
b=int(input("Enter another number"))
largest = maxnum(a,b)
print("largest number  is", largest)
