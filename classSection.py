""" classSection.py 
        
        Created by Kyle LeDoux
            Final Python Project in CS212 
    """

class Section():
    """
    Each section from the executable will have its
    own attributes. Attributes include function objects that
    belong to that section.
    """

    # Create a static list of section objects
    sectionList = []
    @staticmethod
    def getSections():
        """
        Output: Return list of section objects
        """
        myList = []
        for x in Section.sectionList:
            myList.append(x)
        return myList


    def __init__(self, sectionName, sectionContents):
        """
        Add this section object to the list of section objects.
        Generate function objects of each section.

        Input:  Section name and contents
        Output: Initialize section name and contents to each section
                object, generate function objects in section.
        """
        Section.sectionList = Section.getSections()
        Section.sectionList.append(self)
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
                    functionList.append(line)
        return functionList


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