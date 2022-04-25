""" classManageExecutable   
        
        Created by Kyle LeDoux
            Final Python Project in CS212 
    """


from classSection import *
from classFunction import *

class ManageExecutable():
    """
    Main driver of code. Attaches executable name to object.
    This object will have different attributes. 
    The first attribute is Sections. Each section will then have it's own
    list of function from the section class. Then, each section will have
    a list of functions that belongs to it, with the function having its 
    own data structure for instruction memory addresses, hex, instruction
    command, registers.

    Input:  Filename of executable
    Output: Sections, functions of sections, and attributes of functions
            created. 
    """


    def __init__(self, fileName):
        """
        Input:  Filename of executable
        Output: Sections, functions of sections, and attributes of functions
                created. 
        """
        self.__executableFile = open(fileName, 'r')
        self.__executableFileContents = self.__executableFile.readlines()
        self.generateSections()


    def generateSections(self):
        """
        Get section name from executable. Send each section
        name to generateSectionContents, where a section object
        will be made with section name and contents.
        
        Input:  ManageExecutable 'self' object
        Output: Section name found and sent to generateSectionContents
        """
        for line in self.__executableFileContents:
            # If a section is found in executable
            if "Disassembly of section" in line:
                # Create a list of that line
                sentenceList = list(line.split(" "))
                # Takes of new line from sectionName
                sentenceList[-1] = sentenceList[-1][:-1]
                # Take the last work in that list of words in line
                # and set that as the section name
                sectionName = sentenceList[len(sentenceList)-1]
                self.generateSectionContents(sectionName)


    def generateSectionContents(self, sectionName):
        """
        Finds the section contents that coorespond to the section name.

        Input:  sectionName to find its contents
        Output: Section object created with section name and contents
        """
        sectionContents = ""
        readOn = False
        for line in self.__executableFileContents:
            # If same name from before is found, we can start reading the next line
            if sectionName in line and "Disassembly of section" in line:
                readOn = True
            # Save section contents, excluding empty lines in section
            elif(("Disassembly of section" not in line) and readOn == True and line != "\n" and line != ''):
                    sectionContents += line
            # Stop reading section contents
            elif(("Disassembly of section" in line and sectionName not in line)):
                readOn = False
        # Create section data structure using sectionName and sectionContents
        Section(sectionName, sectionContents)


    def printFileContents(self):
        """
        Used by user to print executable if they so desire
        """
        for line in self.__executableFileContents:
            print(line,end="")
        

    def getFile(self):
        """
        Can get file object is desired
        """
        return self.__executableFileContents


    def getSections(self):
        """
        Generates a list of all section objects in executable file

        Input:  ManageExecutable 'self' object
        Output: List of section objects
        """
        myList = []
        for a in Section.getSections():
            myList.append(a.getSectionName())
        return myList


    def getSectionContents(self, sectionName):
        """
        Given a specific section to look at, return
        the contents of that section.

        Input:  section name to be returned
        Output: contents cooresponding to section name
        """
        for a in Section.getSections():
            if sectionName in a.getSectionName():
                return a.getSectionContents()
    def getSectionNames(self):
        mySectionList = []
        for a in Section.getSections():
            mySectionList.append(a.getSectionName())
        return mySectionList

    def getSectionFunctions(self, sectionName):
        """
        Return a list of functions that belong to that specific 
        section.

        Input:  section you want to find the functions for
        Output: returned function objects list that coorespond
                to the section provided
        """
        for a in Section.getSections():
            if sectionName in a.getSectionName():
                return a.getFunctionList()
