# -*- coding: utf-8 -*-
"""
Author: Ariana Rocha
AndrewID: afrocha
Python HW5
"""
import re

# Step 1: Read data from expenses.txt and store it in a list
records = []

# Open the expenses.txt file and read the lines (no new line char)
with open(r'C:\Users\arian\OneDrive\Documents\CMU-A_Laptop2\CLASSES\PYTHON\HW5\expenses.txt', 'r') as f:
    records = [line.strip() for line in f]

# PART 1a: Lines that contain a 'D'
# Pattern to match any line containing the letter 'D'
pat = r'D'
for line in records:
    if re.search(pat, line):
        print(line)

# PART 1b: Lines with (')
#Comment out the previous part and use this pattern
#pat = r"\'"
#for line in records:
#    if re.search(pat, line):
#        print(line)

# PART 1c: Lines with (")
#pat = r'\"'
#for line in records:
#    if re.search(pat, line):
#        print(line)

# PART 1d: Lines start w/ '7'
#pat = r'^7'
#for line in records:
#    if re.search(pat, line):
#        print(line)

# PART 1e: Lines end w/ 'r' or 't'
#pat = r'[rt]$'
#for line in records:
#    if re.search(pat, line):
#        print(line)

# PART 1f: Lines that contain (.)
#pat = r'\.'
#for line in records:
#    if re.search(pat, line):
#        print(line)

# PART 1g: Lines that contain an 'r' then a 'g'
#pat = r'r.*g'
#for line in records:
#    if re.search(pat, line):
#        print(line)

# PART 1h: Lines w/ two consecutive uppercase letters
#pat = r'[A-Z]{2}'
#for line in records:
#    if re.search(pat, line):
#        print(line)

# PART 1i: Lines w a comma
#pat = r','
#for line in records:
#    if re.search(pat, line):
#        print(line)

# PART 1j: Lines w three or more commas
#pat = r'(.*,){3,}'
#for line in records:
#    if re.search(pat, line):
#        print(line)

# PART 1k: Lines w/out letters v, w, x, y, or z
#pat = r'^[^vwxyz]*$'
#for line in records:
#    if re.search(pat, line):
#        print(line)

# PART 1l: Lines w/ $$ b/w 10.00 and 99.99
#pat = r'\b[1-9]\d\.\d{2}\b'
#for line in records:
#    if re.search(pat, line):
#        print(line)

# PART 1m: Lines w exactly three commas
#pat = r'(.*?,){3}$'
#for line in records:
#    if re.search(pat, line):
#        print(line)

# PART 1n: Lines w an open parenthesis '('
#pat = r'\('
#for line in records:
#    if re.search(pat, line):
#        print(line)

# PART 1o: Lines that describe meals costing >= 100.00
#pat = r'\bmeal\b.*\b1\d{2}\.\d{2}\b'
#for line in records:
#    if re.search(pat, line):
#        print(line)

# PART 1p: Lines with expense exactly four characters wide
#pat = r'\b\w{4}\b'
#for line in records:
#    if re.search(pat, line):
#        print(line)

# PART 1q: Lines for expenses in March (Dates starting with '201703')
#pat = r'\b201703\b'
#for line in records:
#    if re.search(pat, line):
#        print(line)

# PART 1r: Lines that contain an 'abc'
#pat = r'a.*b.*c'
#for line in records:
#    if re.search(pat, line):
#        print(line)

# PART 1s: Lines w a sequence of 2x characters repeated three times
#pat = r'(\w\w).*\1.*\1'
#for line in records:
#    if re.search(pat, line):
#        print(line)

# PART 1t: Lines w description contains a lowercase 'a' and a digit 0-9 in any order
#pat = r'[aA].*[0-9]|[0-9].*[aA]'
#for line in records:
#    if re.search(pat, line):
#        print(line)

# PART 1u: Lines w/ no uppercase letters
#pat = r'^[^A-Z]*$'
#for line in records:
#    if re.search(pat, line):
#        print(line)

# PART 1v: Lines w 'd' possibly followed by one optional character and then an 'i'
#pat = r'd.?i'
#for line in records:
#    if re.search(pat, line):
#        print(line)
