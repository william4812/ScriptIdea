#!/usr/bin/env python3                   
import os
import sys
import logging

def getOsInfo():
    print(f'The name of the OS module it imports is {os.name}.\n')

def getPID():
    print(f'Current process ID or P ID is {os.getpid()}.')

def getPythonExe():
    print(f'The python exectible is located at {sys.executable}.')

def getCurDir():
    return os.getcwd()

def getLog():
    return logging.debug( getCurDir() )

def main():
    
    getOsInfo()

    getPID()

    getPythonExe()

    #print(f"{os.environ['home']}")

    ## run other commands on the system
    #program = "python"
    #arguments = ["hello.py"]
    #print(os.execvp(program, (program,) +  tuple(arguments)))
    
    

    #currentFiles = os.system("'test' > users.txt")

if __name__ == "__main__":
    main()