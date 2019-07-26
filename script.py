#!/usr/bin/env python

"""script.py: Inserts custom router configuration command to any .imn file in order to automate package capture then later safe to filesystem on its own."""

__author__  = "Jazmin I. Paz"
__version__ = "1.0.3"
__maintainer__ = "Jazmin I. Paz"
__email__ = "jipaz@miners.utep.edu"
__status__ = "In Progress/26 July 2019"



import sys
file = open(sys.argv[1], "r")
modif = open(sys.argv[2], "w")
node_num=0
_command = "    custom-config {\n\tcustom-config-id service:UserDefined\n\n\tcustom-command UserDefined\n\tconfig {\n\tcmdup=('tcpdump -i eth0 -n -w /tmp/n"
command_ = ".pcap', )\n\t}\n    }\n}\n"
modelPCservices = "    services {DefaultRoute UserDefined}\n}\n"
routerServices = "    services {zebra 0SPFv2 0SPFv3 vtysh IPForward UserDefined}\n}\n"
_c2 = ", 'tcpdump -i eth0 -n -w /tmp/n"
c2_ = ".pcap' , )"
prevLine = False
routerNode = False
modelRouter = False
modelPC = False

for line in file:
    if "node" in line:
        node_num+=1 
    if "type router" in line:
        routerNode = True
    if "model router" in line:
        modelRouter = True
    if "model PC" in line:
        modelPC = True
    if "interface-peer" in line:
        prevLine = True
    if "cmdup" in line:
        index_num = line.rfind(",")
        line = line[:index_num] + _c2+str(node_num)+c2_ + "\n"
        prevLine = False
        routerNode = False
    if line.startswith("}") and prevLine and routerNode:
        if (modelPC):
            modif.write(_command+str(node_num)+command_+modelPCServices)
            modelPC = False
            modelRouter = False
        if (modelRouter)
            modif.write(_command+str(node_num)+command_+routerServices)
            modelPC = False
            modelRouter = False
        prevLine = False
        routerNode = False
    else:
        modif.write(line)
file.close() 

