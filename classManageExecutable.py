""" Class Executable   
    Created by Kyle LeDoux
    Final Python Project in CS212 
    """


from classSection import *

class ManageExecutable():
    """
    Main driver of code. Attaches executable name to object.
    This object will have different attributes. The first attribute
    is Sections. Each section will then have it's own functions
    """
    def __init__(self, fileName):
        self.__executableFile = open(fileName, 'r')
        self.__executableFileContents = self.__executableFile.readlines()
        self.generateSections()
    def generateSections(self):
        for line in self.__executableFileContents:
            if "Disassembly of section" in line:
                sentenceList = list(line.split(" "))
                sectionName = sentenceList[len(sentenceList)-1]
                self.generateSectionContents(sectionName)
    def generateSectionContents(self, sectionName):
        sectionContents = ""
        readOn = False
        for line in self.__executableFileContents:
            if sectionName in line and "Disassembly of section" in line:
                readOn = True
            elif(("Disassembly of section" not in line) and readOn == True and line != "\n" and line != ''):
                    sectionContents += line
            elif(("Disassembly of section" in line and sectionName not in line)):
                readOn = False
        Section(sectionName, sectionContents)
    def printFileContents(self):
        for line in self.__executableFileContents:
            print(line,end="")
    def getFile(self):
        return self.__executableFileContents
    def getSections(self):
        myList = []
        for a in Section.getSections():
            myList.append(a)
        return myList
    def getSectionContents(self, sectionName):
        for a in Section.getSections():
            if sectionName in a.getSectionName():
                return a.getSectionContents()
    def getSectionFunctions(self, sectionName):
        for a in Section.getSections():
            if sectionName in a.getSectionName():
                return a.getFunctionList()
