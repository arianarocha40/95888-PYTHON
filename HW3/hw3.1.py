# -*- coding: utf-8 -*-
"""
@author: arian
Andrew ID: afrocha
Name: Ariana Rocha
Data Focused Python hw3.1 -- SECTION 1
"""
#SECTION 1: Lists, Tuples, Sets, Dicts, and Comprehensions

## PART A: 
records = [] #initializes the first empty list

with open('expenses.txt', 'r') as file:     
    for line in file:                       
        records.append(line.rstrip('\n'))   
        
    for line in records:                    
        print(line)                        
        
## PART B: 
with open('expenses.txt', 'r') as file:
    records2 = [line.rstrip('\n') for line in file]
print("\nrecords == records2:", records == records2, '\n')

## PART C: 
with open('expenses.txt', 'r') as file:
    records3 = tuple(tuple(line.rstrip('\n').split(':')) for line in file)

for tup in records:
    print(tup)
    
## PART D:
cat_set = {tup[1] for tup in records3 if tup[1] != 'Category'}
date_set = {tup[2] for tup in records3 if tup[2] != 'Date'}

print('Categories:', cat_set, '\n')
print('Dates:',date_set,'\n')

## PART E:
rec_num_to_record = {i: record for i, record in enumerate(records3)}

print('Range Format')
for rn in range(len(rec_num_to_record)):
    print('{:3d}: {}'.format(rn,
                             rec_num_to_record[rn]))

print('\nUsing items() Format')
for i in rec_num_to_record.items():
    print('{:3d}: {}'.format(i[0],i[1]))
    

print('\nUsing tuple unpacking Format')
for k, v in rec_num_to_record.items():
    print('{:3d}: {}'.format(k,v))











