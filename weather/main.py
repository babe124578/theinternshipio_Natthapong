import xmltodict
import json

filename = str(input())
if filename[-4:]!=".xml":
    filename+=".xml"
try:
    with open(filename) as fd:
        doc = xmltodict.parse(fd.read())
except FileNotFoundError:
    print("File not found")
    input("Press ENTER to exit ...")
    exit(0)
jsonIC = json.dumps(doc)

a = jsonIC.replace("'","").replace("@","")
out = ""
for i in range(len(a)):
    out+=a[i]
    if a[i] == "{":
        out += "\n"
    if a[i] == ",":
        out += "\n"
    if i+1<len(a) and a[i+1] == "}":
        out += "\n"
    
listOfLine = out.splitlines(False)
listOfLine.pop(1)
listOfLine[-1] = listOfLine[-1][0:-1]
del listOfLine[-1]

stackList = []
lineCount = 0
for i in listOfLine:
    if i[-1] == "{":
        stackList.append(lineCount)
    if i[0] == "}":
        for j in range(len(listOfLine)):
            if len(stackList) != 0 and (int(stackList[-1]) < j < lineCount):
                if listOfLine[j][0]==' ':
                    listOfLine[j] = "   "+listOfLine[j]
                else:
                    listOfLine[j] = "    "+listOfLine[j]
        if len(stackList) != 0:        
            del stackList[-1]
    lineCount += 1
file = open("weather.JSON","w")
for i in listOfLine:
    print(i) 
    file.write(i+"\n") 
file.close() 
