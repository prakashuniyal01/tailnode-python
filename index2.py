
     
     
# ---------------index2.py -------------------#


import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')
print(response.text)

