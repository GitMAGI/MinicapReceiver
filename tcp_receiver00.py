import socket

def tcp_receiver(remote_addr, remote_port):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    return