from pysnmp.hlapi import *

snmp_object1 = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)
snmp_object2 = ObjectIdentity('1.3.6.1.2.1.2.2.1.2')
snmp_object3 = ObjectIdentity('SNMPv2-MIB', 'sysLocation', 0)
snmp_object4 = ObjectIdentity('SNMPv2-MIB', 'sysContact', 0)

result = getCmd(SnmpEngine(),
    CommunityData('public', mpModel=0),
    UdpTransportTarget(('10.31.70.107', 161)),
    ContextData(),
    ObjectType(snmp_object1))
 #   ObjectType(snmp_object2))

result2 = nextCmd(SnmpEngine(),
    CommunityData('public', mpModel=0),
    UdpTransportTarget(('10.31.70.107', 161)),
    ContextData(),
#    ObjectType(snmp_object1))
    ObjectType(snmp_object2),
    lexicographicMode=False)

result3 = getCmd(SnmpEngine(),
    CommunityData('public', mpModel=0),
    UdpTransportTarget(('10.31.70.107', 161)),
    ContextData(),
    ObjectType(snmp_object3))
 #   ObjectType(snmp_object2))

result4 = getCmd(SnmpEngine(),
    CommunityData('public', mpModel=0),
    UdpTransportTarget(('10.31.70.107', 161)),
    ContextData(),
    ObjectType(snmp_object4))
 #   ObjectType(snmp_object2))

for r in result:
    for r2 in r[3]:
        print(r2)
#    print(r)

for r in result2:
    for r2 in r[3]:
        print(r2)

for r in result3:
    for r2 in r[3]:
        print(r2)

#for r in result4:
#    for r2 in r[3]:
#        print(r2)
#L4 = list(result4)
#print(L4)

