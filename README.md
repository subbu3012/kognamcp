# Kogna MCP Server

A Model Context Protocol (MCP) server that provides tools for interacting with Kogna's multi-agent AI avatar system.

## Installation

```bash
pip install kogna-mcp
```

## Configuration

Add this to your MCP client configuration (e.g., Cursor):

```json
{
  "mcpServers": {
    "kogna": {
      "command": "kogna-mcp"
    }
  }
}
```

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
