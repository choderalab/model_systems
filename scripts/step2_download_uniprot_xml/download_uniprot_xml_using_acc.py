# This script must import xml files corresponding to a list of accession numbers
# I took Sonya's uniprot_download_xml.py as an example when I am writing this script
# list of accession numbers is written as a string in a separate file

# run this from model_systems directory as:

# usage:    python scripts/step2_download_uniprot_xml/download_uniprot_xml_using_acc.py input_path/input_file
#           python scripts/step2_download_uniprot_xml/download_uniprot_xml_using_acc.py input/step2/uni_acc_str_of_validation_set.txt
#           OR for testing
#           python scripts/step2_download_uniprot_xml/download_uniprot_xml_using_acc.py input/step2/acc_short.txt
#

import urllib, urllib2
from sys import argv
import os

#unpacking and importing input string
script, filename = argv
ACCs_file = open(filename)
ACCs_str= ACCs_file.read()
ACCs_list = ACCs_str.split()  #convert string to a list

print ACCs_list

#Defining path to put output files
out_path = "output/step2"
input_path_of_next_step = "input/step3"

#define acc (Uniprot accession number)
#iterate over uniprot accession numbers(acc)
for acc in ACCs_list:
    url = 'http://www.uniprot.org/uniprot/'
#   response = urllib2.urlopen(url + "%s" %acc + ".xml")
    request = urllib2.Request(url + "%s" %acc + ".xml" )
    response = urllib2.urlopen(request)

#   xml_page=response.read().decode('utf-8') #this is probably not necessary since I am not using Python 3
    xml_page = response.read()

    xml_page = xml_page.replace('<uniprot xmlns="http://uniprot.org/uniprot" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://uniprot.org/uniprot http://www.uniprot.org/support/docs/uniprot.xsd">','<uniprot>', 1)

    file = open(os.path.join(out_path, "%s.xml" %acc), "w")
    file.write(xml_page)
    file.close()

    #also saving the same output file to input path of the next script (step3)
    file = open(os.path.join(input_path_of_next_step, "%s.xml" %acc), "w")
    file.write(xml_page)
    file.close()


    # I wanted to create symlinks to output files in step3's input file but somehow broken link is produced
    # src = os.path.join(out_path, "%s.xml" %acc)
    # dst = os.path.join(input_path_of_next_step, "%s.xml" %acc)
    # os.symlink(src, dst)

