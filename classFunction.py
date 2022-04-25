""" classFunction.py 
        
        Created by Kyle LeDoux
            Final Python Project in CS212 
    """


class Function():
    """
    Class will eventually contain attributes for
    each function.
    This will be a super class, where eventually every
    line in the funciton will have it's own attributes
    like memory address, hex value, instruction command,
    registers used. 
    """
    def __init__(self, functionName, functionContents):
        self.__functionName = functionName
        self.__functionContents = functionContents
        #if "<_start>" in functionName:
            #self.genAssemblyDictionary()


    def genAssemblyDictionary(self):
        """
        Take mem address, hex, instruction, register, comment
        from each line in function and put in dictionary
        Input:  Self 'function' object
        Output: Each assembly line part put in dictionary
        """
        memAddress = ""
        hex = ""
        instruction = ""
        registers = ""
        index = 0
        functionSeparator = self.__functionContents.split("\n")
        for line in functionSeparator:
            while("  " in line):
                line = line.replace("  ", " ")
            print(line)
            #for char in line:                


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