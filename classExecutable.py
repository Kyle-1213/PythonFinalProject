"""
Year and Semester    : 2022 SPRING
Course Number        : CS-212
Course Title         : Practical Python
Work Number          : Final Project
Work Name            : Final Python Project
Work Version         : Version 1
Long Date            : May 2022
Author(s) Name(s)    : Kyle LeDoux
"""
#import "classSection"
class Executable:
    def __init__(self, fileName):
        self.__executableFile = open(fileName, 'r')
        self.__executableFileContents = self.__executableFile.readlines()
        self.generateSections()
        self.test()
    def generateSections(self):
        for line in self.__executableFileContents:
            if "Disassembly of section" in line:
                sentenceList = list(line.split(" "))
                sectionName = sentenceList[len(sentenceList)-1]
                self.generateSectionContents(sectionName)
    def generateSectionContents(self, sectionName):
        sectionContents = ""
        readOn = False
        #print(sectionName)
        for line in self.__executableFileContents:
            if sectionName in line and "Disassembly of section" in line:
                readOn = True
            elif(("Disassembly of section" not in line) and readOn == True):
                    sectionContents += line
            elif(("Disassembly of section" in line and sectionName not in line)):
                readOn = False
        Section(sectionName, sectionContents)
    def printFileContents(self):
        print(self.__executableFileContents)
    def test(self):
        print("yes")

class Section():
    sectionList = []
    @staticmethod
    def getSections():
        myList = []
        for x in Section.sectionList:
            myList.append(x)
        return myList
    def __init__(self, sectionName, sectionContents):
        Section.sectionList = Section.getSections()
        Section.sectionList.append(self)
        self.sectionList.append(sectionName)
        self.__sectionContents = sectionContents

def main():
    myExecutable = Executable("testDump.txt")
    #myExecutable.printFileContents()
if __name__=="__main__":
    main()
