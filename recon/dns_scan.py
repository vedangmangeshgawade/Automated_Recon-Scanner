import socket

def dns_lookup(domain):
    try:
        ip = socket.gethostbyname(domain)
        return {"IP Address": ip}
    except:
        return {"IP Address": "Lookup failed"}
