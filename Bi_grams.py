# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 02:52:31 2019

@author: user
"""

import binascii
import nltk
import collections
import pathlib
import csv
import os
from collections import Counter

bigram1 = set()
with open('C:/Users/user/Desktop/Project/benignware/factor.exe', 'rb') as f:
    for i in iter(lambda:f.read(),b''):#Converting a benign file into a hex file and then creating bi-grams.
        s=binascii.hexlify(i)
        d=nltk.bigrams(s)
    
    counts=Counter(d)
    f=set(counts)
    print(counts)
    for k in f:
        bigram1.add(k)
    with open('Malware_dataset6.csv', 'a') as f:
        writer = csv.writer(f ,  quoting=csv.QUOTE_ALL,lineterminator='\n')
        writer.writerow(bigram1)
    
#Iterating through each file in benignware folder and add the freguency of each bi-grams into the respective columns.
path2 = 'C:\\Users\\user\\Desktop\\Project\\benignware\\'
currentDirectory5 = pathlib.Path('C:\\Users\\user\\Desktop\\Project\\benignware',delim_whitespace=True)
currentDirectory = pathlib.Path("C:\\Users\\user\\Desktop\\Project")
for filename2 in os.listdir(currentDirectory5):
        with open(path2+filename2,'rb') as f:
                for i in iter(lambda:f.read(),b''):
                    s=binascii.hexlify(i)
                    d=nltk.bigrams(s)
                counts1=Counter(d)
               
              
    #print(z.keys())
   
                fj=set(counts1)
                for bi in bigram1:
                    if bi not in counts1:
                        counts1[bi]=0
                with open('Malware_dataset6.csv', 'a') as f:
                    writer = csv.writer(f ,  quoting=csv.QUOTE_ALL,lineterminator='\n')
                    writer.writerow(counts1.keys())
                    writer.writerow(counts1.values())

#Now doing the same with malware files
bigram2 = set()
with open('C:/Users/user/Desktop/Project/z/101.file', 'rb') as f1:
    for j in iter(lambda:f1.read(),b''):
        s1=binascii.hexlify(j)
        d1=nltk.bigrams(s1)
    
    counts_mal=Counter(d1)
    malware=set(counts_mal)
    for k in malware:
        bigram2.add(k)
    with open('Malware_dataset11.csv', 'a') as f:
        writer = csv.writer(f ,  quoting=csv.QUOTE_ALL,lineterminator='\n')
        writer.writerow(bigram2)

path = 'C:\\Users\\user\\Desktop\\Project\\z\\'
currentDirectory = pathlib.Path('C:\\Users\\user\\Desktop\\Project\\z',delim_whitespace=True)
for filename_malware in os.listdir(currentDirectory):
        with open(path+filename_malware,'rb') as f:
                for i in iter(lambda:f.read(),b''):
                    hex_dump=binascii.hexlify(i)
                    created_biagrams=nltk.bigrams(hex_dump)
                counts_malware=Counter(created_biagrams)
                f_malware=set(counts_malware)
                for bi in bigram2:
                    if bi not in counts_malware:
                        counts_malware[bi]=0
                with open('Malware_dataset11.csv', 'a') as f:
                    writer = csv.writer(f ,  quoting=csv.QUOTE_ALL,lineterminator='\n')
                    writer.writerow(counts_malware.keys())
                    writer.writerow(counts_malware.values())