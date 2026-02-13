import tkinter as tk
from tkinter import messagebox
from recon.dns_scan import dns_lookup
from recon.tech_detect import detect_technology
from scanner.headers import check_headers
from scanner.port_scan import port_scan
from scanner.xss import test_xss
from scanner.sqli import test_sqli
from report.report import generate_report

def run_scan():
    target = entry.get()

    if not target:
        messagebox.showerror("Error", "Please enter a domain")
        return

    status_label.config(text="Scanning... Please wait")

    dns_info = dns_lookup(target)
    tech_info = detect_technology(target)
    header_info = check_headers(target)
    ports = port_scan(target)
    xss_result = test_xss(target)
    sqli_result = test_sqli(target)

    generate_report(target, dns_info, tech_info, header_info, ports, xss_result, sqli_result)

    status_label.config(text="Scan complete! Report saved.")
    messagebox.showinfo("Done", "Scan finished!\nCheck report.txt")

# Window
window = tk.Tk()
window.title("Cyber Recon Scanner")
window.geometry("400x200")

title = tk.Label(window, text="Automated Recon Scanner", font=("Arial", 14))
title.pack(pady=10)

entry = tk.Entry(window, width=30)
entry.pack(pady=5)
entry.insert(0, "example.com")

scan_button = tk.Button(window, text="Run Scan", command=run_scan)
scan_button.pack(pady=10)

status_label = tk.Label(window, text="")
status_label.pack()

window.mainloop()
