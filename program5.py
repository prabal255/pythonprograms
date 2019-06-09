import webbrowser
from googlesearch import search

f=open("url.txt","w")
web = input("Enter topic to search : ")
for i in search(web,stop=10):
	f.write(i)
	print(i)
	print("\n")
webbrowser.open("https://www.google.com/search?q="+web)

