import requests

def test_xss(domain):
    payload = "<script>alert(1)</script>"

    try:
        r = requests.get(f"http://{domain}/?q={payload}", timeout=5)

        if payload in r.text:
            return "Possible XSS vulnerability detected"
        else:
            return "No obvious XSS reflection"
    except:
        return "XSS test failed"
