import socket
import struct
import textwrap

def main():
    print("Welcome to the Packet Sniffer")
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))
    conn.bind(('enp0s3', 0))
    print("Socket created. Waiting for packets...")


    while True:
        raw_data, addr = conn.recvfrom(65536)
        print("Packet received:", len(raw_data), "bytes")
        dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)
        print('\nEthernet Frame:')
        print('Destination: {}, Source: {}, Protocol: {}'.format(dest_mac, src_mac, eth_proto))




#Unpack Ethernet Frame
def ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
    return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[14:]
#Return properly formatted MAC address (AA:BB:CC:DD:EE:FF)
def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    return ':'.join(bytes_str).upper()

main()