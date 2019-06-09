import time
import datetime
a=datetime.datetime.now()
print(a)
c=a.hour
#c=int(input("enter time")) ( if you want to check for any other input

if c >= 4 and c < 12 :
	print("good Morning")
elif c >= 12 and c < 16 :
	print("good afternoon")
elif c >= 16 and c < 20 :
	print("good evening ")
else :
	print("good night")
