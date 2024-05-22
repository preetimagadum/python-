import requests
#print(dir())

from pymongo import MongoClient

resp=requests.get('https://jsonplaceholder.typicode.com/users')
user_list=resp.json()

print(type(user_list))
print(user_list)