""" classFunction.py 
        
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

class Function():
    """
    Create a dictionary for each line of a function. Used
    so one can find a specific memory line, instruction,
    register, etc. from a specific function.
    """
    def __init__(self, functionName, functionContents):
        self.__functionName = functionName
        self.__functionContents = functionContents
        self.__functionDictionaryList = []
        self.genAssemblyDictionary()
        #print(self.__functionDictionaryList)


    def genAssemblyDictionary(self):
        """
        Take mem address, hex, instruction, register, comment
        from each line in function and put in dictionary. Add
        dictionary to list so there's a list of dictionaries
        Input:  Self 'function' object
        Output: Each assembly line part put in dictionary,
                added to list of dictionaries
        """
        assemblyCallsList = ["jmp", "je", "jz", "jne", "jnz", "js", "jns", "jg", "jnle", "jge",
                     "jnl", "jl", "jnge", "jle", "jng", "ja", "jnbe", "jae", "jnb", "jb",
                     "jnae", "jbe", "jna", "call", "leave", "ret"]
    
        # Take long string and separate by new lines
        functionSeparator = self.__functionContents.split("\n")
        # Go through each line of function's contents
        for line in functionSeparator:
            # Variable decarations
            lineDict = {}
            memAddress = ""
            myHex = ""
            instruction = ""
            registers = ""
            comment = ""
            # Take tabs and turn them into 3 spaces to be parsed by split
            line = line.replace("\t", "   ")
            # Create a list of words separated by three spaces
            lis = list(line.split("   "))
            # Take out empty words in list
            for a in lis:
                # Keyword for taking out empty string
                if not a:
                    lis.remove(a)
            # Some empty strings not take out
            if len(lis) > 1:
                memAddress = lis[0]
                memAddress = memAddress[:-1]
                myHex = lis[1]
                # If line has a comment
                if '#' in lis[-1]:
                    comment = lis[-1]
                    registers = "None"
                    if len(lis[-2]) > 1:
                        registers = lis[-2]
                    #registers = lis[-2]
                    instruction = lis[-3]
                # If not comment, put "None" for comment
                else:
                    comment = "None"
                    registers = "None"
                    if len(lis[-1]) > 1:
                        registers = lis[-1]
                    instruction = lis[-2]
            # Create a dictionary of each line in function
            lineDict["memAddress"] = memAddress
            lineDict["hex"] = myHex
            lineDict["instruction"] = instruction
            lineDict["registers"] = registers
            lineDict["comment"] = comment
            # Create list of dictionaries for function
            self.__functionDictionaryList.append(lineDict)


    def getFunctionName(self):
        """
        Return this objects function name
        Input:  Self 'function' object
        """
        return self.__functionName


    def getFunctionContents(self):
        """
        Return this objects function contents
        Input:  Self 'function' object
        """
        return self.__functionContents


    def getFunctionDictionaryList(self):
        """
        Returns list of all lines in a dictionary, sorted by
        the lines memory address, hex, instruction, registers,
        and comments.
        Input:  Function 'self' object
        Output: Returns list of dictionarys for lines in function
        """
        return self.__functionDictionaryList
