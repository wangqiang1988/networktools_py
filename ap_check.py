from pysnmp.hlapi import *
import sys
from smtp import sendmail
#在下面把ap的名字写好
apall = """AP-1
AP-2
AP-3
AP-4
AP-5
AP-6
AP-7
AP-8
AP-9
AP-10
AP-11
AP-12
AP-13
AP-14
AP-15
AP-16
AP-17
AP-18
AP-19
AP-20"""
def walk(host, oid):
    aplist = []
    for (errorIndication,
         errorStatus,
         errorIndex,
         varBinds) in nextCmd(SnmpEngine(),
                              CommunityData('public'),
                              UdpTransportTarget((host, 161)),
                              ContextData(),
                              ObjectType(ObjectIdentity(oid)),
                              lookupMib=False,
                              lexicographicMode=False):

        if errorIndication:
            print(errorIndication, file=sys.stderr)
            break

        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'), file=sys.stderr)
            break

        else:
            for varBind in varBinds:
#                 print('%s = %s' % varBind)
#                 print(varBind[1])
                 aplist.append(str(varBind[1]))
#    print(aplist)
    apalllist = apall.splitlines()
#    print(apalllist)
    diff = list(set(apalllist) - set(aplist))
    if len(diff)==0:
        print("无线AP状态正常")
        sendmail('无线AP巡检','AP正常') #这里引入了sendmail脚本，可自行注销

    else:
        print('AP掉线',diff)
        sendmail('无线AP巡检',('AP掉线',diff))  #这里引入了sendmail脚本，可自行注销

#wlc的ip以及oid
walk('192.168.x.x', '1.3.6.1.4.1.14179.2.2.1.1.3')

