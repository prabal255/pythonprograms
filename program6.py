
import time

print("1 to view a single file\n"
       "2 to create  file\n"
	"3 to copy file data'\n'"
	"4 to view multiples files data in a single command")
comm=input()
if comm == '1':
	f_name=input("enter a file name")
	f=open(f_name,'r')
	print(f.read())
elif comm =='2':
	f_name=input("enter a file name")
	f=open(f_name,'w')
	data=input("enter data without pressing enter")
	f.write(data)
elif comm=='3':
	f_name=input("enter a file name whose content to be copied")
	f=open(f_name,'r')
	data=f.read()
	f_name1=input("enter a file name in which data to be copied")
	f=open(f_name1,'a+')
	print('\n')
	f.write(data)
	f.seek(0)
	print('\n')
	print(f.read())
elif comm=='4':
	no=int(input("enter no. of files you want to view data"))
	li=[]
	for i in range(no):
		li=input("enter file name")
		li.append(li) #error line
	print(li)
	for i in li:
		f=open(i,'r')
		print('\n')
		print(f.read())
		time.sleep(1)	
