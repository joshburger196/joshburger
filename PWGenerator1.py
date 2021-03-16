########### CASE EXHAUST FUNCTIONS

def toggleCharCase(word,i): 
	if word[i]==word[i].lower(): #if the ith character is lowercase
		return word[0:i]+word[i].upper()+word[i+1:len(word)]
	else:
		return word[0:i]+word[i].lower()+word[i+1:len(word)]

def toggleWordCase(word,pattern):
	#word:"abbanoa" pattern:"110011" switches case of word where pattern is "1"
	
	#the pattern needs to be reversed for loop simplicity
	pattern=pattern[::-1]

	for i in range(0,len(pattern)): #cycle through pattern digits
		if word[i].isalpha() and pattern[i]=="1": #if char is a letter and pattern is 1
			word=toggleCharCase(word,i) #switch its case
	return word

def caseExhaust(word):
	#loop will cycle from 1 to 2^len(word)
	#i will be converted into the string of a binary number which will be used as a pattern
	#for toggleWord. All binary numbers will be hit and all patterns will be hit.
	comboList=[]
	for i in range(1,2**len(word)):
		comboList.append(toggleWordCase(word,("{0:b}".format(i))))
	return comboList
	

########### ADD SYMBOL FUNCTIONS

def addSymbolR(word):
	comboList=[]
	for symbol in symbolList:
		comboList.append(word+symbol)
	return comboList

def addSymbolL(word):
	comboList=[]
	for symbol in symbolList:
		comboList.append(symbol+word)
	return comboList
	
########### ADD NUM FUNCTION

def addNumR(word):
	comboList=[]
	for oneDigit in range(0,10):
		comboList.append(word+str(oneDigit))
	for twoDigits in range(0,100):
		twoDigits="{:02d}".format(twoDigits)
		comboList.append(word+twoDigits)
	for threeDigits in range(0,1000):
		threeDigits="{:03d}".format(threeDigits)
		comboList.append(word+threeDigits)
	for fourDigits in range(0,10000):
		fourDigits="{:04d}".format(fourDigits)
		comboList.append(word+fourDigits)
	return comboList

def addNumL(word):
	comboList=[]
	for oneDigit in range(0,10):
		comboList.append(str(oneDigit)+word)
	for twoDigits in range(0,100):
		twoDigits="{:02d}".format(twoDigits)
		comboList.append(twoDigits+word)
	for threeDigits in range(0,1000):
		threeDigits="{:03d}".format(threeDigits)
		comboList.append(threeDigits+word)
	for fourDigits in range(0,10000):
		fourDigits="{:04d}".format(fourDigits)
		comboList.append(fourDigits+word)
	return comboList
	
########### Substitute FUNCTIONS

def subNextChar(char):
	if char=="a":
		pass

########### START

symbolList=["!","@","#","\"","\'","&","£","$","%","=","?",".",","," "]
rootWords=["abbanoa"]

for word in rootWords:
	print(word)
	caseList=caseExhaust(word)
	for case in caseList:
		numCaseList=addNumR(case)
		for numCase in numCaseList:
			print(numCase)
		
		symbolCaseList=addSymbolR(case)
		for symbolCase in symbolCaseList:
			numSymbolCaseList=addNumR(symbolCase)
			for numSymbolCase in numSymbolCaseList:
				print(numSymbolCase)
			
			
			
			
			
