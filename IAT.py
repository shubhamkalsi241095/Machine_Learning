# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 00:58:10 2019

@author: user
"""
import pathlib
import pefile
import os
import errno
import csv
s=dict()
lst=[]
#Appending each file of benignware folder to a list
path = 'C:\\Users\\user\\Desktop\\Project\\benignware\\'
currentDirectory = pathlib.Path('C:\\Users\\user\\Desktop\\Project\\benignware',delim_whitespace=True)
for filename in os.listdir(currentDirectory):
    try: 
        file2 = pefile.PE(path+filename)
        if file2.OPTIONAL_HEADER.DATA_DIRECTORY[pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_IMPORT']].VirtualAddress == 0:
            pass
        else:
            for entry in file2.DIRECTORY_ENTRY_IMPORT:      
                for imp in entry.imports:
                    continue
                lst.append(entry.dll)
    except IOError as exc:
        if exc.errno != errno.EISDIR:
            raise
#Appending each file of malware folder to a list            
path2='C:\\Users\\user\\Desktop\\Project\\z\\'
currentDirectory2 = pathlib.Path('C:\\Users\\user\\Desktop\\Project\\z',delim_whitespace=True)
for filename2 in os.listdir(currentDirectory2):
    try: 
        file3 = pefile.PE(path2+filename2)
        if file3.OPTIONAL_HEADER.DATA_DIRECTORY[pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_IMPORT']].VirtualAddress == 0:
            pass
        else:
            for entry2 in file3.DIRECTORY_ENTRY_IMPORT:      #Testing on other file
                for imp2 in entry2.imports:
                    continue
                lst.append(entry2.dll)
    except IOError as exc:
        if exc.errno != errno.EISDIR:
            raise
#collecting distinct dll in header            
header = set()
for j in lst:
    header.add(j)
with open('Malware_dll_benignware.csv', 'a') as f:
    writer = csv.writer(f ,  quoting=csv.QUOTE_ALL,lineterminator='\n')
    writer.writerow(header)
    
#Comparing each file to the header and displaying the count if the dll is present in a file  
for filename in os.listdir(currentDirectory):
     try: 
        file2 = pefile.PE(path+filename)
        if file2.OPTIONAL_HEADER.DATA_DIRECTORY[pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_IMPORT']].VirtualAddress == 0:
            pass
        else:
            counter=0
            for entry in file2.DIRECTORY_ENTRY_IMPORT:      #Testing on other file
                for imp in entry.imports:
                    counter=counter+1
                s.update({entry.dll:counter})
            for h in header:
                if h not in s.keys():
                    s[h]=0
            with open('Malware_dll_benignware.csv','a') as fj:
                writer = csv.writer(fj ,  quoting=csv.QUOTE_ALL,lineterminator='\n')
                writer.writerow(s.keys())
                writer.writerow(s.values())
            counter=0
     except IOError as exc:
        if exc.errno != errno.EISDIR:
            raise
    
d=dict()
for filename2 in os.listdir(currentDirectory2):
     try: 
        file3 = pefile.PE(path2+filename2)
        if file3.OPTIONAL_HEADER.DATA_DIRECTORY[pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_IMPORT']].VirtualAddress == 0:
            pass
        else:
            counter1=0
            for entry2 in file3.DIRECTORY_ENTRY_IMPORT:      #Testing on other file
                for imp2 in entry2.imports:
                    counter1=counter1+1
                d.update({entry2.dll:counter1})
            for h in header:
                if h not in d.keys():
                    d[h]=0
            with open('Malware_dll_benignware.csv','a') as fm:
                writer = csv.writer(fm ,  quoting=csv.QUOTE_ALL,lineterminator='\n')
                writer.writerow(d.keys())
                writer.writerow(d.values())
            counter1=0
     except IOError as exc:
        if exc.errno != errno.EISDIR:
            raise
    
