""" classSection.py 
        
        Created by Kyle LeDoux
            Final Python Project in CS212 
    """


from classFunction import *


class Section():
    """
    Each section from the executable will have its
    own attributes. Attributes include function objects that
    belong to that section.
    """

    def __init__(self, sectionName, sectionContents):
        """
        Add this section object to the list of section objects.
        Generate function objects of each section.

        Input:  Section name and contents
        Output: Initialize section name and contents to each section
                object, generate function objects in section.
        """
        self.__sectionName = sectionName
        self.__sectionContents = sectionContents
        self.__functionList = self.generateFunction()
                    

    def generateFunction(self):
        """
        Input:  Section 'self' object
        Output: Creates a list of function objects with
                its own attributes in classFunction
        """
        functionList = []
        # So string of function contents aren't all on one continuous line
        sectionSeparator = self.__sectionContents.split("\n")
        for line in sectionSeparator:
            # So empty lines don't give error when accessing line[0]
            if line != '\n' and line != '':
                # If function found, add to list
                if line[0].isdigit() == True and line[-1] == ':':
                    functionName = list(line.split(" "))
                    functionName[-1] = functionName[-1][:-1]
                    functionName = functionName[-1]
                    # Get functions contents from function. Used for creating
                    # Function object
                    functionContents = self.getFunctionContents(functionName)
                    # Create list of function objects
                    functionList.append(Function(functionName, functionContents))
        # Return list of function objects for this section
        return functionList

    
    def getFunctionContents(self, functionName):
        """
        Returns function contents given function name
        Input:  Section 'self' object, function's name
        Output: Contents of dictionary that pertain to function name
        """

        # Take string and separate into lines by '\n' char
        sectionSeparator = self.__sectionContents.split("\n")
        readOn = False
        functionContents = ""
        for line in sectionSeparator:
            # Get rid of unwanted lines
            if line != '\n' and line != '':
                # If funciton name found, start reading
                if functionName in line:
                    readOn = True
                # If new function is found, stop reading
                elif line[0].isdigit() == True and line[-1] == ':':
                    readOn = False
                # Keep reading if section contents still belong to function
                elif readOn == True:
                    line = line + '\n'
                    functionContents += line
        # Return total of section's contents
        return functionContents


    def getFunctionList(self):
        """
        Input:  section 'self' object
        Output: Returns list of function objects
        """
        return self.__functionList


    def getSectionContents(self):
        """
        Input:  section 'self' object
        Output: returns contents of this section object
        """
        return self.__sectionContents


    def getSectionName(self):
        """
        Input:  section 'self' object
        Output: returns the name of this section object
        """
        return self.__sectionName
