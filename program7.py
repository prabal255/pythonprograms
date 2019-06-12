import os 
print("1 : to create single file")
print("2 : to create multiple file")
inp=input()

if inp == '1':
	file_= input("enter file name : ")
	f=open(file_ ,'a')
	
elif inp =='2' :
	no=int(input("enter no. of files you want to create"))
	for i in range(no):
		file_ = input("enter file name")
		f=open(file_,'a')
else:
	os.path.getmtime(home/adhoc/hello.txt)
