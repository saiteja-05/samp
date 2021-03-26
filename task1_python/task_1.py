# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 19:05:16 2021

@author: tejan
"""

#import pandas as pd
#data=pd.read_csv("sample_input.csv",header=None)
#data.columns =['MSISDN', 'operation type', 'service indication', 'Time Stamp','status']
#to filter the unique MSISDN
#df=data.drop_duplicates('MSISDN')



#first question
from csv import reader

l1 = ['MSISDN']
with open('sample_input.csv', 'r') as f:
	csv_reader = reader(f)
	for row in csv_reader:
		if(row[0] not in l1):
			print(row[0] + ' ' + row[1] + ' ' + row[2])
			l1.append(row[0])




##2nd question(using pandas)
##input from console
##indication =input("Enter Service indication(VM_SUBPROFILE or SMS_SUBPROFILE):")
##print("you entered: ",indication)
##input from file
#input = open('indic.txt','r')
#n=input.read()
#if n=='VM_SUBPROFILE':
    #print(data[data['service indication']=='VM_SUBPROFILE'])
#    VM_S=data[data['service indication']=='VM_SUBPROFILE']
#    VM_S.to_csv("VM_SUBPROFILE.csv")
#elif n == "SMS_SUBPROFILE":
#    #print(data[data['service indication']=='SMS_SUBPROFILE'])
#    SMS_S=data[data['service indication']=='SMS_SUBPROFILE']
#    SMS_S.to_csv("SMS_SUBPROFILE.csv")



#second question set1
input = open('indic.txt','r')
indication=input.read()
    
with open('sample_input.csv', 'r') as read_obj:
	csv_reader = reader(read_obj)
	for row in csv_reader:
		if(row[2] == indication):
			print(row[0] + ' '+ row[1] + ' ' + row[2] + ' '+ row[3] + ' '+ row[4])



#-------------------------------------------------------


#set2 

import csv
print("begin writing xml")




#reader=csv.reader(open("sample_input.csv",'r'),delimiter=',')

reader=csv.reader(open("VM_SUBPROFILE.csv",'r'),delimiter=',')
next(reader)

#open xml file

f=open('VM_SUBPROFILE.xml','w')
#f=open('x.xml','w')

#xml declaration

f.write('<?xml version="1.0" encoding="UTF-8"?>')

#xml root element

f.write('<Audit xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="schema.xsd">')

for row in reader:
    #xml child element
    f.write('    '+'<auditSubscribers>')
    f.write('    '+'<MSISDN>'+row[0]+'</MSISDN>')
    f.write('    '+'<OperationType>'+row[1]+'</OperationType>')
    f.write('    '+'<ServiceIndication>'+row[2]+'</ServiceIndication>')
    f.write('    '+'</auditSubscribers>')
    
#xml end root element

f.write('</Audit>')
f.close()
print("finished writing xml")




#limiting with the batch size 

import csv
print("begin writing xml")

n=input("enter the batch size")

#reader=csv.reader(open("sample_input.csv",'r'),delimiter=',')
reader=csv.reader(open("VM_SUBPROFILE.csv",'r'),delimiter=',')
next(reader)

#open xml file
f=open('VM_SUB(limited).xml','w')
#f=open('x.xml','w')

#xml declaration
f.write('<?xml version="1.0" encoding="UTF-8"?>')

#xml root element
f.write('<Audit xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="schema.xsd">')

count=0
for row in reader:
    #xml child element
    f.write('    '+'<auditSubscribers>')
    f.write('    '+'<MSISDN>'+row[0]+'</MSISDN>')
    f.write('    '+'<OperationType>'+row[1]+'</OperationType>')
    f.write('    '+'<ServiceIndication>'+row[2]+'</ServiceIndication>')
    f.write('    '+'</auditSubscribers>')
    count=count+1
    if count == n :
        break
        
#xml end root element
f.write('</Audit>')
f.close()
print("finished writing xml")


#----------------------------------------------------------------

#set3

import logging 

LOG_FORMAT="%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="D:\\tasks\\task1_python\\s.log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,filemode='w')

#logger=logging.getLogger()

logging.debug("hiiiiii")
logging.info("dzvdsfsdfvfsd")
logging.warning("hi thui sis sai")
logging.error("check this out")
logging.critical("entire stream is down")
logging.error("check this out---------------")




