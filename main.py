""" main.py  
        
        Created by Kyle LeDoux
            Final Python Project in CS212 
    """

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

""" Import other class files """
from classManageExecutable import *
from classSection import *
from classFunction import *


def main():
    myExecutable = ManageExecutable("testDump.txt")
    #print("\nGetting file contents...\n")
    #myExecutable.printFileContents()
    #myExecutableSections = myExecutable.getSections()
    #print("\nPrinting executable's sections...\n")
    #print(myExecutable.getSections())
    #print("\nPrinting contents for section 'text'...\n")
    #print(myExecutable.getSectionContents(".text"))
    sectionList = myExecutable.getSectionList()
    for a in sectionList:
        secName = a.getSectionName()
        secFunctionList = myExecutable.getSectionFunctionList(secName)
        print("Section name...")
        print(secName)
        for b in secFunctionList:
            print("Function Name...")
            print(b.getFunctionName())
            print("Function", b.getFunctionName(), "contents...")
            print(b.getFunctionContents())
            functionDictList = b.getFunctionDictionaryList()
            for line in functionDictList:
                #print(line["instruction"])
                if "call" in line["instruction"]:
                    print("Function", b.getFunctionName(), "contains a 'call' at line:", line["memAddress"])

    #myExecutable.getSections()
    #myExecutable.getSectionFunctionList(".text")

if __name__=="__main__":
    main()
