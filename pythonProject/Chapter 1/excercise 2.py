#excercise percentage calculation
#data retrieval
yes= int(input("YES"))
no= int(input("NO"))
blank= int(input("BLANK"))
#% calc
# yes+no+blank -> total/votes*100
total= (yes+no+blank)
yes_percentage= (yes/total*100)
no_percentage= (no/total*100)
blank_percentage = (blank/total*100)
#print results
#print ("YES"+ str(yes%)+"\n""NO"+str(no%)+"\n""BLANK"+str(blank_percentage))
print("YES:"+ str(yes_percentage) +'%')
print("NO:"+ str(no_percentage) +"%")
print ("BlANK:"+ str(blank_percentage) +"%")