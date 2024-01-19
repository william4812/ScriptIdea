#!/usr/bin/env python3                   
import os
import sys
import logging

class OSDIS():
    def getOsInfo(self):
        print(f'The name of the OS module it imports is {os.name}.\n')

    def getPID(self):
        print(f'Current process ID or P ID is {os.getpid()}.')

    def getPythonExe(self):
        print(f'The python exectible is located at {sys.executable}.')

    def getCurDir(self):
        return os.getcwd()

    def getLog(self):
        return logging.debug( getCurDir() )
    
    def showLogging(self):
        logging.basicConfig(level = logging.DEBUG, 
                    format = ' %(asctime)s -  %(levelname)s -  %(message)s')

        logging.debug('Start of program')

def main():
    
    osObj = OSDIS()
    osObj.getOsInfo()
    osObj.getPID()
    osObj.getPythonExe()
    osObj.showLogging()

    #print(f"{os.environ['home']}")

    ## run other commands on the system
    #program = "python"
    #arguments = ["hello.py"]
    #print(os.execvp(program, (program,) +  tuple(arguments)))
    
    

    #currentFiles = os.system("'test' > users.txt")

if __name__ == "__main__":
    main()