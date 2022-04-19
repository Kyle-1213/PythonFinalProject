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
#import "classSection"
class Executable:
    def __init__(self, fileName):
        self.__executableFile = open(fileName, 'r')
        self.__executableFileContents = self.__executableFile.readline()
    def printFileContents(self):
        print(self.__executableFileContents)


def main():
    myExecutable = Executable("testDump.txt")
    myExecutable.printFileContents()
if __name__=="__main__":
    main()
