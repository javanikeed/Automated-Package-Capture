import sys

filename = sys.argv[1]

file = open(filename, "r")
appended = open("ARL_demo.txt", "w")
command = "    custom-config{\n\tcustom-config-id service: UserDefined\n\tcustom-command UserDefined\n\tconfig{\n\tcmdup=('tcpdump -i eth0 -n -w /tmp/n1.pcap',)\n\t}\n }\n"
i =0
for line in file:
    appended.write(line)
    print(i)
    if "interface-peer" in line:
        i+=1
        print(i)
        break
    else:
        appended.write(command)
    
    
file.close()
        

