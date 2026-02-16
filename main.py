import argparse
from concurrent.futures import ThreadPoolExecutor
from portfinder.scanner import scan_port
from portfinder.banner import grab_banner
from portfinder.services import COMMON_SERVICES
from portfinder.reporter import save_json

def main():
    parser = argparse.ArgumentParser(description="PortFinder-X")
    parser.add_argument("target", help="Target IP or hostname")
    parser.add_argument("--start", type=int, default=1)
    parser.add_argument("--end", type=int, default=1024)
    parser.add_argument("--threads", type=int, default=100)
    args = parser.parse_args()

    open_ports = []

    def worker(port):
        if scan_port(args.target, port):
            banner = grab_banner(args.target, port)
            service = COMMON_SERVICES.get(port, "Unknown")
            open_ports.append({
                "port": port,
                "service": service,
                "banner": banner
            })
            print(f"[+] {port} OPEN ({service})")

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        executor.map(worker, range(args.start, args.end + 1))

    save_json(open_ports, f"reports/{args.target}_scan.json")

if __name__ == "__main__":
    main()
