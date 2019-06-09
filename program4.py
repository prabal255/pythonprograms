import os
import crypt
username=input("Enter your Username--->")
no_prsnt=0
for i in username:
	if(i.isdigit()):
		no_prsnt=1
		if(no._prsnt==1):
			print("Invalid User Name")
		break
		
else:
	password="hello"+username
	encripting = crypt.crypt(password,"22") #Encrypting Password
	os.system("useradd -p " + encripting +" "+username)
print("CONGRATUALION I HAVE ADDED AN USER")
print("username--->",username)
print(":password---> ","hello"+username)

