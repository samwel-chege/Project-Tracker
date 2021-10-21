# from abc import ABCMeta
# import requests
# import json

# from requests.sessions import session

# def login(email,password):
#     passw = requests.Session()
#     payload = {
#         'email':email,
#         'password':password
#     }
#     response = passw.post('http://127.0.0.1:8000/auth/login/',json=payload)
#     passw.headers.update({'authorization':json.loads(response.content)['tokens']})
#     print(response.content)
#     return passw
# session=login('chege.developer@gmail.com','string')