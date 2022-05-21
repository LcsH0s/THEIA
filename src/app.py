import netscan
import socket

if __name__ == '__main__':

    print('Mapping...')
    lst = netscan.map_network()

    for ip in lst:
        print(ip)
        try:
            print(socket.gethostbyaddr(ip))
        except socket.herror as e:
            pass
