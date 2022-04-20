

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
        self.__sectionName = sectionName
        self.__sectionContents = sectionContents
        self.__functionList = self.generateFunction()
    def generateFunction(self):
        functionList = []
        sectionSeparator = self.__sectionContents.split("\n")
        for line in sectionSeparator:
            if line != '\n' and line != '':
                if line[0].isdigit() == True and line[-1] == ':':
                    functionList.append(line)
        return functionList
    def getFunctionList(self):
        return self.__functionList
    def getSectionContents(self):
        return self.__sectionContents
    def getSectionName(self):
        return self.__sectionName