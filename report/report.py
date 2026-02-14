def generate_report(domain, dns, tech, headers, ports, xss, sqli):
    with open("report.txt", "w") as f:
        f.write(f"=== Security Scan Report ===\n")
        f.write(f"Target: {domain}\n\n")

        f.write("DNS Info:\n")
        for k, v in dns.items():
            f.write(f"{k}: {v}\n")

        f.write("\nTechnology Detection:\n")
        for k, v in tech.items():
            f.write(f"{k}: {v}\n")

        f.write("\nSecurity Headers:\n")
        for k, v in headers.items():
            f.write(f"{k}: {v}\n")

        f.write(f"\nOpen Ports: {ports}\n")
        f.write(f"XSS Test: {xss}\n")
        f.write(f"SQL Injection Test: {sqli}\n")

        f.write("\n=== End of Report ===\n")
