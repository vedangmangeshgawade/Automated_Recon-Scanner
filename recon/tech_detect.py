import requests

def detect_technology(domain):
    try:
        r = requests.get(f"http://{domain}", timeout=5)
        server = r.headers.get("Server", "Unknown")
        powered = r.headers.get("X-Powered-By", "Unknown")

        return {
            "Server": server,
            "X-Powered-By": powered
        }
    except:
        return {"Technology": "Detection failed"}
