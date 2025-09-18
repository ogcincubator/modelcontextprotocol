#!/usr/bin/env python3
"""
Script to generate all MCP method example files
Run this script to create all JSON files in a local directory
"""

import json
import os

# Create directory for MCP files
os.makedirs('mcp_methods', exist_ok=True)

# Define all MCP method examples
mcp_methods = {
    'initialize.json': {
        "jsonrpc": "2.0",
        "id": "1",
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {
                "tools": {},
                "resources": {},
                "prompts": {},
                "logging": {}
            },
            "clientInfo": {
                "name": "example-client",
                "version": "1.0.0"
            }
        }
    },
    
    'initialized.json': {
        "jsonrpc": "2.0",
        "method": "notifications/initialized"
    },
    
    'tools_list.json': {
        "jsonrpc": "2.0",
        "id": "2",
        "method": "tools/list",
        "params": {}
    },
    
    'tools_call.json': {
        "jsonrpc": "2.0",
        "id": "3",
        "method": "tools/call",
        "params": {
            "name": "get_weather",
            "arguments": {
                "location": "San Francisco",
                "units": "celsius"
            }
        }
    },
    
    'resources_list.json': {
        "jsonrpc": "2.0",
        "id": "4",
        "method": "resources/list",
        "params": {}
    },
    
    'resources_read.json': {
        "jsonrpc": "2.0",
        "id": "5",
        "method": "resources/read",
        "params": {
            "uri": "file:///path/to/document.txt"
        }
    },
    
    'resources_subscribe.json': {
        "jsonrpc": "2.0",
        "id": "6",
        "method": "resources/subscribe",
        "params": {
            "uri": "file:///path/to/watched/directory"
        }
    },
    
    'resources_unsubscribe.json': {
        "jsonrpc": "2.0",
        "id": "7",
        "method": "resources/unsubscribe",
        "params": {
            "uri": "file:///path/to/watched/directory"
        }
    },
    
    'prompts_list.json': {
        "jsonrpc": "2.0",
        "id": "8",
        "method": "prompts/list",
        "params": {}
    },
    
    'prompts_get.json': {
        "jsonrpc": "2.0",
        "id": "9",
        "method": "prompts/get",
        "params": {
            "name": "code_review",
            "arguments": {
                "language": "python",
                "complexity": "high"
            }
        }
    },
    
    'logging_setLevel.json': {
        "jsonrpc": "2.0",
        "id": "10",
        "method": "logging/setLevel",
        "params": {
            "level": "info"
        }
    },
    
    'completion_complete.json': {
        "jsonrpc": "2.0",
        "id": "11",
        "method": "completion/complete",
        "params": {
            "ref": {
                "type": "ref/resource",
                "uri": "file:///path/to/file.py"
            },
            "argument": {
                "name": "query",
                "value": "def calculate_"
            }
        }
    },
    
    'notifications_cancelled.json': {
        "jsonrpc": "2.0",
        "method": "notifications/cancelled",
        "params": {
            "requestId": "3",
            "reason": "User requested cancellation"
        }
    },
    
    'notifications_progress.json': {
        "jsonrpc": "2.0",
        "method": "notifications/progress",
        "params": {
            "progressToken": "upload_123",
            "progress": 75,
            "total": 100
        }
    },
    
    'notifications_resources_updated.json': {
        "jsonrpc": "2.0",
        "method": "notifications/resources/updated",
        "params": {
            "uri": "file:///path/to/document.txt"
        }
    },
    
    'notifications_resources_list_changed.json': {
        "jsonrpc": "2.0",
        "method": "notifications/resources/list_changed"
    },
    
    'notifications_tools_list_changed.json': {
        "jsonrpc": "2.0",
        "method": "notifications/tools/list_changed"
    },
    
    'notifications_prompts_list_changed.json': {
        "jsonrpc": "2.0",
        "method": "notifications/prompts/list_changed"
    },
    
    'sampling_createMessage.json': {
        "jsonrpc": "2.0",
        "id": "12",
        "method": "sampling/createMessage",
        "params": {
            "messages": [
                {
                    "role": "user",
                    "content": {
                        "type": "text",
                        "text": "What's the weather like today?"
                    }
                }
            ],
            "modelPreferences": {
                "hints": [
                    {
                        "name": "claude-3-sonnet"
                    }
                ],
                "costPriority": 0.5,
                "speedPriority": 0.8,
                "intelligencePriority": 0.9
            },
            "systemPrompt": "You are a helpful weather assistant.",
            "includeContext": "thisServer",
            "temperature": 0.7,
            "maxTokens": 1000
        }
    },
    
    'roots_list.json': {
        "jsonrpc": "2.0",
        "id": "13",
        "method": "roots/list",
        "params": {}
    }
}

# Generate all files
for filename, content in mcp_methods.items():
    filepath = os.path.join('mcp_methods', filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(content, f, indent=2, ensure_ascii=False)
    print(f"Created: {filepath}")

# Create the mapping file as well
mapping_content = """# MCP Method Files and JSON Schema Fragments

## File List and Schema Mappings

| File Name | Method | Schema Fragment |
|-----------|--------|-----------------|
| `initialize.json` | `initialize` | `InitializeRequest` |
| `initialized.json` | `notifications/initialized` | `InitializedNotification` |
| `tools_list.json` | `tools/list` | `ListToolsRequest` |
| `tools_call.json` | `tools/call` | `CallToolRequest` |
| `resources_list.json` | `resources/list` | `ListResourcesRequest` |
| `resources_read.json` | `resources/read` | `ReadResourceRequest` |
| `resources_subscribe.json` | `resources/subscribe` | `SubscribeRequest` |
| `resources_unsubscribe.json` | `resources/unsubscribe` | `UnsubscribeRequest` |
| `prompts_list.json` | `prompts/list` | `ListPromptsRequest` |
| `prompts_get.json` | `prompts/get` | `GetPromptRequest` |
| `logging_setLevel.json` | `logging/setLevel` | `SetLevelRequest` |
| `completion_complete.json` | `completion/complete` | `CompleteRequest` |
| `notifications_cancelled.json` | `notifications/cancelled` | `CancelledNotification` |
| `notifications_progress.json` | `notifications/progress` | `ProgressNotification` |
| `notifications_resources_updated.json` | `notifications/resources/updated` | `ResourceUpdatedNotification` |
| `notifications_resources_list_changed.json` | `notifications/resources/list_changed` | `ResourceListChangedNotification` |
| `notifications_tools_list_changed.json` | `notifications/tools/list_changed` | `ToolListChangedNotification` |
| `notifications_prompts_list_changed.json` | `notifications/prompts/list_changed` | `PromptListChangedNotification` |
| `sampling_createMessage.json` | `sampling/createMessage` | `CreateMessageRequest` |
| `roots_list.json` | `roots/list` | `ListRootsRequest` |
"""

with open('mcp_methods/README.md', 'w', encoding='utf-8') as f:
    f.write(mapping_content)

print(f"Created: mcp_methods/README.md")
print(f"\nAll {len(mcp_methods)} MCP method files created in 'mcp_methods' directory")
print("You can now zip the 'mcp_methods' directory to package all files together.")
