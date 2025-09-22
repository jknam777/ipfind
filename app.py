from flask import Flask, jsonify, render_template_string
import requests, socket

app = Flask(__name__)

INDEX = """<!doctype html>
<html lang="ko"><meta charset="utf-8">
<title>Render Flask Starter</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<body style="font-family:system-ui,Segoe UI,Roboto,Malgun Gothic,sans-serif;margin:20px">
<h1>Render Flask Starter</h1>
<p>/, /ip, /health 엔드포인트가 준비되어 있습니다.</p>
<ul>
  <li><a href="/ip">/ip</a></li>
  <li><a href="/health">/health</a></li>
</ul>
</body></html>"""


def get_local_ip():
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8",80))
        ip=s.getsockname()[0]; s.close(); return ip
    except Exception:
        return "127.0.0.1"

@app.get("/")
def index():
    return render_template_string(INDEX)

@app.get("/ip")
def ip():
    local = get_local_ip()
    external = None
    errors = []
    providers = [
        ("ipify-json","https://api.ipify.org?format=json","json","ip"),
        ("aws-checkip","https://checkip.amazonaws.com","text",None),
        ("ifconfig.me","https://ifconfig.me/ip","text",None)
    ]
    for name,url,kind,key in providers:
        try:
            r = requests.get(url, timeout=6, headers={"User-Agent":"RenderFlaskStarter/1.0"})
            r.raise_for_status()
            external = (r.json().get(key) if kind=="json" else (r.text or "").strip())
            if external: break
        except Exception as e:
            errors.append({ "provider": name, "error": str(e) })
    return jsonify({ "local": local, "external": external or "unavailable", "errors": errors })

@app.get("/health")
def health():
    return jsonify({"ok": True})

if __name__ == "__main__":
    # For local testing. Render will use gunicorn via Procfile.
    app.run(host="0.0.0.0", port=5000, debug=False)
