import os
import re
import urllib.parse
from fastapi import FastAPI, Request, Response
from fastapi.responses import RedirectResponse, HTMLResponse
import uvicorn
import requests
from requests_ntlm import HttpNtlmAuth

BC_HOST = "192.168.0.39"
BC_PORT = 8080
BC_BASE = f"http://{BC_HOST}:{BC_PORT}"
BC_USER = r"npcsolutions\administrator"
BC_PASS = "ig2tq:up8#"

app = FastAPI(title="Business Central Gateway")

backend_session = requests.Session()
backend_session.auth = HttpNtlmAuth(BC_USER, BC_PASS)

try:
    print(f"[*] Authenticating with Business Central at {BC_BASE}/BC250/ ...")
    r = backend_session.get(f"{BC_BASE}/BC250/", timeout=10)
    print(f"[+] Initial Auth Status: {r.status_code}, Cookies: {list(backend_session.cookies.keys())}")
except Exception as e:
    print(f"[-] Initial Auth Warning: {e}")

@app.get("/")
async def root():
    return RedirectResponse(url="/BC250/")

@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD", "PATCH"])
async def proxy_all(request: Request, path: str):
    target_url = f"{BC_BASE}/{path}"
    if request.url.query:
        target_url += f"?{request.url.query}"

    body = await request.body()

    headers = {}
    for k, v in request.headers.items():
        if k.lower() not in ["host", "content-length", "authorization"]:
            headers[k] = v
    headers["Host"] = f"{BC_HOST}:{BC_PORT}"

    try:
        resp = backend_session.request(
            method=request.method,
            url=target_url,
            headers=headers,
            data=body,
            allow_redirects=False,
            timeout=60
        )

        if resp.status_code == 401:
            print("[*] Session 401 received, refreshing NTLM authentication...")
            backend_session.auth = HttpNtlmAuth(BC_USER, BC_PASS)
            backend_session.get(f"{BC_BASE}/BC250/", timeout=10)
            resp = backend_session.request(
                method=request.method,
                url=target_url,
                headers=headers,
                data=body,
                allow_redirects=False,
                timeout=60
            )

        excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection", "www-authenticate"]
        out_headers = {k: v for k, v in resp.headers.items() if k.lower() not in excluded_headers}

        if "location" in out_headers:
            loc = out_headers["location"]
            loc = loc.replace(f"http://{BC_HOST}:{BC_PORT}", "")
            loc = loc.replace(f"https://{BC_HOST}:{BC_PORT}", "")
            out_headers["location"] = loc

        return Response(
            content=resp.content,
            status_code=resp.status_code,
            headers=out_headers,
            media_type=resp.headers.get("content-type")
        )
    except Exception as e:
        print(f"[-] Proxy error for {target_url}: {e}")
        return HTMLResponse(
            content=f"""
            <html>
                <body style="background:#0f172a;color:#f8fafc;font-family:sans-serif;text-align:center;padding:50px;">
                    <h2>Business Central Gateway Error</h2>
                    <p style="color:#ef4444;">{e}</p>
                    <a href="/BC250/" style="color:#38bdf8;text-decoration:none;">Retry Connection</a>
                </body>
            </html>
            """,
            status_code=502
        )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8096, log_level="warning")
