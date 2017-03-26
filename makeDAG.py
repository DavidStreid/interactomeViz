import os
import sys
import re
import json
import requests

'''
INPUT:
    Entrez Gene IDA Symbol A    Entrez Gene IDB Symbol B
    60  ACTB    60  ACTB
    71  ACTG1   60  ACTB
    71  ACTG1   71  ACTG1
    95  ACY1    95  ACY1

OUTPUT:
    export var nodes = [{id: '#',label: 'entrezID'}, ...];
    export var links = [{source: '#', target: '#'}, ...];
'''

if(len(sys.argv) < 3):
    print "ERROR: Specify a file and min number of links per node"
    sys.exit()

filename = sys.argv[1]  # Data containing interactome data
minLinks = int(sys.argv[2])  # Defines the number of links each node should have

with open(filename,'r') as i:
    lines = i.readlines()
    data = lines[1:]            # Remove header - ['Entrez Gene IDA', 'Symbol A', 'Entrez Gene IDB', 'Symbol B\n']
    if(data):                   # If file contains non-header information
        linkNumDic = {}         # Keeps track of the number of links each node has
        nodeDic = {}            # Keeps track of nodes
        idToEntrezID = {}       # Mapping of id to entrezID
        links = []              # links
        idCount = 1             # id count for graph
        count = 1

        # Get Number of links in nodes
        for line in data:
            lineSep = line.split('\t')  # ['541468', 'LOC541468', '164127', 'FLJ35728\n']
            entrezID_A = lineSep[0]
            symbol_A = lineSep[1]
            entrezID_B = lineSep[2]
            symbol_B = lineSep[3]

            if entrezID_A not in linkNumDic:
                linkNumDic[entrezID_A] = 1
            else:
                linkNumDic[entrezID_A] += 1

        # Get Node information for genes with min number of links
        for line in data:
            lineSep = line.split('\t')  # ['541468', 'LOC541468', '164127', 'FLJ35728\n']
            entrezID_A = lineSep[0]
            symbol_A = lineSep[1]
            entrezID_B = lineSep[2]
            symbol_B = lineSep[3]

            if(linkNumDic[entrezID_A] > minLinks):
                # Add node if it doesn't exist
                if entrezID_A not in nodeDic:
                    nodeDic[entrezID_A] = json.dumps({"id": str(idCount), "label": symbol_A}, sort_keys=False)
                    idToEntrezID[entrezID_A] = str(idCount)
                    idCount += 1

        # Get links for nodes with min number of links
        for line in data: 
            lineSep = line.split('\t')  # ['541468', 'LOC541468', '164127', 'FLJ35728\n']
            entrezID_A = lineSep[0]
            symbol_A = lineSep[1]
            entrezID_B = lineSep[2]
            symbol_B = lineSep[3]

            if((entrezID_A in nodeDic) and (entrezID_B in nodeDic)):
                # Ignore nodes to each other
                if(entrezID_A != entrezID_B):
                    # Add link
                    links.append(json.dumps({"source": idToEntrezID[entrezID_A], "target": idToEntrezID[entrezID_B]}, sort_keys=False))      

    print "Nodes: " + str(len(nodeDic.keys()))
    print "Links: " + str(len(links))
    nodeFile = "node.txt"
    linkFile = "links.txt"

    dataFile = "/Users/Bike_Thoughts/Documents/Ninja/angular_webpack/src/app/dataVizComponent/interactomeComponent/model/interactomeData.ts"

    # target = open(nodeFile, 'w')
    target = open(dataFile, 'w')
    target.write('export var nodes = [\n')
    for  node in nodeDic.values():
        target.write(node + ',')
    target.write('\n]\n')

    # target = open(linkFile, 'w')
    target.write('export var links = [\n')
    for link in links:
        target.write(link + ',')
    target.write('\n]')