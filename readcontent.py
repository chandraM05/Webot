
f = open("../metainfo/Acne.txt","r")
primary_data = f.readlines()
f.close()

content=""
for i in primary_data :
	content=content+i
vendor = content.split(">>>")
for i in vendor :
	features=i.split(" ! ")
	print features
	break