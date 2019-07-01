file1 = open("record.txt", "a") 

while 1 :
	x = raw_input()
	file1.write(x + '\n')
	if x == "close" :
		
		break

file1.close()
