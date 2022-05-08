""" main.py  
        
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

import turtle
# Import other class files
from classManageExecutable import *
from classSection import *
from classFunction import *

# List of all assembly calls to look for in x86 Assembly Language
assemblyCallsList = ["jmp", "je", "jz", "jne", "jnz", "js", "jns", "jg", "jnle", "jge",
                     "jnl", "jl", "jnge", "jle", "jng", "ja", "jnbe", "jae", "jnb", "jb",
                     "jnae", "jbe", "jna", "call", "leave", "ret"]

# ----- Global variables -----
myFile1 = ManageExecutable("testDump.txt")
myFile2 = ManageExecutable("dumpTest.txt")
SCREEN_SIZE_X = 1000
SCREEN_SIZE_Y = 500

def main():
    """
    Displays binary file, sections, and shows off the ability
    to print specific functions/sections as desired.
    Also runs mainloop to display tables
    Input:  N/A
    Output: Creates Python mainloop and keys can be pressed
            to display desired table
    """
    # Define turtle screen and size of screen.
    # The +50 is so that the edges of graph don't
    # overlap with end of screen.
    wn = turtle.Screen()
    wn.setup(SCREEN_SIZE_X+50, SCREEN_SIZE_Y+50)
    # Print entire binary file
    printFileContent(myFile2)
    # Print the functions from section .plt to fulfil
    # project requirements
    printFunctionsFromSection(myFile1, ".plt")
    # Draws assembly file table initially
    drawAssembly()
    # Allows user to draw assembly table or function table
    # by pressing a key
    wn.onkey(drawFunction, "f")
    wn.onkey(drawAssembly, "a")
    # Listens for key commands and runs in a loop, so keys can
    # continuously be pressed
    wn.listen()
    wn.mainloop()


def drawFunction():
    """
    Used by turtle.onkey() function to display chart.
    This function must have 0 parameters
    Input:  N/A
    Output: calls displayFunctionCalls() to display
            assembly table of commands
    """
    wn = turtle.Screen()
    wn.clear()
    # Tracer doesn't draw visually. Makes graphic print fast
    wn.tracer(0)
    # Sends to function to display table chart
    displayFunctionCalls(myFile2, SCREEN_SIZE_X, SCREEN_SIZE_Y)
    # Turns tracer back on to show whats been drawn
    wn.tracer(1)


def drawAssembly():
    """
    Used by turtle.onkey() function to display chart.
    This function must have 0 parameters
    Input:  N/A
    Output: calls displayAssemblyCalls() to display
            function calls in turtle-drawn table
    """
    wn = turtle.Screen()
    wn.clear()
     # Tracer doesn't draw visually. Makes graphic print fast
    wn.tracer(0)
    # Sends to function to display table chart
    displayAssemblyCalls(myFile2, SCREEN_SIZE_X, SCREEN_SIZE_Y)
    # Turns tracer back on to show whats been drawn
    wn.tracer(1)


def printFileContent(myFile):
    """
    Prints binary of selected binary object file
    Input:  N/A
    Output: Prints binary
    """
    myFile.printFileContents()


def printSections(myFile):
    """
    Prints all section objects contents
    Input:  Binary object file
    Output: Prints binary's sections
    """
    sectionList = myFile.getSectionList()
    # Cycle through section objects
    for section in sectionList:
        print("---------- Printing contents of section", section.getSectionName(), "----------")
        print(section.getSectionContents())


def printFunctionsFromSection(myFile, sectionName):
    """
    Prints spectific functions from provided section
    Input:  Binary object file, sectionName cooresponding to section object
    Output: Prints functions from section with sectionName
    """
    sectionList = myFile.getSectionList()
    # Cycle through section objects
    for section in sectionList:
        secName = section.getSectionName()
        if secName == sectionName:
            # Get function object lists of section
            functionList = myFile.getSectionFunctionList(sectionName)
            print("---------- Printing functions from section", sectionName, "----------")
            # Cycle through function objects from section
            for function in functionList:
                print(function.getFunctionName())
                print(function.getFunctionContents())


def createAssemblyCallList(myFile):
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


def displayAssemblyCalls(myFile, SCREEN_SIZE_X, SCREEN_SIZE_Y):
    assemblyList = createAssemblyCallList(myFile)

    #SCREEN_SIZE_X = 1000
    #SCREEN_SIZE_Y = 500  
    rowCount = len(assemblyList)
    height = SCREEN_SIZE_Y / rowCount
    width = SCREEN_SIZE_X / 5
    tableT = turtle.Turtle()
    tableT.speed('fastest')
    #wn = turtle.Screen()
    #wn.setup(SCREEN_SIZE_X+50, SCREEN_SIZE_Y+50)

    tableT.penup()
    tableT.goto(-SCREEN_SIZE_X/2, SCREEN_SIZE_Y/2)
    tableT.pendown()

    assemDictList = ["Memory Address", "Hex", "Instruction", "Registers", "Comment"]

    for i in range(1, rowCount+1):
        newWidth = width
        for j in range(5):
            tableT.forward(newWidth)
            newWidth = width*2
            tableT.right(90)
            tableT.forward(height)
            tableT.right(90)
            tableT.forward(width)
            tableT.right(90)
            tableT.forward(height)
            tableT.right(90)
            saveState = saveTurtleState(tableT)
            tableT.penup()
            tableT.forward(width/2)
            tableT.right(90)
            tableT.forward(height-1/2)
            if i == 1:
                tableT.write(assemDictList[j],move=False, font=('monaco',10,'bold'),align='center')
            else:
                myDictKey = list(assemblyList[i-1].keys())
                tableT.write(assemblyList[i-1].get(myDictKey[j]),move=False, font=('monaco',7),align='center')
            tableT.setheading(saveState[0])
            tableT.setposition(saveState[1])
            tableT.pendown()
        tableT.penup()
        tableT.goto(-SCREEN_SIZE_X/2, SCREEN_SIZE_Y/2 - (height*i))
        tableT.pendown()
    #wn.exitonclick()


def saveTurtleState(turtle):
    return turtle.heading(), turtle.position()


def createFunctionCallList(myFile):
    functionCallList = []
    sectionList = myFile.getSectionList()
    for section in sectionList:
        sectionName = section.getSectionName()
        functionList = myFile.getSectionFunctionList(sectionName)
        for func in functionList:
            functionDictionaryList = func.getFunctionDictionaryList()
            for dict in functionDictionaryList:
                comment = dict["comment"]
                commentList = list(comment.split(" "))
                commentList.remove(commentList[0])
                if len(commentList) > 1:
                    commentList.remove(commentList[0])
                    commentList.remove(commentList[0])
                    commentList.insert(0, dict["memAddress"])
                    functionCallList.append(commentList)
    return functionCallList


def displayFunctionCalls(myFile, SCREEN_SIZE_X, SCREEN_SIZE_Y):
    functionList = createFunctionCallList(myFile)

    #SCREEN_SIZE_X = 700
    #SCREEN_SIZE_Y = 400
    numColumns = 3
    rowCount = len(functionList)
    height = SCREEN_SIZE_Y / rowCount
    width = SCREEN_SIZE_X / numColumns
    tableTurt = turtle.Turtle()
    tableTurt.speed('fastest')
    #wn2 = turtle.Screen()
    #wn2.setup(SCREEN_SIZE_X+50, SCREEN_SIZE_Y+50)

    tableTurt.penup()
    tableTurt.goto(-SCREEN_SIZE_X/2, SCREEN_SIZE_Y/2)
    tableTurt.pendown()

    functionHeadingList = ["Address Location", "Function Memory Location", "Function Name"]

    for i in range(1, rowCount+1):
        newWidth = width
        for j in range(numColumns):
            tableTurt.forward(newWidth)
            newWidth = width*2
            tableTurt.right(90)
            tableTurt.forward(height)
            tableTurt.right(90)
            tableTurt.forward(width)
            tableTurt.right(90)
            tableTurt.forward(height)
            tableTurt.right(90)
            saveState = saveTurtleState(tableTurt)
            tableTurt.penup()
            tableTurt.forward(width/2)
            tableTurt.right(90)
            tableTurt.forward(height-1/2)
            if i == 1:
                tableTurt.write(functionHeadingList[j],move=False, font=('monaco',10,'bold'),align='center')
            else:
                #myDictKey = list(functionHeadingList[i-1].keys())
                tableTurt.write(functionList[i-1][j],move=False, font=('monaco',8),align='center')
            tableTurt.setheading(saveState[0])
            tableTurt.setposition(saveState[1])
            tableTurt.pendown()
        tableTurt.penup()
        tableTurt.goto(-SCREEN_SIZE_X/2, SCREEN_SIZE_Y/2 - (height*i))
        tableTurt.pendown()

    #wn2.exitonclick()

if __name__=="__main__":
    main()