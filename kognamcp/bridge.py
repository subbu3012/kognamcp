#!/usr/bin/env python3
"""
Kogna MCP Bridge
Forwards MCP requests to the Kogna HTTP server
"""

import sys
import json
import httpx
import asyncio
import argparse

BASE_URL = "https://kogna.up.railway.app/mcp"

def send_error_response(error_code, message, request_id=None):
    """Send a JSON-RPC error response."""
    response = {
        "jsonrpc": "2.0",
        "error": {
            "code": error_code,
            "message": message
        }
    }
    if request_id is not None:
        response["id"] = request_id
    print(json.dumps(response))
    sys.stdout.flush()

def main():
    """Entry point for the MCP bridge."""
    parser = argparse.ArgumentParser(
        description="Kogna MCP Bridge - Forwards MCP requests to the Kogna HTTP server",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run as MCP server (reads from stdin, writes to stdout)
  kognamcp
  
  # Test with echo (for development)
  echo '{"jsonrpc": "2.0", "method": "initialize", "id": 1}' | kognamcp"""
        )
    
    # Parse arguments (help flag is handled automatically)
    parser.parse_known_args()
    
    # Run the MCP bridge
    asyncio.run(async_main())

async def async_main():
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
                    # Unknown method - don't send response for notifications
                    if request_id is not None:
                        send_error_response(-32601, f"Method not found: {method}", request_id)
                    # For notifications (no id), don't send any response
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
                        
                        # Handle id field properly
                        if "id" in response_data and response_data["id"] is None:
                            # Remove null id from response (for notifications)
                            del response_data["id"]
                        elif "id" not in response_data and request_id is not None:
                            # Add id if it's missing but we have a request_id
                            response_data["id"] = request_id
                        
                        print(json.dumps(response_data))
                        sys.stdout.flush()
                    else:
                        # HTTP error
                        send_error_response(-1, f"HTTP error: {response.status_code}", request_id)
                        
                except httpx.TimeoutException:
                    send_error_response(-1, "Request timeout", request_id)
                except Exception as e:
                    send_error_response(-1, f"Request error: {str(e)}", request_id)
                    
            except json.JSONDecodeError:
                send_error_response(-32700, "Parse error: Invalid JSON")
            except Exception as e:
                # Add id only if request exists and has a valid id
                request_id_for_error = None
                if 'request' in locals() and request.get("id") is not None:
                    request_id_for_error = request.get("id")
                send_error_response(-1, f"Internal error: {str(e)}", request_id_for_error)

if __name__ == "__main__":
    main() 