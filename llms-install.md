# Kogna MCP Server Installation Guide

## Overview
Kogna is a multi-agent AI system that provides MCP tools for interacting with AI avatars in virtual rooms. The server connects to a hosted backend service.

## Installation Steps

### 1. Install the Package
```bash
pip install kognamcp
```

### 2. Configure MCP Client
Add this configuration to your MCP client (e.g., Cursor):

```json
{
  "mcpServers": {
    "kogna": {
      "command": "kognamcp"
    }
  }
}
```

That's it! The Kogna MCP server will connect to the hosted backend automatically.

## Available MCP Tools

### 1. Start Kogna Conversation
- **Tool**: `start_kogna_conversation`
- **Description**: Start a new Kogna conversation with a specific avatar or room. Requires platform_user_id, platform, and channel_id.
- **Required Parameters**: 
  - `platform_user_id`: Platform-specific user identifier
  - `platform`: Platform name (e.g., 'slack', 'whatsapp', 'cursor')
  - `channel_id`: Channel/session identifier
- **Optional Parameters**:
  - `avatar_id`: ID of the avatar to start conversation with
  - `room_id`: ID of the room to start conversation in
  - `message`: Initial message to send

### 2. Send Message to Kogna
- **Tool**: `send_kogna_message`
- **Description**: Send a message to the current Kogna conversation. Requires platform_user_id, platform, and channel_id.
- **Required Parameters**:
  - `platform_user_id`: Platform-specific user identifier
  - `platform`: Platform name (e.g., 'slack', 'whatsapp', 'cursor')
  - `channel_id`: Channel/session identifier
  - `message`: Message to send to the Kogna conversation

### 3. List Available Avatars
- **Tool**: `list_kogna_avatars`
- **Description**: Get list of available Kogna avatars and their specialties. Use this to see what avatars are available in Kogna.
- **Optional Parameters**:
  - `room_id`: Filter Kogna avatars by room

### 4. List Available Rooms
- **Tool**: `list_kogna_rooms`
- **Description**: Get list of available Kogna rooms and their descriptions. Use this to see what rooms are available in Kogna.
- **Parameters**: None required

### 5. Switch Avatar
- **Tool**: `switch_kogna_avatar`
- **Description**: Switch to a different avatar in the current Kogna conversation. Use this to change which Kogna avatar you're talking to.
- **Required Parameters**:
  - `platform_user_id`: Platform-specific user identifier
  - `platform`: Platform name (e.g., 'slack', 'whatsapp', 'cursor')
  - `channel_id`: Channel/session identifier
  - `avatar_id`: ID of the Kogna avatar to switch to

### 6. Switch Room
- **Tool**: `switch_kogna_room`
- **Description**: Switch to a different Kogna room/context. Use this to change which Kogna room you're in.
- **Required Parameters**:
  - `platform_user_id`: Platform-specific user identifier
  - `platform`: Platform name (e.g., 'slack', 'whatsapp', 'cursor')
  - `channel_id`: Channel/session identifier
  - `room_id`: ID of the Kogna room to switch to

### 7. Get Conversation History
- **Tool**: `get_kogna_conversation_history`
- **Description**: Get the current Kogna conversation history. Use this to see the conversation with Kogna avatars.
- **Required Parameters**:
  - `platform_user_id`: Platform-specific user identifier
  - `platform`: Platform name (e.g., 'slack', 'whatsapp', 'cursor')
  - `channel_id`: Channel/session identifier
- **Optional Parameters**:
  - `limit`: Limit number of messages returned
  - `order`: Order of messages: 'asc' or 'desc'

### 8. Get System Info
- **Tool**: `get_kogna_system_info`
- **Description**: Get Kogna system information and status. Use this to check Kogna server status and available tools.
- **Parameters**: None required

## Testing the Installation

1. Start a conversation:
   ```json
   {
     "jsonrpc": "2.0",
     "id": 1,
     "method": "tools/call",
     "params": {
       "name": "start_kogna_conversation",
       "arguments": {
         "platform_user_id": "user123",
         "platform": "cursor",
         "channel_id": "channel456",
         "message": "Hello! Can you introduce yourself?"
       }
     }
   }
   ```

2. Send a message:
   ```json
   {
     "jsonrpc": "2.0",
     "id": 2,
     "method": "tools/call",
     "params": {
       "name": "send_kogna_message",
       "arguments": {
         "platform_user_id": "user123",
         "platform": "cursor",
         "channel_id": "channel456",
         "message": "Tell me about your capabilities"
       }
     }
   }
   ```

3. List available avatars:
   ```json
   {
     "jsonrpc": "2.0",
     "id": 3,
     "method": "tools/call",
     "params": {
       "name": "list_kogna_avatars",
       "arguments": {}
     }
   }
   ```

## Session Management

**Important**: All conversation operations require session management parameters:
- `platform_user_id`: Unique identifier for the user
- `platform`: Platform name (e.g., 'cursor', 'slack', 'whatsapp')
- `channel_id`: Channel or session identifier

These parameters ensure conversations are properly isolated and managed across different users and platforms.

## Troubleshooting

- **Rate Limiting**: The server implements rate limiting (50 requests/minute per IP)
- **No Authentication Required**: The service is open for public use
- **Service Status**: The server is deployed on Railway and should be always available
- **Session Management**: Make sure to provide all required session parameters

## Support

For issues or questions, check the main README.md or create an issue in the repository.

## For Developers

If you want to run your own instance or contribute to development, see the main Kogna repository. 