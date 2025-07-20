#!/usr/bin/env python3
"""
Kogna MCP Bridge
Forwards MCP requests to the Kogna HTTP server
"""

import sys
import json
import httpx
import asyncio

BASE_URL = "https://kogna.up.railway.app/mcp"

async def main():
    """Bridge between MCP stdin/stdout and HTTP using httpx."""
    async with httpx.AsyncClient() as client:
        for line in sys.stdin:
            try:
                # Parse JSON-RPC request from stdin
                request = json.loads(line.strip())
                method = request.get("method", "")
                request_id = request.get("id")
                
                # Map MCP methods to HTTP endpoints
                if method == "initialize":
                    endpoint = f"{BASE_URL}/initialize"
                elif method == "tools/list":
                    endpoint = f"{BASE_URL}/tools/list"
                elif method == "tools/call":
                    endpoint = f"{BASE_URL}/tools/call"
                else:
                    # Unknown method
                    response = {
                        "jsonrpc": "2.0",
                        "id": request_id,
                        "error": {
                            "code": -32601,
                            "message": f"Method not found: {method}"
                        }
                    }
                    print(json.dumps(response))
                    sys.stdout.flush()
                    continue
                
                # Make HTTP request
                try:
                    response = await client.post(
                        endpoint,
                        json=request,
                        headers={"Content-Type": "application/json"},
                        timeout=30.0
                    )
                    
                    # Return the response to stdout
                    if response.status_code == 200:
                        response_data = response.json()
                        # Ensure the response has the required JSON-RPC fields
                        if "jsonrpc" not in response_data:
                            response_data["jsonrpc"] = "2.0"
                        if "id" not in response_data and request_id is not None:
                            response_data["id"] = request_id
                        
                        print(json.dumps(response_data))
                        sys.stdout.flush()
                    else:
                        # HTTP error
                        response = {
                            "jsonrpc": "2.0",
                            "id": request_id,
                            "error": {
                                "code": -1,
                                "message": f"HTTP error: {response.status_code}"
                            }
                        }
                        print(json.dumps(response))
                        sys.stdout.flush()
                        
                except httpx.TimeoutException:
                    response = {
                        "jsonrpc": "2.0",
                        "id": request_id,
                        "error": {
                            "code": -1,
                            "message": "Request timeout"
                        }
                    }
                    print(json.dumps(response))
                    sys.stdout.flush()
                except Exception as e:
                    response = {
                        "jsonrpc": "2.0",
                        "id": request_id,
                        "error": {
                            "code": -1,
                            "message": f"Request error: {str(e)}"
                        }
                    }
                    print(json.dumps(response))
                    sys.stdout.flush()
                    
            except json.JSONDecodeError:
                response = {
                    "jsonrpc": "2.0",
                    "id": None,
                    "error": {
                        "code": -32700,
                        "message": "Parse error: Invalid JSON"
                    }
                }
                print(json.dumps(response))
                sys.stdout.flush()
            except Exception as e:
                response = {
                    "jsonrpc": "2.0",
                    "id": request.get("id") if 'request' in locals() else None,
                    "error": {
                        "code": -1,
                        "message": f"Internal error: {str(e)}"
                    }
                }
                print(json.dumps(response))
                sys.stdout.flush()

if __name__ == "__main__":
    asyncio.run(main()) 