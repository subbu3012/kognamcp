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
version="1.0.12"  # Increment version
__version__ = "1.0.12"
```

### 3. Build Package
```bash
rm -rf dist && pyproject-build
```

### 4. Check Package (Optional)
```bash
twine check dist/*
```

### 5. Upload to PyPI
```bash
twine upload dist/*
```

### 6. Verify Upload
```bash
pipx upgrade kognamcp
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
- `1.0.7` - Cleaned up documentation and made it generic
- `1.0.8` - Fixed JSON-RPC null ID issue
- `1.0.9` - Fixed JSON-RPC notification handling
- `1.0.10` - Fixed JSON-RPC notification handling
- `1.0.11` - Cleaned up code and reduced duplication
- `1.0.12` - Fixed help text formatting 