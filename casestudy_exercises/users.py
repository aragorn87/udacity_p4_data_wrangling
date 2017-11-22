#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re


def get_user(element):
    return


def process_map(filename):
    users = set()
    for event, element in ET.iterparse(filename, ("start",)):
        if 'user' in element.attrib:
            users.add(element.attrib['user'])
        pass

    return users


def test():

    users = process_map('sample.osm')
    pprint.pprint(users)
    pprint.pprint(len(users))


if __name__ == "__main__":
    test()