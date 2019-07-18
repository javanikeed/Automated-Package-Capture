#!/usr/bin/env python

"""script.py: Inserts custom router configuration command to any .imn file in order to automate package capture then later safe to filesystem on its own."""

__author__  = "Jazmin I. Paz"
__version__ = "1.0.2"
__maintainer__ = "Jazmin I. Paz"
__email__ = "jipaz@miners.utep.edu"
__status__ = "In Progress"



import sys

file = open(sys.argv[1], "r")
#modif = open("ARL_demo.imn", "w")
modif = open(sys.argv[2], "w")
node_num=0
_command = "    custom-config {\n\tcustom-config-id service:UserDefined\n\n\tcustom-command UserDefined\n\tconfig {\n\tcmdup=('tcpdump -i eth0 -n -w /tmp/n"
command_ = ".pcap', )\n\t}\n    }\n}\n"
#prevLine = " "
prevLine = False;
routerNode = False

for line in file:
    if "node" in line:
        node_num+=1 
    if "router" in line:
        routerNode = True
    if "interface-peer" in line:
        prevLine = True
    if line.startswith("}") and prevLine and routerNode:
        modif.write(_command+str(node_num)+command_)
        prevLine = False
        routerNode = False
    else:
        modif.write(line)
file.close() 

