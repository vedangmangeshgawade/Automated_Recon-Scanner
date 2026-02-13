from recon.dns_scan import dns_lookup
from recon.tech_detect import detect_technology
from scanner.headers import check_headers
from scanner.port_scan import port_scan
from scanner.xss import test_xss
from scanner.sqli import test_sqli
from report.report import generate_report

def main():
    target = input("Enter domain (example.com): ")

    print("\n[+] Running Recon Phase...")
    dns_info = dns_lookup(target)
    tech_info = detect_technology(target)

    print("\n[+] Running Security Checks...")
    header_info = check_headers(target)
    ports = port_scan(target)
    xss_result = test_xss(target)
    sqli_result = test_sqli(target)

    print("\n[+] Generating Report...")
    generate_report(target, dns_info, tech_info, header_info, ports, xss_result, sqli_result)

    print("\n✔ Scan complete. Report saved as report.txt")

if __name__ == "__main__":
    main()
