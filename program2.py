adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
gr=[]
eq=[]
for i in adhoc :
	if i > 5 :
		print(i)
		gr.append(i)
	if i <= 2:
		print(i)
		eq.append(i)

print(eq)
print (gr)
