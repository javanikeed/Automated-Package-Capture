#!/usr/bin/env python

"""script.py: Inserts custom router configuration command to any .imn file in
order to automate package capture then later safe to filesystem on its own.

MODIFICATIONS since 18 July 2019:
1) Creates folder in /tmp where .pcap files will be stored
2) Timestamps the folder with date and time.
3) Fixes bug in numbering nodes
4) Increases dynamics/ less hardcoded
"""

__author__  = "Jazmin I. Paz"
__version__ = "1.0.4"
__maintainer__ = "Jazmin I. Paz"
__email__ = "jipaz@miners.utep.edu"
__status__ = "In Progress/26 July 2019"


import sys
import os
import time
import datetime

file = open(sys.argv[1], "r")
modif = open(sys.argv[2], "w")
ts = time.time()
timestamp = str(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H:%M:%S'))
_command = "    custom-config {\n\tcustom-config-id service:UserDefined\n\n\tcustom-command UserDefined\n\tconfig {\n\tcmdup=('tcpdump -i eth0 -n -w /tmp/"
command_ = ".pcap', )\n\t}\n    }\n"
PCservices = "    services {DefaultRoute UserDefined}\n}\n"
routerServices = "    services {zebra 0SPFv2 0SPFv3 vtysh IPForward UserDefined}\n}\n"
_c2 = ", 'tcpdump -i eth0 -n -w /tmp/"
c2_ = ".pcap' , )"
interfacePeer = False
routerNode = False
modelRouter = False
modelPC = False
folderName = os.path.splitext(sys.argv[1])[0]
folderName = str(folderName+"_"+timestamp)

newFolder = r'/tmp/'+folderName
if not os.path.exists(newFolder):
    os.makedirs(newFolder)
   
for line in file:
    if "node " in line:
        n = [int(char) for char in line if char.isdigit()]
        node_num = int(''.join(map(str,n)))
    if "type router" in line:
        routerNode = True
    if "model router" in line:
        modelRouter = True
    if "model PC" in line:
        modelPC = True
    if "interface-peer" in line:
        interfacePeer = True
    if "cmdup" in line:
        index_num = line.rfind(",")
        line = line[:index_num] + _c2+folderName+"/node_"+str(node_num)+c2_ + "\n"
        interfacePeer = False
        routerNode = False
    if line.startswith("}") and interfacePeer and routerNode:
        if (modelPC):
            modif.write(_command+folderName+"/node_"+str(node_num)+command_+modelPCServices)
            modelPC = False
            modelRouter = False
        if (modelRouter):
            modif.write(_command+folderName+"/node_"+str(node_num)+command_+routerServices)
            modelPC = False
            modelRouter = False
        interfacePeer = False
        routerNode = False
    else:
        modif.write(line)
        
file.close()
