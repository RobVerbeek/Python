#calculations garden fence
# length=50 #int
# width=30 #int
length=int(input("length?"))
width=int(input("width?")) #input returns datatype string
#step 2 calculate perimeter
perimeter=(length+width)*2
#step 3 print
print("perimeter fence:"+ str(perimeter)) #+ concatenate -> conversion
print("perimeter fence", perimeter) #, concatenate -> no conversion
print(type(perimeter))