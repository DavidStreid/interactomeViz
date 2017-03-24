import os
import sys
import re
import json
import requests

filename = 'HI-I-05.tsv'

with open(filename,'r') as i:
    lines = i.readlines()
    data = lines[1:]            # Remove header - ['Entrez Gene IDA', 'Symbol A', 'Entrez Gene IDB', 'Symbol B\n']
    count = 1
    if(data):                   # If file contains non-header information
        linkNumDic = {}         # Keeps track of the number of links each node has
        nodeDic = {}            # Keeps track of nodes
        idToEntrezID = {}       # Mapping of id to entrezID
        links = []              # links
        idCount = 1             # id count for graph
        numNodes = 100



        # Get Nodes
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

            if(idCount < numNodes):
                # Add node if it doesn't exist
                if entrezID_A not in nodeDic:
                    nodeDic[entrezID_A] = json.dumps({"id": str(idCount), "label": entrezID_A}, sort_keys=False)
                    idToEntrezID[entrezID_A] = str(idCount)
                    idCount += 1

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

#export var nodes = [{
#     id: 'start',
#     label: 'start'
#   }, {
#     id: '1',
#     label: 'Query ThreatConnect',
#     rank: 'first'
#   }, {
#     id: '2',
#     label: 'Query XForce',
#     rank: 'first'
#   }, {
#     id: '3',
#     label: 'Format Results'
#   }, {
#     id: '4',
#     label: 'Search Splunk'
#   }, {
#     id: '5',
#     label: 'Block LDAP'
#   }, {
#     id: '6',
#     label: 'Email Results'
#   }];

# export var links = [{
#     source: 'start',
#     target: '1'
#   }, {
#     source: 'start',
#     target: '2'
#   }, {
#     source: '1',
#     target: '3'
#   }, {
#     source: '2',
#     target: '4'
#   }, {
#     source: '2',
#     target: '6'
#   }, {
#     source: '3',
#     target: '5'
#   }];