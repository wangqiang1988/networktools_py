import socket

device="""172.16.255.1
172.16.255.2
172.16.255.3
172.16.255.4
172.16.255.5
172.16.255.6
172.16.255.7
172.16.255.8
172.16.255.9
172.16.255.10

"""
devicelist = device.splitlines()

def check_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(3)  # 设置超时时间
            s.connect((host, port))
        print(f"Port {port} is open on {host}")
    except (socket.timeout, ConnectionRefusedError):
        print(f"Port {port} is closed on {host}")

if __name__ == "__main__":
    port = 22  # SSH port
    for host in devicelist:
        check_port(host, port)
