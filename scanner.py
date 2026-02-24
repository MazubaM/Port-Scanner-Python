import socket

def is_port_open(host: str, port: int, timeout: float = 1.0) -> bool:
    """
    Tries to open a TCP connection to (host, port).
    Returns True if connection succeeds, otherwise False.
    """
    # Create a TCP socket using IPv4
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Timeout stops it from waiting too long
        s.settimeout(timeout)

        # connect_ex returns 0 on success, else an error code
        return s.connect_ex((host, port)) == 0


if __name__ == "__main__":
    host = "127.0.0.1"
    port = 80

    if is_port_open(host, port):
        print(f"{host}:{port} is OPEN")
    else:
        print(f"{host}:{port} is CLOSED")