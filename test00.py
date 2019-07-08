import tcp_receiver01 as receiver_lib

def test00():
    remote_addr = 'localhost'
    remote_port = 1717

    receiver_lib.tcp_receiver(remote_addr, remote_port)

    return