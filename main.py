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
    """
    Creates a list of all assembly lines with an assembly call
    Input:  Binary object file
    Output: List of all assembly calls in binary and locations
    """
    assemblyCallList = []
    sectionList = myFile.getSectionList()
    for section in sectionList:
        sectionName = section.getSectionName()
        functionList = myFile.getSectionFunctionList(sectionName)
        # Cycle through functions of sections
        for func in functionList:
            functionDictionaryList = func.getFunctionDictionaryList()
            # Cycle through dictionary list
            for dict in functionDictionaryList:
                # Find instructions for assembly lines and add to list
                # if they belong to the function call lists made above
                for inst in assemblyCallsList:
                    if inst in dict["instruction"]:
                        assemblyCallList.append(dict)
    return assemblyCallList


def displayAssemblyCalls(myFile):
    """
    Uses list assembly call list generated from createAssemblyCallList()
    Input:  Binary object file
    Output: Table of assembly calls from turtle module
    """
    assemblyList = createAssemblyCallList(myFile)
    rowCount = len(assemblyList)
    # How big each box should be
    height = SCREEN_SIZE_Y / rowCount
    # Amount of columns for table
    width = SCREEN_SIZE_X / 5

    tableT = turtle.Turtle()
    tableT.speed('fastest')
    # Go to top left corner of turtle screen
    tableT.penup()
    tableT.goto(-SCREEN_SIZE_X/2, SCREEN_SIZE_Y/2)
    tableT.pendown()
    # Used to write in turtle table
    assemDictList = ["Memory Address", "Hex", "Instruction", "Registers", "Comment"]
    # For each box x, y (or i,j) of table
    for i in range(1, rowCount+1):
        newWidth = width
        for j in range(5):
            # Create table box 
            tableT.forward(newWidth)
            newWidth = width*2
            tableT.right(90)
            tableT.forward(height)
            tableT.right(90)
            tableT.forward(width)
            tableT.right(90)
            tableT.forward(height)
            tableT.right(90)
            # Saves where the turtle is at the current moment so the name
            # that goes in said box can be written in
            saveState = saveTurtleState(tableT)
            tableT.penup()
            # Go down to center of box
            tableT.forward(width/2)
            tableT.right(90)
            tableT.forward(height-1/2)
            # If if the title of table
            if i == 1:
                tableT.write(assemDictList[j],move=False, font=('monaco',10,'bold'),align='center')
            # Not title of table, put contents of assembly line
            else:
                myDictKey = list(assemblyList[i-1].keys())
                tableT.write(assemblyList[i-1].get(myDictKey[j]),move=False, font=('monaco',7),align='center')
            # Resore where turtle was
            tableT.setheading(saveState[0])
            tableT.setposition(saveState[1])
            tableT.pendown()
        # Go back to far left of screen and correct heigh for current row
        tableT.penup()
        tableT.goto(-SCREEN_SIZE_X/2, SCREEN_SIZE_Y/2 - (height*i))
        tableT.pendown()


def saveTurtleState(turtle):
    """
    Save where the turtle is currently
    Input:  Turtle object
    Output: Direction of turtle and x/y position
    """
    return turtle.heading(), turtle.position()


def createFunctionCallList(myFile):
    """
    Creates a list of all function calls
    Input:  Binary object file
    Output: List of all function calls in binary and locations
    """
    functionCallList = []
    sectionList = myFile.getSectionList()
    for section in sectionList:
        sectionName = section.getSectionName()
        functionList = myFile.getSectionFunctionList(sectionName)
        # Cycle through functions of sections
        for func in functionList:
            functionDictionaryList = func.getFunctionDictionaryList()
            # Cycle through dictionary list in function
            for dict in functionDictionaryList:
                # Get comment from assembly line dictionary
                comment = dict["comment"]
                # Split comment into words
                commentList = list(comment.split(" "))
                # Remove unneeded part of comment
                commentList.remove(commentList[0])
                # If it's a real comment
                if len(commentList) > 1:
                    # Remove unneeded wordds
                    commentList.remove(commentList[0])
                    commentList.remove(commentList[0])
                    # Add function call to lists
                    commentList.insert(0, dict["memAddress"])
                    functionCallList.append(commentList)
    return functionCallList


def displayFunctionCalls(myFile, SCREEN_SIZE_X, SCREEN_SIZE_Y):
    functionList = createFunctionCallList(myFile)
    # Three columns for address of assembly line, address of function
    # and function name being called
    numColumns = 3
    rowCount = len(functionList)
    # Uses to put table row/colum into right position based on screen size
    height = SCREEN_SIZE_Y / rowCount
    width = SCREEN_SIZE_X / numColumns
    tableTurt = turtle.Turtle()
    tableTurt.speed('fastest')
    # Go to top left corner of screen
    tableTurt.penup()
    tableTurt.goto(-SCREEN_SIZE_X/2, SCREEN_SIZE_Y/2)
    tableTurt.pendown()
    # Create a list of headings
    functionHeadingList = ["Address Location", "Function Memory Location", "Function Name"]
    # For row, column of table
    for i in range(1, rowCount+1):
        newWidth = width
        for j in range(numColumns):
            # Create box for table
            tableTurt.forward(newWidth)
            newWidth = width*2
            tableTurt.right(90)
            tableTurt.forward(height)
            tableTurt.right(90)
            tableTurt.forward(width)
            tableTurt.right(90)
            tableTurt.forward(height)
            tableTurt.right(90)
            # Save where current turtle is
            saveState = saveTurtleState(tableTurt)
            tableTurt.penup()
            # Go to center of box to write what goes in spot in table
            tableTurt.forward(width/2)
            tableTurt.right(90)
            tableTurt.forward(height-1/2)
            # If it's a heading
            if i == 1:
                tableTurt.write(functionHeadingList[j],move=False, font=('monaco',10,'bold'),align='center')
            else:
                #  Write in the table box
                tableTurt.write(functionList[i-1][j],move=False, font=('monaco',8),align='center')
            # Restore where turtle is
            tableTurt.setheading(saveState[0])
            tableTurt.setposition(saveState[1])
            tableTurt.pendown()
        # Go back to far left of screen and correct heigh for current row
        tableTurt.penup()
        tableTurt.goto(-SCREEN_SIZE_X/2, SCREEN_SIZE_Y/2 - (height*i))
        tableTurt.pendown()

# Call main at end of file
if __name__=="__main__":
    main()