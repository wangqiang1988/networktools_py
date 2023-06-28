byte="""Last clearing of counters: Never
Last 300 seconds input:  2220 packets/sec 1517875 bytes/sec 0%
Last 300 seconds output:  2240 packets/sec 2252620 bytes/sec 0%
Last clearing of counters: Never
Last 300 seconds input:  2260 packets/sec 953684 bytes/sec 0%
Last 300 seconds output:  2821 packets/sec 2226602 bytes/sec 0%
Last clearing of counters: Never
Last 300 seconds input:  391 packets/sec 232645 bytes/sec 0%
Last 300 seconds output:  173 packets/sec 78020 bytes/sec 0%
Last clearing of counters: Never
Last 300 seconds input:  23635 packets/sec 10381287 bytes/sec 0%
Last 300 seconds output:  25272 packets/sec 12691425 bytes/sec 0%"""
def bytes2human(n):
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value,s)
    return '%sB' % n
p = 0
bytelist = byte.splitlines()
for i  in bytelist:
    if 'bytes' in i:
        print(bytes2human(int(i.split(' ')[-3])))
        p+= int(i.split(' ')[-3])
print(bytes2human(p))

