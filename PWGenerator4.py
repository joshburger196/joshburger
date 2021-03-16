########### ADD SYMBOL FUNCTIONS

symbolList=["!","@","#","%","&","£","$","€","?","."]

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
	
########### ADD NUM FUNCTIONS

def add4NumR(word):
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

def add4NumL(word):
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

def add3NumR(word):
	comboList=[]
	for oneDigit in range(0,10):
		comboList.append(word+str(oneDigit))
	for twoDigits in range(0,100):
		twoDigits="{:02d}".format(twoDigits)
		comboList.append(word+twoDigits)
	for threeDigits in range(0,1000):
		threeDigits="{:03d}".format(threeDigits)
		comboList.append(word+threeDigits)
	return comboList
	
def addYearR(word):
	comboList=[]
	for i in range(1900,2023):
		comboList.append(word+str(i))
	return comboList

def addYearL(word):
	comboList=[]
	for i in range(1900,2023):
		comboList.append(str(i)+word)
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
"m":"M", "M":"m",
"n":"N", "N":"n",
"o":"O", "O":"0", "0":"o", #"ò":"°", "°":"o",
"p":"P", "P":"p",
"q":"Q", "Q":"q",
"r":"R", "R":"r",
"s":"S", "S":"$", "$":"5", "5":"s",
"t":"T", "T":"t",
"u":"U", "U":"u",
"v":"V", "V":"v",
"w":"W", "W":"w",
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
	
	if len(word)==1: #if the word is a character THEN return list with the character family
		word=nextChar(word) #cycle to the next character in the family
		cycleList.append(word) #add it to the list
		#print("I'm passing "+word+" to whoever called me")
		while root!=word: #until it turns back to the original character
			word=nextChar(word) #cycle to the next character in the family
			cycleList.append(word) #add it to the list
			#print("I'm passing "+word+" to whoever called me")
		
	elif len(word)>1: #if word is more than a character
	
		"""
		divide the algorythm in smaller problems:
		use recursion to get a list of all combinations
		of a chunk of the word: the word without the first char.
		Once you have a list of all combos of the chunk,
		add them to all possible combination of the first char.
		"""
		
		chunkList=cycleWord(word[1:]) #ask the recursion to find all combos of the smller chunk
		for chunk in chunkList: #cycle through each possible chunk
			word=nextChar(word[0])+chunk #add this combo of chunk to this cycle of char
			cycleList.append(word) #add result to the list
			#print("I'm passing "+word+" to whoever called me")
			while root[0]!=word[0]: #until char[0] turns back to the original
				word=nextChar(word[0])+chunk #add this combo of chunk to this cycle of char
				cycleList.append(word) #add result to the list
				#print("I'm passing "+word+" to whoever called me")
	return cycleList
		

########### START


rootWords=["dauvea"]

for word in rootWords:
	cycleList=cycleWord(word) #4bb4n0a
	for cycle in cycleList:
		print(cycle)
		
		cycleYearList=addYearR(cycle) #abbanoa2021
		for cycleYear in cycleYearList:
			print(cycleYear)
		
		cycleSymbList=addSymbolR(cycle) #abbanoa€
		for cycleSymb in cycleSymbList:
			print(cycleSymb)
		
			cycleSymbYearList=addYearR(cycleSymb) #abbanoa€2021
			for cycleSymbYear in cycleSymbYearList:
				print(cycleSymbYear)
				
		"""
		symbCycleList=addSymbolL(cycle) #€abbanoa
		for symbCycle in symbCycleList:
			print(symbCycle)
			
			yearSymbCycleList=addYearL(symbCycle) #2021€abbanoa
			for yearSymbCycle in yearSymbCycleList:
				print(yearSymbCycle)"""
		
				
		
	









