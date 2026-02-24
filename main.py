import argparse
from scanner import scan_range_threaded

# ... keep parse_ports unchanged ...

def main() -> None:
    parser = argparse.ArgumentParser(description="Simple TCP port scanner (authorized use only).")
    parser.add_argument("host", help="Target host, e.g. 127.0.0.1")
    parser.add_argument("--ports", type=parse_ports, default="1-1024", help="Port range START-END (default 1-1024)")
    parser.add_argument("--timeout", type=float, default=0.5, help="Timeout in seconds (default 0.5)")
    parser.add_argument("--workers", type=int, default=100, help="Thread workers (default 100)")
    args = parser.parse_args()

    start_port, end_port = args.ports

    open_ports = scan_range_threaded(args.host, start_port, end_port, args.timeout, args.workers)

    if open_ports:
        for p in open_ports:
            print(f"{args.host}:{p} OPEN")
    else:
        print(f"No open ports found on {args.host} in range {start_port}-{end_port}")

if __name__ == "__main__":
    main()