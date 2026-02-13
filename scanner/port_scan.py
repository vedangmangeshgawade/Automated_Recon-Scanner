import socket

def port_scan(domain):
    ports = [21, 22, 80, 443]
    open_ports = []

    for port in ports:
        sock = socket.socket()
        sock.settimeout(1)

        try:
            if sock.connect_ex((domain, port)) == 0:
                open_ports.append(port)
        except:
            pass

        sock.close()

    return open_ports
