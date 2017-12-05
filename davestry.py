import os, re

def grabNames():
    #load all name data from the names folder into a single dictionary of dictionaries
    #top level = race/entity (tavern, orc, human, party, etc)
    #second level =name element (L1, F1F, A1 etc)
    #assumptions:
    #.    All files in the names fokder contain name data
    #.    File names are in the format [entity][ELEMENT CODE]
    #.    File name case is important
    
    nameDict={}

    #filePath = 'C:/Users/David/AppData/Local/Programs/Python/Python36/RPG-name-generator-master/names/'
    filePath = 'names/'
    fileList = os.listdir(filePath) #get a list of all the files in the names directory
    fileList.remove('__init__.py')

    for nameFile in fileList: 
        nameSplit = re.split('([A-Z].*)\.', nameFile) #break apart entity name(orc, human, tavern, etc.) from element type (L1, etc.)
        with open(filePath +  nameFile) as myfile:
            fileText = myfile.read() #read the content of the current file
            
            while True:
                #store the list of name elements from the current file under the appropriate dictionary key
                #nameSplit[0] will be the entity type (orc, tavern, etc.)
                #nameSplit[1] will be the element type (L1, F1M, A1, etc.)
                try:                    
                    nameDict[nameSplit[0]][nameSplit[1]] = fileText[8:-3].split()
                    break
                except:
                    nameDict[nameSplit[0]]= {}

    #print (nameDict)
      

#grabNames()
