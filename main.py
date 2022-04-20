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
    #myExecutable.printFileContents()
    #myExecutableSections = myExecutable.getSections()
    print(myExecutable.getSectionContents(".text"))
    print(myExecutable.getSectionFunctions(".text"))


if __name__=="__main__":
    main()