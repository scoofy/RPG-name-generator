import os, re

def grabNames():
    nameDict={}

    #filePath = 'C:/Users/David/AppData/Local/Programs/Python/Python36/RPG-name-generator-master/names/'
    filePath = 'names/'
    fileNames = os.listdir(filePath) #get a list of all the name datafiles
    fileNames.remove('__init__.py')


    for nameGroup in fileNames: 
        nameSplit = re.split('([A-Z].*)\.',nameGroup) #Identify the name family (orc, human, tavern, etc.)
        with open(filePath + nameGroup) as myfile:
            fileText = myfile.read()
            
            while True:
                
                try:
                    
                    nameDict[nameSplit[0]][nameSplit[1]] = fileText[8:-3].split()
                    break
                except:
                    nameDict[nameSplit[0]]= {}


    print (nameDict)
       

grabNames()
