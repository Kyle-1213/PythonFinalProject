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

import turtle
""" Import other class files """
from classManageExecutable import *
from classSection import *
from classFunction import *

myFile1 = ManageExecutable("testDump.txt")
assemblyCallsList = ["jmp", "je", "jz", "jne", "jnz", "js", "jns", "jg", "jnle", "jge",
                     "jnl", "jl", "jnge", "jle", "jng", "ja", "jnbe", "jae", "jnb", "jb",
                     "jnae", "jbe", "jna", "call", "leave", "ret"]

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
            #print(b.getFunctionContents())
            functionDictList = b.getFunctionDictionaryList()
            for line in functionDictList:
                #print(line["instruction"])
                if "call" in line["instruction"]:
                    print("Function", b.getFunctionName(), "contains a 'call' at line:", line["memAddress"])

    #myExecutable.getSections()
    #myExecutable.getSectionFunctionList(".text")

#if __name__=="__main__":
#    main()
def printFileContents():
    myFile1.printFileContents()


def printSections():
    sectionList = myFile1.getSectionList()
    for section in sectionList:
        print("---------- Printing section", section.getSectionName() + "'s contents ----------")
        print(section.getSectionContents())

def printFunctionsFromSection(myFile, sectionName):
    sectionList = myFile.getSectionList()
    for section in sectionList:
        secName = section.getSectionName()
        if secName == sectionName:
            functionList = myFile.getSectionFunctionList(sectionName)
            print("---------- Printing functions from section", sectionName, "----------")
            for function in functionList:
                print(function.getFunctionName())
                print(function.getFunctionContents())


def createFunctionCallList(myFile):
    assemblyCallList = []
    sectionList = myFile.getSectionList()
    for section in sectionList:
        sectionName = section.getSectionName()
        functionList = myFile.getSectionFunctionList(sectionName)
        for func in functionList:
            functionDictionaryList = func.getFunctionDictionaryList()
            for dict in functionDictionaryList:
                for inst in assemblyCallsList:
                    if inst in dict["instruction"]:
                        assemblyCallList.append(dict)
    return assemblyCallList
def displayAssemblyCalls(myFile):
    assemblyList = createFunctionCallList(myFile)

    SCREEN_SIZE = 800
    rowCount = len(assemblyList)+1
    height = SCREEN_SIZE / rowCount
    width = SCREEN_SIZE / 5
    tableT = turtle.Turtle()
    tableT.speed('fastest')
    wn = turtle.Screen()
    wn.setup(SCREEN_SIZE+50, SCREEN_SIZE+50)

    tableT.penup()
    tableT.goto(-SCREEN_SIZE/2, SCREEN_SIZE/2)
    tableT.pendown()

    for i in range(1, rowCount+1):
        newHeight = height
        newWidth = width
        for j in range(1,6):
            tableT.forward(width*j)
            tableT.right(90)
            tableT.forward(height*i)
            tableT.right(90)
            tableT.forward(width)
            tableT.right(90)
            tableT.forward(height)
            tableT.right(90)

            #tableT.goto(-SCREEN_SIZE/2, SCREEN_SIZE/2 - (height*i))


    wn.exitonclick()
#main()
printSections()
printFunctionsFromSection(myFile1, ".plt")
#createFunctionCallList(myFile1)
displayAssemblyCalls(myFile1)