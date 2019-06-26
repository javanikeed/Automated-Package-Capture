from core import pycore
import "github.com/vishvananda/netns"
import optparse, sys, os, datetime
#Package netns allows ultra-simple network namespace handling

session = pycore.Session(persistent=True)
node = []
node[0] = session.addobj(cls=pycore.nodes.CoreNode, name="n1")
node[1] = session.addobj(cls=pycore.nodes.CoreNode, name="n2")
node[2] = session.addobj(cls=pycore.nodes.CoreNode, name="n3")
node[3] = session.addobj(cls=pycore.nodes.CoreNode, name="n4")
node[4] = session.addobj(cls=pycore.nodes.CoreNode, name="n5")
node[5] = session.addobj(cls=pycore.nodes.CoreNode, name="n6")
node[6] = session.addobj(cls=pycore.nodes.CoreNode, name="eth1")
node[7] = session.addobj(cls=pycore.nodes.CoreNode, name="n8")
node[8] = session.addobj(cls=pycore.nodes.CoreNode, name="n9")
node[9] = session.addobj(cls=pycore.nodes.CoreNode, name="n10")

for i in range(10):
    node[i].icmd(["tcpdump", "-w", "capture.pcap", "-i", "eth0"])
session.shutdown()
