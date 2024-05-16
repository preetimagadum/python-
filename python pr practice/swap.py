'''x=int(input("Enter first value(a):"))
y=int(input("Enter second value(b):"))
print(f"original values x={x}, y={y}")

temp=x
x=y
y=temp
print(f"swapped values x={y}, y={y}")'''

P = int( input("Please enter value for P: "))  
Q = int( input("Please enter value for Q: "))  
    
temp= P  
P = Q  
Q = temp 
   
print ("The Value of P after swapping: ", P)  
print ("The Value of Q after swapping: ", Q)  