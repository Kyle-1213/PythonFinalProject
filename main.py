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

assemblyCallsList = ["jmp", "je", "jz", "jne", "jnz", "js", "jns", "jg", "jnle", "jge",
                     "jnl", "jl", "jnge", "jle", "jng", "ja", "jnbe", "jae", "jnb", "jb",
                     "jnae", "jbe", "jna", "call", "leave", "ret"]
myFile1 = ManageExecutable("testDump.txt")
myFile2 = ManageExecutable("dumpTest.txt")
def main():

    SCREEN_SIZE_X = 1000
    SCREEN_SIZE_Y = 500
    wn = turtle.Screen()
    wn.setup(SCREEN_SIZE_X+50, SCREEN_SIZE_Y+50)
    
    printFileContentsPls(myFile1)
    printFunctionsFromSection(myFile1, ".plt")

    drawAssembly()
    wn.onkey(drawFunction, "f")
    wn.onkey(drawAssembly, "a")

    wn.listen()
    wn.mainloop()


def drawFunction():
    wn = turtle.Screen()
    wn.clear()

    SCREEN_SIZE_X = 1000
    SCREEN_SIZE_Y = 500
    displayFunctionCalls(myFile2, SCREEN_SIZE_X, SCREEN_SIZE_Y)


def drawAssembly():
    wn = turtle.Screen()
    wn.clear()

    SCREEN_SIZE_X = 1000
    SCREEN_SIZE_Y = 500
    displayAssemblyCalls(myFile2, SCREEN_SIZE_X, SCREEN_SIZE_Y)

def clearScreen(wn):
    wn.clearscreen()

def printFileContentsPls(myFile):
    myFile.printFileContents()


def printSections(myFile):
    sectionList = myFile.getSectionList()
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