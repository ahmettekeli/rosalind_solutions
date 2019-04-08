def computeGCcontent(dataDict):
    percent = 0
    maxKey = ''
    for key,value in dataDict.items():
        seqSize = len(value)
        gcCount = value.count('G') + value.count('C')
        tempPerc = gcCount/seqSize *100
        if tempPerc>percent:
            percent=tempPerc
            maxKey = key
    print(maxKey)
    print(percent)

#Formatting data which is stored in a text file.
def textEdit():
    key = list()
    value = list()
    temp = ''
    arrayIndex = 0
    isfirstItem=True
    contentDict = {}
    file = open('rosalind_gc.txt','r')
    for line in file:
        if line[0] == '>':
            if isfirstItem:
                key.append(line.strip('\n'))
                isfirstItem=False
            else:
                key.append(line.strip('\n'))
                value.append(temp)
                temp=''
                arrayIndex = arrayIndex + 1
        else:
            temp = temp + line.strip('\n')
    value.append(temp)
    for i in range(0,len(key)):
        contentDict[key[i]] = value[i]
    return contentDict
         
computeGCcontent(textEdit())
        

