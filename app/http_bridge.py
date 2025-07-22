import os
from fastapi import FastAPI, Request, Response
import httpx
import uvicorn

app = FastAPI()

# Get the port from the environment variable (default to 8080 for local dev)
PORT = int(os.environ.get("PORT", 8080))

# Kogna backend MCP endpoint
KOGNA_BACKEND_URL = "https://kogna.up.railway.app/mcp"

METHOD_TO_ENDPOINT = {
    "initialize": f"{KOGNA_BACKEND_URL}/initialize",
    "tools/list": f"{KOGNA_BACKEND_URL}/tools/list",
    "tools/call": f"{KOGNA_BACKEND_URL}/tools/call",
}

@app.post("/mcp")
async def mcp_proxy(request: Request):
    body = await request.body()
    try:
        json_body = await request.json()
        method = json_body.get("method")
        endpoint = METHOD_TO_ENDPOINT.get(method)
        if not endpoint:
            return Response(content='{"error": "Unknown method"}', status_code=400, media_type="application/json")
    except Exception:
        return Response(content='{"error": "Invalid JSON"}', status_code=400, media_type="application/json")

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(endpoint, content=body, headers={"Content-Type": "application/json"})
            return Response(content=response.content, status_code=response.status_code, media_type="application/json")
        except httpx.RequestError as e:
            return Response(content=f'{{"error": "Upstream request error: {str(e)}"}}', status_code=502, media_type="application/json")

if __name__ == "__main__":
    uvicorn.run("app.http_bridge:app", host="0.0.0.0", port=PORT, reload=False) 