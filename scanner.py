import socket

def port_scanner(target, ports):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

target = '127.0.0.1'
ports = range(1, 1025)
open_ports = port_scanner(target, ports)
print(f"Open ports: {open_ports}")
