import os, sys, json, re

FILE_TYPES = [".tif", ".exr", ".png"]
IGNORE_FILE_TYPES = [".tx", ".json"]
MAKETX_PATH = "PATH TO maketx.exe"
CMD_FLAGS = "-v -u --oiio --checknan --filter lanczos3"

# @@ https://stackoverflow.com/questions/287871/print-in-terminal-with-colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def failStr(str):
    return  bcolors.FAIL + str + bcolors.ENDC

def warnStr(str):
    return  bcolors.WARNING + str + bcolors.ENDC

def arrayAllowToStr(array):
    return warnStr("(allowed: " + ' '.join(array) + ")")

# ====================================

path = sys.argv[1]
error_list = []
def errorLog(entryPath, errorType, extra=""):
    error_list.append(failStr(entryPath.replace(path, '') + ": ") + "not converted" + " " + extra)

def checkFileExtension(entryPath):
    if os.path.isfile(entryPath):
        filename, extension = os.path.splitext(entryPath)
        if extension.lower() not in FILE_TYPES:
            if extension.lower() not in IGNORE_FILE_TYPES:
                errorLog(entryPath, "extension", arrayAllowToStr(FILE_TYPES))
        return extension.lower() in FILE_TYPES
    else: 
        return False


# Loop throught directories and check tree
currentRootEntries = os.listdir(path)
for rootEntry in currentRootEntries:
    currentPath = path + "\\" + rootEntry
    filename, extension = os.path.splitext(currentPath)
    if checkFileExtension(currentPath):
        command = MAKETX_PATH + " " + CMD_FLAGS + " " + currentPath + " -o " + filename + ".tx"
        os.system(command)

# End of script, print each error
print path
for err in error_list:
    print err
