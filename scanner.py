import socket

def is_port_open(host: str, port: int, timeout: float = 1.0) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return s.connect_ex((host, port)) == 0

def scan_range(host: str, start_port: int, end_port: int, timeout: float = 1.0) -> list[int]:
    open_ports: list[int] = []

    for port in range(start_port, end_port + 1):
        if is_port_open(host, port, timeout):
            open_ports.append(port)

    return open_ports

if __name__ == "__main__":
    host = "127.0.0.1"
    start_port = 1
    end_port = 200
    timeout = 0.5

    open_ports = scan_range(host, start_port, end_port, timeout)

    for p in open_ports:
        print(f"{host}:{p} OPEN")

    if not open_ports:
        print("No open ports found.")