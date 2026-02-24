import argparse
from scanner import scan_range

def parse_ports(text: str) -> tuple[int, int]:
    parts = text.split("-")
    if len(parts) != 2:
        raise argparse.ArgumentTypeError("Use START-END, e.g. 1-1024")

    start = int(parts[0])
    end = int(parts[1])

    if start < 1 or end > 65535 or start > end:
        raise argparse.ArgumentTypeError("Ports must be 1-65535 and START <= END")

    return start, end

def main() -> None:
    parser = argparse.ArgumentParser(description="Simple TCP port scanner (authorized use only).")
    parser.add_argument("host", help="Target host, e.g. 127.0.0.1")
    parser.add_argument("--ports", type=parse_ports, default="1-1024", help="Port range START-END (default 1-1024)")
    parser.add_argument("--timeout", type=float, default=0.5, help="Timeout in seconds (default 0.5)")
    args = parser.parse_args()

    start_port, end_port = args.ports

    open_ports = scan_range(args.host, start_port, end_port, args.timeout)

    if open_ports:
        for p in open_ports:
            print(f"{args.host}:{p} OPEN")
    else:
        print(f"No open ports found on {args.host} in range {start_port}-{end_port}")

if __name__ == "__main__":
    main()