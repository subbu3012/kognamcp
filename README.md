---
title: Kogna MCP Server
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: docker
pinned: false
license: mit
---

# Kogna MCP Server

A Model Context Protocol (MCP) server that provides tools for interacting with Kogna's multi-agent AI avatar system.

## Installation

### Install pipx (if you don't have it)

```bash
# macOS
brew install pipx

# Other systems
pip install pipx

# Add pipx to your PATH (if not already done)
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### Install kognamcp

```bash
pipx install kognamcp
```

## Testing the Installation

### 1. Test the command is available

```bash
kognamcp --help
```

You should see:
```
usage: kognamcp [-h]

Kogna MCP Bridge - Forwards MCP requests to the Kogna HTTP server

options:
  -h, --help  show this help message and exit

Examples:
  # Run as MCP server (reads from stdin, writes to stdout)
  kognamcp
  
  # Test with echo (for development)
  echo '{"jsonrpc": "2.0", "method": "initialize", "id": 1}' | kognamcp
```

### 2. Test the MCP bridge connection

```bash
echo '{"jsonrpc": "2.0", "method": "initialize", "id": 1}' | kognamcp
```

You should get a response like:
```json
{"jsonrpc": "2.0", "id": 1, "result": {"protocolVersion": "2024-11-05", "capabilities": {"tools": {}}, "serverInfo": {"name": "kognamcp-server", "version": "1.0.0"}}}
```

## Configuration

### Find the kognamcp path

First, find the full path to the kognamcp command:

```bash
which kognamcp
```

This will output something like `/Users/username/.local/bin/kognamcp`

### Configure your MCP client

Add this configuration to your MCP client:

```json
{
  "mcpServers": {
    "kognamcp": {
      "command": "FULL_PATH_FROM_WHICH_COMMAND"
    }
  }
}
```

**Replace `FULL_PATH_FROM_WHICH_COMMAND` with the output from `which kognamcp`**

For example, if `which kognamcp` returns `/Users/john/.local/bin/kognamcp`, your config should be:

```json
{
  "mcpServers": {
    "kognamcp": {
      "command": "/Users/john/.local/bin/kognamcp"
    }
  }
}
```

## Troubleshooting

### "Command not found: kognamcp"

1. Make sure the installation completed successfully:
   ```bash
   pipx list | grep kognamcp
   ```

2. Add pipx to your PATH:
   ```bash
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
   source ~/.zshrc
   ```

3. Restart your terminal/IDE

### "spawn kognamcp ENOENT" or similar errors

This happens when your MCP client can't find the `kognamcp` command. The solution is to use the full path:

1. Find the full path:
   ```bash
   which kognamcp
   ```

2. Copy the exact output and use it in your MCP configuration

3. Restart your MCP client

### Connection errors

The bridge connects to `https://kogna.up.railway.app/mcp`. Make sure you have internet access.

## Available Tools

- `start_kogna_conversation` - Start a new conversation with Kogna avatars
- `send_kogna_message` - Send a message to the current conversation
- `list_kogna_avatars` - List available avatars and their specialties
- `list_kogna_rooms` - List available rooms and their descriptions
- `switch_kogna_avatar` - Switch to a different avatar
- `switch_kogna_room` - Switch to a different room
- `get_kogna_conversation_history` - Get conversation history
- `get_kogna_system_info` - Get system information

## Usage

Once configured, you can use Kogna through your MCP client:

- "Start a Kogna conversation"
- "List the available Kogna avatars"
- "Switch to the business room"
- "Ask the strategist avatar about market positioning"

## Requirements

- Python 3.8+
- Internet connection (connects to Kogna backend)

## License

MIT License
