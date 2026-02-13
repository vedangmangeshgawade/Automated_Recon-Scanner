import requests

def check_headers(domain):
    try:
        r = requests.get(f"http://{domain}", timeout=5)
        headers = r.headers

        security_headers = [
            "X-Frame-Options",
            "X-XSS-Protection",
            "Content-Security-Policy",
            "Strict-Transport-Security"
        ]

        result = {}
        for h in security_headers:
            result[h] = headers.get(h, "Missing")

        return result
    except:
        return {"Error": "Header check failed"}
