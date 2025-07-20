# KognaMCP Development Setup Guide

## Development Environment

### 1. Clone Repository
```bash
git clone https://github.com/subbu3012/kognamcp.git
cd kognamcp
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Install in Development Mode
```bash
pip install -e .
```

### 4. Test Locally
```bash
kognamcp --help
```

## Publishing to PyPI

### 1. Install Build Tools
```bash
pipx install build twine
```

### 2. Update Version
Edit `setup.py` and `kognamcp/__init__.py`:
```python
version="1.0.7"  # Increment version
__version__ = "1.0.7"
```

### 3. Build Package
```bash
pyproject-build
```

### 4. Check Package
```bash
twine check dist/*
```

### 5. Upload to PyPI
```bash
twine upload dist/*
```

### 6. Verify Upload
```bash
pipx install kognamcp --force
```

## Project Structure
```
kognamcp/
├── kognamcp/           # Python package
│   ├── __init__.py
│   └── bridge.py       # MCP bridge implementation
├── setup.py            # Package configuration
├── requirements.txt    # Dependencies
├── README.md          # User documentation
├── llms-install.md    # MCP marketplace docs
├── LICENSE            # MIT license
└── logo.png           # Package logo
```

## Key Files
- `setup.py` - Package configuration and entry point
- `kognamcp/bridge.py` - MCP bridge to Kogna backend
- `llms-install.md` - MCP marketplace submission
- `requirements.txt` - Python dependencies

## MCP Bridge Details
- **Backend URL**: `https://kogna.up.railway.app/mcp`
- **Protocol**: JSON-RPC 2.0
- **Methods**: `initialize`, `tools/list`, `tools/call`
- **Tools**: 8 Kogna AI avatar tools

## Version History
- `1.0.0` - Initial release with MCP bridge functionality
- `1.0.4` - Fixed package structure and added help functionality
- `1.0.5` - Updated documentation with pipx instructions
- `1.0.6` - Fixed help functionality 