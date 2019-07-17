#!/usr/bin/env python

"""CORE_script1.py: Inserts custom router configuration command to any .imn file in order to automate package capture then later safe to filesystem on its own."""

__author__  = "Jazmin I. Paz"
__version__ = "1.0.1"
__maintainer__ = "Jazmin I. Paz"
__email__ = "jipaz@miners.utep.edu"
__status__ = "In Progress"



import sys

file = open(sys.argv[1], "r")
modif = open("ARL_demo.imn", "w")
node_num=1
_command = "    custom-config{\n\tcustom-config-id service: UserDefined\n\tcustom-command UserDefined\n\tconfig{\n\tcmdup=('tcpdump -i eth0 -n -w /tmp/n"
command_ = ".pcap',)\n\t}\n }\n"
#prevLine = " "
prevLine = False;


for line in file:
    if "interface-peer" in line:
        prevLine = True
    if line.startswith("}") and prevLine:
        modif.write(_command+str(node_num)+command_)
        node_num+=1
        prevLine = False
    else:
        modif.write(line)
file.close() 

