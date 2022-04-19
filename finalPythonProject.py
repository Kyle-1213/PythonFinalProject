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

class Assembly:
    """
    Class Assembly will take the name of an objdump file and
    allow parsing to be done on the file. One the parsing
    is primed, the parsed data will be sent to another function
    to provide further analysis. 
    Input:  objdump filename
    Output: Parsed objdump file
    """
    def __init__(self, fileName):
        """
        Sets objdump file equal to object and opens it.
        Initializes variables that will be added to
        Input: objdump filename
        Output: initialized variables
        """
        self.__assemblyFile = open(fileName, 'r')
        self.__functionHeaderDict = {}
        self.__functionHeaderContentsDict = {}
        self.__assemblyFileContents = self.__assemblyFile.readlines()
        
    def printFileContents(self):
        """
        Used if you want to print the contents of the objdump
        """
        print(self.__assemblyFileContents)
    def createFunctionDictionary(self):
        """
        Maps a memory address to the function name in a dictionary.
        I.E. memory address 1004 will contant the function "<_init>"
        Input:  Assembly 'self' object
        Output: Dictionary with memory address as key, function header as contents
        """
        # Go through each line of objdump file
        for line in self.__assemblyFileContents:
            # If you found function heading
            if line[0].isdigit() == True and line[-2] == ':':
                key = ""
                functionName = ""
                # Go through each char in line with function header
                for i in line:
                    # If it's a memory address
                    if i.isnumeric() == True:
                        key += i
                    # If it's a function header name
                    elif i != ' ' and i != ':' and i != '\n':
                        functionName += i
                # Create dictionary using key and function header name
                self.__functionHeaderDict[key] = functionName
    def createFunctionContentsDictionary(self):
        """
        Creates a dictionary where the key is the function heading name
        and the contents are lines that belong to that function header
        Input:  Assembly 'self' object
        Output: Dictionary with function header as key, function header contents as contents
        """
        readContents = False
        functionContents = ""
        key = ""
        # Go through each line of objdump file
        for line in self.__assemblyFileContents:
            # If a function header is found
            if line[0].isdigit() == True and line[-2] == ':':
                for i in line:
                    # If function header name is found
                    if i.isnumeric() == False and i != ':' and i != '\n' and i != ' ':
                        key+= i
                # Tell functionContents to read all lines that belong
                # to that function header
                readContents = True
            # If still reading contents of function header
            elif readContents == True:
                # If this line is no longer a part of the function header contents
                if line[0] != ' ' and line[0] != '_':
                    # Add contents of function header to dictionary
                    # stop reading each line into functionContents
                    # reset key and functionContents
                    self.__functionHeaderContentsDict[key] = functionContents
                    readContents = False
                    key = ""
                    functionContents = ""
                # Keep reading line into Function header's contents dictionary
                else:
                    functionContents += line
        # Used to catch last function header and contents
        self.__functionHeaderContentsDict[key] = functionContents
                    
    def printFunctionHeadingUsingKey(self, keyName):
        """
        prints function heading's name given it's memory address
        Input:  Assembly 'self object, memory address to find function 
                heading's name
        """
        print(self.__functionHeaderDict[keyName])
    def printFunctionHeadingNames(self):
        print(self.__functionHeaderContentsDict.keys())
    def printFunctionHeadingContent(self, headingName):
        print("Printing function header: " + headingName)
        print(self.__functionHeaderContentsDict[headingName])
    def organizeFunctionData(self):
        #self.__functionHeadContentsDict
        for key, data in self.__functionHeaderContentsDict.items():
            print(key)
                             
# Used to test and create objects
def main():
    myAssembly = Assembly("testDump.txt")
    myAssembly.createFunctionDictionary()
    #myAssembly.printFunctionHeadingUsingKey('0000000000001050')
    myAssembly.createFunctionContentsDictionary()
    #myAssembly.printFunctionHeadingNames()
    #myAssembly.printFunctionHeadingContent("<_init>")
    myAssembly.organizeFunctionData()
if __name__=="__main__":
    main()