# KognaMCP Technical Documentation

## Project Overview

KognaMCP is a Model Context Protocol (MCP) client bridge that enables MCP-compatible clients to interact with the Kogna AI platform. It acts as a bridge between MCP clients and the Kogna backend API.

## Architecture

### High-Level Architecture
```
MCP Client → kognamcp bridge → Kogna Backend (Railway)
```

### Component Breakdown

#### 1. MCP Client
- Sends JSON-RPC 2.0 requests via stdin
- Expects JSON-RPC 2.0 responses via stdout
- Handles tool discovery and execution

#### 2. kognamcp Bridge
- **Location**: `kognamcp/bridge.py`
- **Purpose**: Protocol translation layer
- **Input**: JSON-RPC from MCP client
- **Output**: HTTP requests to Kogna backend
- **Response**: JSON-RPC back to MCP client

#### 3. Kogna Backend
- **URL**: `https://kogna.up.railway.app/mcp`
- **Protocol**: HTTP/JSON-RPC
- **Purpose**: Multi-agent AI avatar system
- **Data**: Firestore persistence

## Technical Implementation

### Bridge Implementation (`bridge.py`)

#### Core Functions
```python
def main():
    """Entry point for MCP bridge."""
    asyncio.run(async_main())

async def async_main():
    """Bridge between MCP stdin/stdout and HTTP using httpx."""
```

#### Request Flow
1. **Read from stdin**: Parse JSON-RPC request
2. **Map method to endpoint**:
   - `initialize` → `/mcp/initialize`
   - `tools/list` → `/mcp/tools/list`
   - `tools/call` → `/mcp/tools/call`
3. **HTTP request**: Send to Kogna backend
4. **Response processing**: Format as JSON-RPC
5. **Write to stdout**: Send response to MCP client

#### Error Handling
- **JSON parsing errors**: Return JSON-RPC parse error
- **HTTP errors**: Return JSON-RPC error with status code
- **Timeouts**: Return timeout error
- **Unknown methods**: Return method not found error

### Package Structure

#### Python Package (`kognamcp/`)
```
kognamcp/
├── __init__.py      # Package initialization
└── bridge.py        # Main bridge implementation
```

#### Distribution Files
```
kognamcp/
├── setup.py         # Package configuration
├── requirements.txt # Dependencies
├── README.md       # User documentation
├── llms-install.md # MCP marketplace docs
├── LICENSE         # MIT license
└── logo.png        # Package logo
```

### Entry Point Configuration
```python
entry_points={
    "console_scripts": [
        "kognamcp=kognamcp.bridge:main",
    ],
}
```

## MCP Protocol Implementation

### Supported Methods

#### 1. `initialize`
- **Purpose**: Handshake between MCP client and server
- **Request**: Protocol version and capabilities
- **Response**: Server info and capabilities

#### 2. `tools/list`
- **Purpose**: Discover available tools
- **Request**: None required
- **Response**: Array of tool definitions

#### 3. `tools/call`
- **Purpose**: Execute a tool
- **Request**: Tool name and parameters
- **Response**: Tool execution result

### Tool Definitions

The bridge exposes 8 Kogna tools:

1. **`start_kogna_conversation`** - Start new conversation
2. **`send_kogna_message`** - Send message to conversation
3. **`list_kogna_avatars`** - List available avatars
4. **`list_kogna_rooms`** - List available rooms
5. **`switch_kogna_avatar`** - Switch avatar in conversation
6. **`switch_kogna_room`** - Switch room in conversation
7. **`get_kogna_conversation_history`** - Get conversation history
8. **`get_kogna_system_info`** - Get system information

## Development Workflow

### Local Development

#### 1. Setup Environment
```bash
cd kognamcp
pip install -r requirements.txt
pip install -e .
```

#### 2. Testing
```bash
# Test bridge directly
echo '{"jsonrpc": "2.0", "method": "initialize", "id": 1}' | kognamcp

# Test package installation
pipx install kognamcp
kognamcp --help
```

#### 3. Building
```bash
# Install build tools
pipx install build twine

# Build package
pyproject-build

# Check package
twine check dist/*
```

### Publishing Process

#### 1. Version Update
Edit `setup.py` and `kognamcp/__init__.py`:
```python
version="1.0.7"  # Increment version
__version__ = "1.0.7"
```

#### 2. Build Package
```bash
pyproject-build
```

#### 3. Upload to PyPI
```bash
twine upload dist/*
```

#### 4. Verify Upload
```bash
pipx install kognamcp --force
```

## Configuration Management

### PyPI Credentials
Create `~/.pypirc`:
```ini
[pypi]
username = __token__
password = pypi-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### MCP Client Configuration
For any MCP client, add to config:
```json
{
  "mcpServers": {
    "kognamcp": {
      "command": "FULL_PATH_FROM_WHICH_COMMAND"
    }
  }
}
```

## Dependencies

### Runtime Dependencies
- `requests>=2.25.0` - HTTP client library 