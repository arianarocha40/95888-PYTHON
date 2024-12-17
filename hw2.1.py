# -*- coding: utf-8 -*-
"""
@author: Ariana Rocha ANDREW ID: afrocha
"""
#Reading and printing file line by line to avoid crashing Spyder
def process(line):
    #function to process lines here
    print(line.strip()) # this only prints right now, we'll change to make chart appear

def shouldBeIncluded(line):
    #define criteria for including line in output
    ### looks for B and 81 stuff
    return 'B' in line

def charCheck(line):
    for char in line: 
        #look for digits or specific char
        if char.isdigit():
            # meaning number i think
            return True
        #example code for loking
        #if char =='$':
            #return True
    return False

HWFile = 'cme.20210709.c.pa2'
HWOutputFile = 'HW2.1 Output'

try:
    with open(HWFile, 'r') as sourceFile:   
        # no need content = sourceFile.read()
        with open(HWOutputFile, 'w') as outputFile:
            for line in sourceFile:
                if shouldBeIncluded(line):
                #print(line.strip())
                    process(line)
                    outputFile.write(line)
        print("Successfully processed and copied filtered content from HW to output")   
    #with open(HWOutputFile, 'w') as outputFile:
        #outputFile.write(content)
   # print("successfully copied from HW to output")

except FileNotFoundError:
    print("Source file DNE")
    
except IOError as e:
    print("IO Error occurred")



