import csv 

with open("county_.txt", "w") as result: 
	output=[]
	source_path="data/pasco_reshaped.csv" 
	listOfRows=list(csv.reader(open(source_path, "rb"), delimiter=","))
	print listOfRows