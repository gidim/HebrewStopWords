from collections import defaultdict
import os
import string
import xml.etree.ElementTree
import operator
import re
import sys

__author__ = 'Gideon Mendels'

xml_path = sys.argv[1]


words = defaultdict(int)


def parse_file(file_path):
    e = xml.etree.ElementTree.parse(xml_path+"/"+file_path).getroot()
    for token in e.iter('token'):
        token = token.attrib['surface'].strip(string.punctuation)
        if(token and not re.search('[a-zA-Z|0-9]', token)):
            words[token] += 1



if __name__ == '__main__':

    #iterate over xml files and parse each one
    for i in os.listdir(xml_path):
        if i.endswith(".xml"):
            parse_file(i)
            continue
        else:
            continue


    #sort the dictionary by value
    sorted_x = sorted(words.items(), key=operator.itemgetter(1),reverse=True)
    for i in range(500):
        print(sorted_x[i][0])

