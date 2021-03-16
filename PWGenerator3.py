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

symbolList=["!","@","#","\"","\'","&","£","$","%","=","?",".",","," "]

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

subSequence={
"a":"A", "A":"4", "4":"@", "@":"a", #"à":"^", "^":"a",
"b":"B", "B":"8", "8":"b",
"c":"C", "C":"c",
"d":"D", "D":"d",
"e":"E", "E":"3", "3":"è", "è":"é", "é":"£", "£":"&", "&":"e",
"f":"F", "F":"f",
"g":"G", "G":"g",
"h":"H", "H":"h",
"i":"I", "I":"1", "1":"!", "!":"i", #"ì":"i",
"j":"J", "J":"j",
"k":"K", "K":"j",
"l":"L", "L":"l",
"m":"M", "M":"w", #goes to w
"n":"N", "N":"u", #goes to u
"o":"O", "O":"0", "0":"o", #"ò":"°", "°":"o",
"p":"P", "P":"p",
"q":"Q", "Q":"q",
"r":"R", "R":"r",
"s":"S", "S":"$", "$":"5", "5":"s",
"t":"T", "T":"t",
"u":"U", "U":"n", #goes to n
"v":"V", "V":"v",
"w":"W", "W":"m", #goes to m
"x":"X", "X":"%", "%":"+", "+":"*", "*":"#", "#":"x",
"y":"Y", "Y":"y",
"z":"Z", "Z":"2", "2":"z"
}

def nextChar(char):
	if char in subSequence:
		return subSequence[char]

def nextWord(word):
	return nextChar(word[0])+word[1:]

def cycleWord(root):
	cycleList=[]
	word=root
	i=0
	
	word=word[0:i]+nextWord(word[i:])
	
	while(word[i]!=root[i]): #cycle through character family
		print(word)
		print("root[i]="+root[i]+" word[i]="+word[i])
		cycleList.append(word)
		word=word[0:i]+nextWord(word[i:])
	if(word[])
	return cycleList
		

########### START


rootWords=["abbanoa"]

for word in rootWords:
	print(word)
	cycleList=cycleWord(word)
	for cycle in cycleList:
		pass#print(cycle)
	




"""
abbanoa
Abbanoa
4bbanoa
@bbanoa
aBbanoa
ABbanoa
4Bbanoa
@Bbanoa
a8banoa
"""
