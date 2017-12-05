import os, re

def grabNames():
    #load all name data from the names folder into a single dictionary of dictionaries
    #top level = race/entity (tavern, orc, human, party, etc)
    #second level =name element (L1, F1F, A1 etc
    #assumptions:
    #.    All files in the names fokder contain name data
    #.    File names are in the format [entity][ELEMENT CODE]
    #.    File name case is important
    
    nameDict={}

    #filePath = 'C:/Users/David/AppData/Local/Programs/Python/Python36/RPG-name-generator-master/names/'
    filePath = 'names/'
    fileNames = os.listdir(filePath) #get a list of all the files in the names directory
    fileNames.remove('__init__.py')

    for nameGroup in fileNames: 
        nameSplit = re.split('([A-Z].*)\.',nameGroup) #Identify the name family (orc, human, tavern, etc.)
        with open(filePath + nameGroup) as myfile#:
            fileText = myfile.read()
            
            while True:
                
                try:
                    
                    nameDict[nameSplit[0]][nameSplit[1]] = fileText[8:-3].split()
                    break
                except:
                    nameDict[nameSplit[0]]= {}


    print (nameDict)
       

grabNames()
