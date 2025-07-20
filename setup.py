from setuptools import setup, find_packages

setup(
    name="kogna-mcp",
    version="1.0.0",
    description="Kogna MCP Server - Multi-agent AI avatar room engine",
    author="Subbu Bhamidipati",
    author_email="bhsubbu.1995@gmail.com",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
        "httpx>=0.24.0"
    ],
    entry_points={
        "console_scripts": [
            "kogna-mcp=kogna-mcp.bridge:main",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    keywords="mcp, ai, avatar, conversation, multi-agent",
    project_urls={
        "Homepage": "https://github.com/subbub/kogna-mcp",
        "Bug Reports": "https://github.com/subbub/kogna-mcp/issues",
        "Source": "https://github.com/subbub/kogna-mcp",
    },
) 