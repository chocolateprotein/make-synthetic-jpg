import os
directory = os.listdir('/Users/test/synthetic/001')
os.chdir('/Users/test/synthetic/001')
#print (directory)
for file in directory :
    open_file = open(file,'r')
    #read_file = open_file.redd()