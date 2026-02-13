import streamlit as st
from recon.dns_scan import dns_lookup
from recon.tech_detect import detect_technology
from scanner.headers import check_headers
from scanner.port_scan import port_scan
from scanner.xss import test_xss
from scanner.sqli import test_sqli
from report.report import generate_report

st.set_page_config(
    page_title="Cyber Recon Scanner",
    page_icon="🔍",
    layout="centered"
)

st.title("🔍 Automated Recon & Vulnerability Scanner")
st.write("Professional cybersecurity scanning dashboard")

target = st.text_input("Enter domain", "example.com")

if st.button("Run Scan"):
    with st.spinner("Scanning target... please wait"):

        dns_info = dns_lookup(target)
        tech_info = detect_technology(target)
        header_info = check_headers(target)
        ports = port_scan(target)
        xss_result = test_xss(target)
        sqli_result = test_sqli(target)

        generate_report(target, dns_info, tech_info, header_info, ports, xss_result, sqli_result)

    st.success("Scan Complete ✅")

    st.subheader("📡 DNS Info")
    st.json(dns_info)

    st.subheader("🧠 Technology Detection")
    st.json(tech_info)

    st.subheader("🛡 Security Headers")
    st.json(header_info)

    st.subheader("🚪 Open Ports")
    st.write(ports)

    st.subheader("⚠ Vulnerability Tests")
    st.write("XSS:", xss_result)
    st.write("SQL Injection:", sqli_result)

    st.info("Full report saved as report.txt")
