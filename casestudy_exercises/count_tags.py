#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
import pprint

def count_tags(filename):
        # YOUR CODE HERE
        tags={}
        for event, elem in ET.iterparse(filename):
            if elem.tag not in tags:
                tags[elem.tag]=1
            else:
                tags[elem.tag]+=1
        return tags
            


def test():

    tags = count_tags('sample.osm')
    pprint.pprint(tags)


if __name__ == "__main__":
    test()