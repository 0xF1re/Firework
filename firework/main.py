from netfilterqueue import NetfilterQueue

banlist = {}

def print_and_accept(pkt):
    if pkt.get_payload_len() in banlist:
        pkt.drop()
    else:
        pkt.accept()

nfqueue = NetfilterQueue()
nfqueue.bind(0, print_and_accept)

print('[*] Queue binded')
print('[*] Firework started')
try:
    nfqueue.run()
except KeyboardInterrupt:
    print('[*] Stopping firework...')

nfqueue.unbind()
