print("---------MENU--------")
print("1.String Concatination")
print("2.String Length")
print("3.String Uppercase")
print("4.String Lowercase")
print("5.String Indexing")
print("6.String Slicing")
print("7.Exit")
while(True):
    ch=int(input("Enter your choice :"))
    if(ch==1):
          s1=input("Enter first string")
          s2=input("Enter second string")
          print("Concatination stirng is :",s1+s2)
    elif(ch==2):
        s1=input("Enter string to find length ")
        print("Length of string is:",len(s1))
    elif(ch==3):
        s1=input("Enter string in lowercase:")
        print("Upper case string is:",s1.upper())
    elif(ch==4):
        s1=input("Enter string in uppercase")
        print("LOwercase string is",s1.lower())
    elif(ch==5):
        s1=input("Enter string for indexing")
        pos=int(input("Enter position to extract"))
        print("Character at position",pos,"is",s1[pos])
    elif(ch==6):
        s1=input("Enter string for slicing")
        start=int(input("Enter starting string to extract"))
        end=int(input("Enter ending string to extract"))
        print("Sliced string is:",s1[start:end])
    elif(ch==7):
        break
    else:
        print("Invalid chioce")
        
