from netfilterqueue import NetfilterQueue

banlist = {}

def print_and_accept(pkt):
    if pkt.get_payload_len() in banlist:
        pkt.drop()
    else:
        pkt.accept()

nfqueue = NetfilterQueue()
nfqueue.bind(0, print_and_accept)
try:
    print('[*] Queue binded')
    print('[*] Firework started')
    nfqueue.run()
except KeyboardInterrupt:
    print('[*] Queue unbinded')

nfqueue.unbind()
