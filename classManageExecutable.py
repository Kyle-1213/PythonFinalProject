""" classManageExecutable   
        
        Created by Kyle LeDoux
            Final Python Project in CS212 
    """
"""
Year and Semester    : 2022 SPRING
Course Number        : CS-212
Course Title         : Practical Python
Work Number          : HA-17
Work Name            : Final Project Deliverables
Work Version         : Version 1
Long Date            : Sunday, 8 May 2022
Author(s) Name(s)    : Kyle LeDoux
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
        self.__sectionList = []
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
                sentenceList[-1] = sentenceList[-1][:-2]
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
            secName = list(line.split(" "))
            secName[-1] = secName[-1][:-2]
            # If same name from before is found, we can start reading the next line
            if sectionName in line and "Disassembly of section" in line and sectionName == secName[-1]:
                readOn = True
            # Save section contents, excluding empty lines in section
            elif(("Disassembly of section" not in line) and readOn == True and line != "\n" and line != ''):
                    sectionContents += line
            # Stop reading section contents
            elif("Disassembly of section" in line):
                    readOn = False
        # Create section data structure using sectionName and sectionContents
        #print(sectionName)
        self.genSectionList(Section(sectionName, sectionContents))


    def genSectionList(self, sectionObj):
        """
        Can get file object if desired
        """
        self.__sectionList.append(sectionObj)


    def printFileContents(self):
        """
        Used by user to print executable if they so desire
        """
        for line in self.__executableFileContents:
            print(line,end="")


    def getSectionList(self):
        """
        Get list of section objects
        Input:  Executable 'self' object
        Output: List of section object that belong to executable file
        """
        return self.__sectionList


    def getSections(self):
        """
        Generates a list of all section objects in executable file

        Input:  ManageExecutable 'self' object
        Output: List of section objects
        """
        for a in self.__sectionList:
            print(a.getSectionName())


    def getSectionFunctionList(self, mySection):
        """
        Get list of object functions given the section name
        Input:  Executable 'self' object, section's name
        Output: List of section's function objects
        """
        for a in self.__sectionList:
            if mySection == a.getSectionName():
                return a.getFunctionList()
