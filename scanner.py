import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

def is_port_open(host: str, port: int, timeout: float = 1.0) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return s.connect_ex((host, port)) == 0

def scan_range_threaded(host: str, start_port: int, end_port: int, timeout: float = 1.0, workers: int = 100) -> list[int]:
    ports = range(start_port, end_port + 1)
    open_ports: list[int] = []

    # ThreadPoolExecutor limits threads to avoid overwhelming the PC/network
    with ThreadPoolExecutor(max_workers=workers) as executor:
        future_to_port = {
            executor.submit(is_port_open, host, port, timeout): port
            for port in ports
        }

        # as_completed yields futures as soon as they finish
        for future in as_completed(future_to_port):
            port = future_to_port[future]
            try:
                if future.result():
                    open_ports.append(port)
            except Exception:
                # Ignore unexpected errors for one port
                pass

    return sorted(open_ports)