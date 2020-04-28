if __name__ == "__main__":
	#file have 3 columns: TF_Name	TF_Species	Family_Name
	f = open("tfName_specie_TFFamily_fromCISBP.txt","r")
	data = {}
	for line in f:
		aux = line[:-1].split("\t")
		if aux[1].replace("_"," ") not in data:
			data[aux[1].replace("_"," ")] = {}
		if aux[2] not in data[aux[1].replace("_"," ")]:
			data[aux[1].replace("_"," ")][aux[2]] = []
		if aux[0] not in data[aux[1].replace("_"," ")][aux[2]]:
			data[aux[1].replace("_"," ")][aux[2]].append(aux[0])

	f = open("data","w")
	for key in data:
		f.write("{"+key+":"+str(data[key])+",\n")
	
	f.close()
