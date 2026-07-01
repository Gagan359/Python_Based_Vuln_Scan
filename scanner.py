import nmap
from cve_lookup import lookup_cves


def scan_target(target):

    scanner = nmap.PortScanner()

    scanner.scan(target, arguments="-sV")

    scan_results = []

    searched = set()

    hosts = scanner.all_hosts()

    if not hosts:
        return []

    for host in hosts:

        if "tcp" not in scanner[host]:
            continue

        for port in scanner[host]["tcp"]:

            service = scanner[host]["tcp"][port]

            product = service.get("product", "")
            version = service.get("version", "")
            service_name = service.get("name", "")

            software = f"{product} {version}"

            if software not in searched:

                vulnerabilities = lookup_cves(product, version)

                searched.add(software)

            else:

                vulnerabilities = []

            service_result = {
                "host": host,
                "port": port,
                "service": service_name,
                "product": product,
                "version": version,
                "vulnerabilities": vulnerabilities
            }

            scan_results.append(service_result)

    return scan_results


if __name__ == "__main__":

    target = input("Enter Target: ")

    results = scan_target(target)

    for service in results:

        print("-" * 50)
        print(f"Host: {service['host']}")
        print(f"Port: {service['port']}")
        print(f"Service: {service['service']}")
        print(f"Product: {service['product']}")
        print(f"Version: {service['version']}")
        print(f"CVEs Found: {len(service['vulnerabilities'])}")