import socket

def grab_banner(target: str, port: int):
    try:
        sock = socket.socket()
        sock.settimeout(2)
        sock.connect((target, port))
        sock.send(b"HEAD / HTTP/1.1\r\nHost: example.com\r\n\r\n")
        banner = sock.recv(1024)
        sock.close()
        return banner.decode(errors="ignore").strip()
    except:
        return None
