import csv
import json


with open("json.txt", "w") as my_json: 
	output=[]
	source_path="H_result.csv"
	listOfRows=list(csv.reader(open(source_path,"rb"), delimiter=","))
	for row in listOfRows: 
		# print row[13]
		if (row[4] == "REP" ) :  
			data={"Precinct": row[5], "Party":row[4], "Votes":row[-1]} 
			output.append(data)
		if (row[4] == "DEM" ) :  
			data={"Precinct": row[5], "Party":row[4], "Votes":row[-1]} 
			output.append(data)
	
	json.dump(output,my_json,indent=4, sort_keys=True, separators=(",", ":"))


# with open("votes.csv", "w") as my_csv: 

 
# 	source_path="H2012.txt"

# 	listOfRows=list(csv.reader(open(source_path,"rb"), delimiter="\t"))


# 	# votes= [] 
# 	# for row in listOfRows:
# 	# 	if row[-4] == "REP" : 
# 	# 		line="".join("%s %s %s" % (row[5],row[-4],row[-1]))
# 	# 		file.write(line + "\n")
# 	# 	elif row[-4] == "DEM" : 
# 	# 		line="".join("%s %s %s" % (row[5],row[-4],row[-1]))
# 	# 		file.write(line + "\n")

# 	csv.register_dialect(
# 	    'mydialect',
# 	    delimiter = ',',
# 	    quotechar = '"',
# 	    doublequote = True,
# 	    skipinitialspace = True,
# 	    lineterminator = '\r\n',
# 	    quoting = csv.QUOTE_MINIMAL)

	 
# 	csv_writer=csv.writer(my_csv, dialect="mydialect")

# 	for row in listOfRows: 
# 		if row[-4] == "REP" : 
# 			line="".join("%s %s %s" % (row[5],row[-4],row[-1]))
# 			csv_writer.writerow([row[5]] + [row[-4]] + [row[-1]])
# 		elif row[-4] == "DEM" : 
# 			line="".join("%s %s %s" % (row[5],row[-4],row[-1]))
# 			csv_writer.writerow([row[5]] + [row[-4]] + [row[-1]])
