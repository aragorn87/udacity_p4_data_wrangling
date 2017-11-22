#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')


def key_type(element, keys):
    if element.tag == "tag":
        # YOUR CODE HERE
        string=element.attrib['k']
        if re.search(lower, string):
            keys['lower']+=1
        else:
            if re.search(lower_colon, string):
                keys['lower_colon']+=1
            else:
                if re.search(problemchars, string):
                    keys['problemchars']+=1
                else:
                    keys['other']+=1
    return keys



def process_map(filename):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    for _, element in ET.iterparse(filename):
        keys = key_type(element, keys)

    return keys



def test():
    # You can use another testfile 'map.osm' to look at your solution
    # Note that the assertion below will be incorrect then.
    # Note as well that the test function here is only used in the Test Run;
    # when you submit, your code will be checked against a different dataset.
    keys = process_map('sample.osm')
    pprint.pprint(keys)


if __name__ == "__main__":
    test()