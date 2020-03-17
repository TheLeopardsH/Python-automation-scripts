#!/usr/bin/python3
import sys
import re
import glob
#print(sys.argv)

#print(glob.glob("D:/*.txt"))
if len(sys.argv) == 4:
    print("you have entered arguments {0} ".format(sys.argv[1]),format(sys.argv[2]),format(sys.argv[3]))
else:
    sys.stderr.write("Usage python {0} # of arguments = ".format(sys.argv[0])+"4")

regexObj=re.compile(r'file1')
regexObj2=re.compile(sys.argv[1])

#for reading line by line(for task)
file1 = open(sys.argv[2], mode='r+',encoding='utf-8') # to
fileappend = open(sys.argv[3], "a")  # append mode

for line in file1:
    changereadline = regexObj.sub(sys.argv[1],line)
    checktest = regexObj2.search(changereadline)
    if checktest != None:
        fileappend.write(changereadline.rstrip())
        fileappend.write(" #comment added\n")
    else:
        fileappend.write(changereadline.rstrip())
        fileappend.write("\n")
    print(line)
    print(changereadline)

file1.close()
fileappend.close()
