fp=None
try:
    fp=open('abc.txt','r')
except:
    fp=open('xyz.txt','r')
data=fp.read
print(data)

print("data read successfully")

fp.close()


