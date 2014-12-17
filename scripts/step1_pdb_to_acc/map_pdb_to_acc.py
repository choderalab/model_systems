# Writes output of Uniprot Accession Numbers that corresponds to PDB IDs given as input
#
# run this from model_systems directory as
# usage:    python scripts/step1_pdb_to_acc/map_pdb_to_acc.py input_path/input_file
#           python scripts/step1_pdb_to_acc/map_pdb_to_acc.py input/step1/pdb_list_from_bindingDB_validationDB.txt
#
#  modified from Uniprot help, programmatic access
# this one must be called with another pdb list file as an argument
# uniqify function from http://www.peterbe.com/plog/uniqifiers-benchmark

import urllib, urllib2
from sys import argv
import os

# Eliminates repeating entries from list. Returns a list with unique elements in the same order
def uniqify_list(a_list): 
   # order preserving
   unique_list = []
   for e in a_list:
       if e not in unique_list:
           unique_list.append(e)
   return unique_list


# unpacking and reading input
script, filename = argv
PDB_file = open(filename)

# uniprot mapping
url = 'http://www.uniprot.org/mapping/'

#str_pdb = raw_input("Enter PDB IDs: ")
str_pdb = PDB_file.read()

params = {
'from':'PDB_ID',
'to':'ACC',
'format':'tab',
'query': str_pdb
}

data = urllib.urlencode(params)

request = urllib2.Request(url, data)

response = urllib2.urlopen(request)
page = response.read(200000)  #page is a str, to check: type(page)

#Defining path to put output files
out_path = "output/step1"


#print page (PDB ACC table)
file1 = open(os.path.join(out_path,'pdb_acc_str_of_validation_set.txt'), 'w')
file1.write(page)
file1.close()

pdb_acc_list = page.split()
print len(pdb_acc_list)
del pdb_acc_list[0:2]
print len(pdb_acc_list)

acc_list=[]
for i, value in enumerate(pdb_acc_list):
    if (i % 2) != 0 :
        acc_list.append(value)
        
print acc_list
print "Number of ACC in acc_list: ", len(acc_list)

file2 = open(os.path.join(out_path,'acc_list_of_validation_set.txt'), 'w')
file2.write(str(acc_list))
file2.close()

acc_list_str = ' '.join(acc_list)
file3 = open(os.path.join(out_path,'acc_str_of_validation_set.txt'), 'w')
file3.write(acc_list_str)
file3.close()

uni_acc_list = uniqify_list(acc_list)
print "Number of unique ACC: ", len(uni_acc_list)

uni_acc_list_str = ' '.join(uni_acc_list)
file4 = open(os.path.join(out_path,'uni_acc_str_of_validation_set.txt'), 'w')
file4.write(uni_acc_list_str)
file4.close()


