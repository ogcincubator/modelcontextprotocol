
# MCP (Schema)

`mcp.mcp` *v1.0.0*

None

[*Status*](http://www.opengis.net/def/status): Stable

## Examples

### initialize
#### json
```json
{
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
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/modelcontextprotocol/build/annotated/mcp/context.jsonld",
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
}
```

#### ttl
```ttl
@prefix mcp: <http://modelcontextprotocol.io/ontology#> .

[] mcp:id "1" ;
    mcp:jsonrpc "2.0" ;
    mcp:method "initialize" ;
    mcp:params [ mcp:capabilities [ mcp:logging [ ] ;
                    mcp:prompts [ ] ;
                    mcp:resources [ ] ;
                    mcp:tools [ ] ] ;
            mcp:clientInfo [ mcp:name "example-client" ;
                    mcp:version "1.0.0" ] ;
            mcp:protocolVersion "2024-11-05" ] .


```


### notifications/initialized
#### json
```json
{
  "jsonrpc": "2.0",
  "method": "notifications/initialized"
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/modelcontextprotocol/build/annotated/mcp/context.jsonld",
  "jsonrpc": "2.0",
  "method": "notifications/initialized"
}
```

#### ttl
```ttl
@prefix mcp: <http://modelcontextprotocol.io/ontology#> .

[] mcp:jsonrpc "2.0" ;
    mcp:method "notifications/initialized" .


```


### tools/list
#### json
```json
{
  "jsonrpc": "2.0",
  "id": "2",
  "method": "tools/list",
  "params": {}
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/modelcontextprotocol/build/annotated/mcp/context.jsonld",
  "jsonrpc": "2.0",
  "id": "2",
  "method": "tools/list",
  "params": {}
}
```

#### ttl
```ttl
@prefix mcp: <http://modelcontextprotocol.io/ontology#> .

[] mcp:id "2" ;
    mcp:jsonrpc "2.0" ;
    mcp:method "tools/list" ;
    mcp:params [ ] .


```


### tools/call
#### json
```json
{
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
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/modelcontextprotocol/build/annotated/mcp/context.jsonld",
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
}
```

#### ttl
```ttl
@prefix mcp: <http://modelcontextprotocol.io/ontology#> .

[] mcp:id "3" ;
    mcp:jsonrpc "2.0" ;
    mcp:method "tools/call" ;
    mcp:params [ mcp:arguments [ mcp:location "San Francisco" ;
                    mcp:units "celsius" ] ;
            mcp:name "get_weather" ] .


```


### resources/list
#### json
```json
{
  "jsonrpc": "2.0",
  "id": "4",
  "method": "resources/list",
  "params": {}
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/modelcontextprotocol/build/annotated/mcp/context.jsonld",
  "jsonrpc": "2.0",
  "id": "4",
  "method": "resources/list",
  "params": {}
}
```

#### ttl
```ttl
@prefix mcp: <http://modelcontextprotocol.io/ontology#> .

[] mcp:id "4" ;
    mcp:jsonrpc "2.0" ;
    mcp:method "resources/list" ;
    mcp:params [ ] .


```


### resources/read
#### json
```json
{
  "jsonrpc": "2.0",
  "id": "5",
  "method": "resources/read",
  "params": {
    "uri": "file:///path/to/document.txt"
  }
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/modelcontextprotocol/build/annotated/mcp/context.jsonld",
  "jsonrpc": "2.0",
  "id": "5",
  "method": "resources/read",
  "params": {
    "uri": "file:///path/to/document.txt"
  }
}
```

#### ttl
```ttl
@prefix mcp: <http://modelcontextprotocol.io/ontology#> .

[] mcp:id "5" ;
    mcp:jsonrpc "2.0" ;
    mcp:method "resources/read" ;
    mcp:params [ mcp:uri "file:///path/to/document.txt" ] .


```


### resources/subscribe
#### json
```json
{
  "jsonrpc": "2.0",
  "id": "6",
  "method": "resources/subscribe",
  "params": {
    "uri": "file:///path/to/watched/directory"
  }
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/modelcontextprotocol/build/annotated/mcp/context.jsonld",
  "jsonrpc": "2.0",
  "id": "6",
  "method": "resources/subscribe",
  "params": {
    "uri": "file:///path/to/watched/directory"
  }
}
```

#### ttl
```ttl
@prefix mcp: <http://modelcontextprotocol.io/ontology#> .

[] mcp:id "6" ;
    mcp:jsonrpc "2.0" ;
    mcp:method "resources/subscribe" ;
    mcp:params [ mcp:uri "file:///path/to/watched/directory" ] .


```


### resources/unsubscribe
#### json
```json
{
  "jsonrpc": "2.0",
  "id": "7",
  "method": "resources/unsubscribe",
  "params": {
    "uri": "file:///path/to/watched/directory"
  }
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/modelcontextprotocol/build/annotated/mcp/context.jsonld",
  "jsonrpc": "2.0",
  "id": "7",
  "method": "resources/unsubscribe",
  "params": {
    "uri": "file:///path/to/watched/directory"
  }
}
```

#### ttl
```ttl
@prefix mcp: <http://modelcontextprotocol.io/ontology#> .

[] mcp:id "7" ;
    mcp:jsonrpc "2.0" ;
    mcp:method "resources/unsubscribe" ;
    mcp:params [ mcp:uri "file:///path/to/watched/directory" ] .


```


### prompts/list
#### json
```json
{
  "jsonrpc": "2.0",
  "id": "8",
  "method": "prompts/list",
  "params": {}
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/modelcontextprotocol/build/annotated/mcp/context.jsonld",
  "jsonrpc": "2.0",
  "id": "8",
  "method": "prompts/list",
  "params": {}
}
```

#### ttl
```ttl
@prefix mcp: <http://modelcontextprotocol.io/ontology#> .

[] mcp:id "8" ;
    mcp:jsonrpc "2.0" ;
    mcp:method "prompts/list" ;
    mcp:params [ ] .


```


### prompts/get
#### json
```json
{
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
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/modelcontextprotocol/build/annotated/mcp/context.jsonld",
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
}
```

#### ttl
```ttl
@prefix mcp: <http://modelcontextprotocol.io/ontology#> .

[] mcp:id "9" ;
    mcp:jsonrpc "2.0" ;
    mcp:method "prompts/get" ;
    mcp:params [ mcp:arguments [ mcp:complexity "high" ;
                    mcp:language "python" ] ;
            mcp:name "code_review" ] .


```


### logging/setLevel
#### json
```json
{
  "jsonrpc": "2.0",
  "id": "10",
  "method": "logging/setLevel",
  "params": {
    "level": "info"
  }
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/modelcontextprotocol/build/annotated/mcp/context.jsonld",
  "jsonrpc": "2.0",
  "id": "10",
  "method": "logging/setLevel",
  "params": {
    "level": "info"
  }
}
```

#### ttl
```ttl
@prefix mcp: <http://modelcontextprotocol.io/ontology#> .

[] mcp:id "10" ;
    mcp:jsonrpc "2.0" ;
    mcp:method "logging/setLevel" ;
    mcp:params [ mcp:level "info" ] .


```


### completion/complete
#### json
```json
{
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
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/modelcontextprotocol/build/annotated/mcp/context.jsonld",
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
}
```

#### ttl
```ttl
@prefix mcp: <http://modelcontextprotocol.io/ontology#> .

[] mcp:id "11" ;
    mcp:jsonrpc "2.0" ;
    mcp:method "completion/complete" ;
    mcp:params [ mcp:argument [ mcp:name "query" ;
                    mcp:value "def calculate_" ] ;
            mcp:ref [ mcp:type "ref/resource" ;
                    mcp:uri "file:///path/to/file.py" ] ] .


```


### notifications/cancelled
#### json
```json
{
  "jsonrpc": "2.0",
  "method": "notifications/cancelled",
  "params": {
    "requestId": "3",
    "reason": "User requested cancellation"
  }
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/modelcontextprotocol/build/annotated/mcp/context.jsonld",
  "jsonrpc": "2.0",
  "method": "notifications/cancelled",
  "params": {
    "requestId": "3",
    "reason": "User requested cancellation"
  }
}
```

#### ttl
```ttl
@prefix mcp: <http://modelcontextprotocol.io/ontology#> .

[] mcp:jsonrpc "2.0" ;
    mcp:method "notifications/cancelled" ;
    mcp:params [ mcp:reason "User requested cancellation" ;
            mcp:requestId "3" ] .


```


### notifications/progress
#### json
```json
{
  "jsonrpc": "2.0",
  "method": "notifications/progress",
  "params": {
    "progressToken": "upload_123",
    "progress": 75,
    "total": 100
  }
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/modelcontextprotocol/build/annotated/mcp/context.jsonld",
  "jsonrpc": "2.0",
  "method": "notifications/progress",
  "params": {
    "progressToken": "upload_123",
    "progress": 75,
    "total": 100
  }
}
```

#### ttl
```ttl
@prefix mcp: <http://modelcontextprotocol.io/ontology#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] mcp:jsonrpc "2.0" ;
    mcp:method "notifications/progress" ;
    mcp:params [ mcp:progress 75 ;
            mcp:progressToken "upload_123" ;
            mcp:total 100 ] .


```


### notifications/resources/updated
#### json
```json
{
  "jsonrpc": "2.0",
  "method": "notifications/resources/updated",
  "params": {
    "uri": "file:///path/to/document.txt"
  }
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/modelcontextprotocol/build/annotated/mcp/context.jsonld",
  "jsonrpc": "2.0",
  "method": "notifications/resources/updated",
  "params": {
    "uri": "file:///path/to/document.txt"
  }
}
```

#### ttl
```ttl
@prefix mcp: <http://modelcontextprotocol.io/ontology#> .

[] mcp:jsonrpc "2.0" ;
    mcp:method "notifications/resources/updated" ;
    mcp:params [ mcp:uri "file:///path/to/document.txt" ] .


```


### notifications/resources/list_changed
#### json
```json
{
  "jsonrpc": "2.0",
  "method": "notifications/resources/list_changed"
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/modelcontextprotocol/build/annotated/mcp/context.jsonld",
  "jsonrpc": "2.0",
  "method": "notifications/resources/list_changed"
}
```

#### ttl
```ttl
@prefix mcp: <http://modelcontextprotocol.io/ontology#> .

[] mcp:jsonrpc "2.0" ;
    mcp:method "notifications/resources/list_changed" .


```


### notifications/tools/list_changed
#### json
```json
{
  "jsonrpc": "2.0",
  "method": "notifications/tools/list_changed"
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/modelcontextprotocol/build/annotated/mcp/context.jsonld",
  "jsonrpc": "2.0",
  "method": "notifications/tools/list_changed"
}
```

#### ttl
```ttl
@prefix mcp: <http://modelcontextprotocol.io/ontology#> .

[] mcp:jsonrpc "2.0" ;
    mcp:method "notifications/tools/list_changed" .


```


### notifications/prompts/list_changed
#### json
```json
{
  "jsonrpc": "2.0",
  "method": "notifications/prompts/list_changed"
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/modelcontextprotocol/build/annotated/mcp/context.jsonld",
  "jsonrpc": "2.0",
  "method": "notifications/prompts/list_changed"
}
```

#### ttl
```ttl
@prefix mcp: <http://modelcontextprotocol.io/ontology#> .

[] mcp:jsonrpc "2.0" ;
    mcp:method "notifications/prompts/list_changed" .


```


### sampling/createMessage
#### json
```json
{
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
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/modelcontextprotocol/build/annotated/mcp/context.jsonld",
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
}
```

#### ttl
```ttl
@prefix mcp: <http://modelcontextprotocol.io/ontology#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] mcp:id "12" ;
    mcp:jsonrpc "2.0" ;
    mcp:method "sampling/createMessage" ;
    mcp:params [ mcp:includeContext "thisServer" ;
            mcp:maxTokens 1000 ;
            mcp:messages [ mcp:content [ mcp:text "What's the weather like today?" ;
                            mcp:type "text" ] ;
                    mcp:role "user" ] ;
            mcp:modelPreferences [ mcp:costPriority 5e-01 ;
                    mcp:hints [ mcp:name "claude-3-sonnet" ] ;
                    mcp:intelligencePriority 9e-01 ;
                    mcp:speedPriority 8e-01 ] ;
            mcp:systemPrompt "You are a helpful weather assistant." ;
            mcp:temperature 7e-01 ] .


```


### roots/list
#### json
```json
{
  "jsonrpc": "2.0",
  "id": "13",
  "method": "roots/list",
  "params": {}
}
```

#### jsonld
```jsonld
{
  "@context": "https://ogcincubator.github.io/modelcontextprotocol/build/annotated/mcp/context.jsonld",
  "jsonrpc": "2.0",
  "id": "13",
  "method": "roots/list",
  "params": {}
}
```

#### ttl
```ttl
@prefix mcp: <http://modelcontextprotocol.io/ontology#> .

[] mcp:id "13" ;
    mcp:jsonrpc "2.0" ;
    mcp:method "roots/list" ;
    mcp:params [ ] .


```

## Schema

```yaml
$schema: http://json-schema.org/draft-07/schema#
definitions:
  ProgressToken:
    $ref: https://ogcincubator.github.io/modelcontextprotocol/build/annotated/json-rpc/schema.yaml#ProgressToken
  Annotations:
    description: Optional annotations for the client. The client can use annotations
      to inform how objects are used or displayed
    properties:
      audience:
        description: 'Describes who the intended customer of this object or data is.


          It can include multiple entries to indicate content useful for multiple
          audiences (e.g., `["user", "assistant"]`).'
        items:
          $ref: '#/definitions/Role'
        type: array
        x-jsonld-id: http://modelcontextprotocol.io/ontology#audience
      lastModified:
        description: 'The moment the resource was last modified, as an ISO 8601 formatted
          string.


          Should be an ISO 8601 formatted string (e.g., "2025-01-12T15:00:58Z").


          Examples: last activity timestamp in an open file, timestamp when the resource

          was attached, etc.'
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#lastModified
      priority:
        description: 'Describes how important this data is for operating the server.


          A value of 1 means "most important," and indicates that the data is

          effectively required, while 0 means "least important," and indicates that

          the data is entirely optional.'
        maximum: 1
        minimum: 0
        type: number
        x-jsonld-id: http://modelcontextprotocol.io/ontology#priority
    type: object
  AudioContent:
    description: Audio provided to or from an LLM.
    properties:
      _meta:
        additionalProperties: {}
        description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
          for notes on `_meta` usage.'
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
      annotations:
        $ref: '#/definitions/Annotations'
        description: Optional annotations for the client.
        x-jsonld-id: http://modelcontextprotocol.io/ontology#annotations
      data:
        description: The base64-encoded audio data.
        format: byte
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#data
      mimeType:
        description: The MIME type of the audio. Different providers may support different
          audio types.
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#mimeType
      type:
        const: audio
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#type
    required:
    - data
    - mimeType
    - type
    type: object
  BaseMetadata:
    description: Base interface for metadata with name (identifier) and title (display
      name) properties.
    properties:
      name:
        description: Intended for programmatic or logical use, but used as a display
          name in past specs or fallback (if title isn't present).
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#name
      title:
        description: "Intended for UI and end-user contexts \u2014 optimized to be
          human-readable and easily understood,\neven by those unfamiliar with domain-specific
          terminology.\n\nIf not provided, the name should be used for display (except
          for Tool,\nwhere `annotations.title` should be given precedence over using
          `name`,\nif present)."
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#title
    required:
    - name
    type: object
  BlobResourceContents:
    properties:
      _meta:
        additionalProperties: {}
        description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
          for notes on `_meta` usage.'
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
      blob:
        description: A base64-encoded string representing the binary data of the item.
        format: byte
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#blob
      mimeType:
        description: The MIME type of this resource, if known.
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#mimeType
      uri:
        description: The URI of this resource.
        format: uri
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#uri
    required:
    - blob
    - uri
    type: object
  BooleanSchema:
    properties:
      default:
        type: boolean
        x-jsonld-id: http://modelcontextprotocol.io/ontology#default
      description:
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#description
      title:
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#title
      type:
        const: boolean
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#type
    required:
    - type
    type: object
  CallToolRequest:
    description: Used by the client to invoke a tool provided by the server.
    properties:
      method:
        const: tools/call
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#method
      params:
        properties:
          arguments:
            additionalProperties: {}
            type: object
            x-jsonld-id: http://modelcontextprotocol.io/ontology#arguments
          name:
            type: string
            x-jsonld-id: http://modelcontextprotocol.io/ontology#name
        required:
        - name
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#params
    required:
    - method
    - params
    type: object
  CallToolResult:
    description: The server's response to a tool call.
    properties:
      _meta:
        additionalProperties: {}
        description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
          for notes on `_meta` usage.'
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
      content:
        description: A list of content objects that represent the unstructured result
          of the tool call.
        items:
          $ref: '#/definitions/ContentBlock'
        type: array
        x-jsonld-id: http://modelcontextprotocol.io/ontology#content
      isError:
        description: 'Whether the tool call ended in an error.


          If not set, this is assumed to be false (the call was successful).


          Any errors that originate from the tool SHOULD be reported inside the result

          object, with `isError` set to true, _not_ as an MCP protocol-level error

          response. Otherwise, the LLM would not be able to see that an error occurred

          and self-correct.


          However, any errors in _finding_ the tool, an error indicating that the

          server does not support tool calls, or any other exceptional conditions,

          should be reported as an MCP error response.'
        type: boolean
        x-jsonld-id: http://modelcontextprotocol.io/ontology#isError
      structuredContent:
        additionalProperties: {}
        description: An optional JSON object that represents the structured result
          of the tool call.
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#structuredContent
    required:
    - content
    type: object
  CancelledNotification:
    description: 'This notification can be sent by either side to indicate that it
      is cancelling a previously-issued request.


      The request SHOULD still be in-flight, but due to communication latency, it
      is always possible that this notification MAY arrive after the request has already
      finished.


      This notification indicates that the result will be unused, so any associated
      processing SHOULD cease.


      A client MUST NOT attempt to cancel its `initialize` request.'
    properties:
      method:
        const: notifications/cancelled
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#method
      params:
        properties:
          reason:
            description: An optional string describing the reason for the cancellation.
              This MAY be logged or presented to the user.
            type: string
            x-jsonld-id: http://modelcontextprotocol.io/ontology#reason
          requestId:
            $ref: '#/definitions/RequestId'
            description: 'The ID of the request to cancel.


              This MUST correspond to the ID of a request previously issued in the
              same direction.'
            x-jsonld-id: http://modelcontextprotocol.io/ontology#requestId
        required:
        - requestId
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#params
    required:
    - method
    - params
    type: object
  ClientCapabilities:
    description: 'Capabilities a client may support. Known capabilities are defined
      here, in this schema, but this is not a closed set: any client can define its
      own, additional capabilities.'
    properties:
      elicitation:
        additionalProperties: true
        description: Present if the client supports elicitation from the server.
        properties: {}
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#elicitation
      experimental:
        additionalProperties:
          additionalProperties: true
          properties: {}
          type: object
        description: Experimental, non-standard capabilities that the client supports.
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#experimental
      roots:
        description: Present if the client supports listing roots.
        properties:
          listChanged:
            description: Whether the client supports notifications for changes to
              the roots list.
            type: boolean
            x-jsonld-id: http://modelcontextprotocol.io/ontology#listChanged
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#roots
      sampling:
        additionalProperties: true
        description: Present if the client supports sampling from an LLM.
        properties: {}
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#sampling
    type: object
  ClientNotification:
    anyOf:
    - $ref: '#/definitions/CancelledNotification'
    - $ref: '#/definitions/InitializedNotification'
    - $ref: '#/definitions/ProgressNotification'
    - $ref: '#/definitions/RootsListChangedNotification'
  ClientRequest:
    anyOf:
    - $ref: '#/definitions/InitializeRequest'
    - $ref: '#/definitions/PingRequest'
    - $ref: '#/definitions/ListResourcesRequest'
    - $ref: '#/definitions/ListResourceTemplatesRequest'
    - $ref: '#/definitions/ReadResourceRequest'
    - $ref: '#/definitions/SubscribeRequest'
    - $ref: '#/definitions/UnsubscribeRequest'
    - $ref: '#/definitions/ListPromptsRequest'
    - $ref: '#/definitions/GetPromptRequest'
    - $ref: '#/definitions/ListToolsRequest'
    - $ref: '#/definitions/CallToolRequest'
    - $ref: '#/definitions/SetLevelRequest'
    - $ref: '#/definitions/CompleteRequest'
  ClientResult:
    anyOf:
    - $ref: '#/definitions/Result'
    - $ref: '#/definitions/CreateMessageResult'
    - $ref: '#/definitions/ListRootsResult'
    - $ref: '#/definitions/ElicitResult'
  CompleteRequest:
    description: A request from the client to the server, to ask for completion options.
    properties:
      method:
        const: completion/complete
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#method
      params:
        properties:
          argument:
            description: The argument's information
            properties:
              name:
                description: The name of the argument
                type: string
                x-jsonld-id: http://modelcontextprotocol.io/ontology#name
              value:
                description: The value of the argument to use for completion matching.
                type: string
                x-jsonld-id: http://modelcontextprotocol.io/ontology#value
            required:
            - name
            - value
            type: object
            x-jsonld-id: http://modelcontextprotocol.io/ontology#argument
          context:
            description: Additional, optional context for completions
            properties:
              arguments:
                additionalProperties:
                  type: string
                description: Previously-resolved variables in a URI template or prompt.
                type: object
                x-jsonld-id: http://modelcontextprotocol.io/ontology#arguments
            type: object
            x-jsonld-id: http://modelcontextprotocol.io/ontology#context
          ref:
            anyOf:
            - $ref: '#/definitions/PromptReference'
            - $ref: '#/definitions/ResourceTemplateReference'
            x-jsonld-id: http://modelcontextprotocol.io/ontology#ref
        required:
        - argument
        - ref
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#params
    required:
    - method
    - params
    type: object
  CompleteResult:
    description: The server's response to a completion/complete request
    properties:
      _meta:
        additionalProperties: {}
        description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
          for notes on `_meta` usage.'
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
      completion:
        properties:
          hasMore:
            description: Indicates whether there are additional completion options
              beyond those provided in the current response, even if the exact total
              is unknown.
            type: boolean
            x-jsonld-id: http://modelcontextprotocol.io/ontology#hasMore
          total:
            description: The total number of completion options available. This can
              exceed the number of values actually sent in the response.
            type: integer
            x-jsonld-id: http://modelcontextprotocol.io/ontology#total
          values:
            description: An array of completion values. Must not exceed 100 items.
            items:
              type: string
            type: array
            x-jsonld-id: http://modelcontextprotocol.io/ontology#values
        required:
        - values
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#completion
    required:
    - completion
    type: object
  ContentBlock:
    anyOf:
    - $ref: '#/definitions/TextContent'
    - $ref: '#/definitions/ImageContent'
    - $ref: '#/definitions/AudioContent'
    - $ref: '#/definitions/ResourceLink'
    - $ref: '#/definitions/EmbeddedResource'
  CreateMessageRequest:
    description: A request from the server to sample an LLM via the client. The client
      has full discretion over which model to select. The client should also inform
      the user before beginning sampling, to allow them to inspect the request (human
      in the loop) and decide whether to approve it.
    properties:
      method:
        const: sampling/createMessage
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#method
      params:
        properties:
          includeContext:
            description: A request to include context from one or more MCP servers
              (including the caller), to be attached to the prompt. The client MAY
              ignore this request.
            enum:
            - allServers
            - none
            - thisServer
            type: string
            x-jsonld-id: http://modelcontextprotocol.io/ontology#includeContext
          maxTokens:
            description: The maximum number of tokens to sample, as requested by the
              server. The client MAY choose to sample fewer tokens than requested.
            type: integer
            x-jsonld-id: http://modelcontextprotocol.io/ontology#maxTokens
          messages:
            items:
              $ref: '#/definitions/SamplingMessage'
            type: array
            x-jsonld-id: http://modelcontextprotocol.io/ontology#messages
          metadata:
            additionalProperties: true
            description: Optional metadata to pass through to the LLM provider. The
              format of this metadata is provider-specific.
            properties: {}
            type: object
            x-jsonld-id: http://modelcontextprotocol.io/ontology#metadata
          modelPreferences:
            $ref: '#/definitions/ModelPreferences'
            description: The server's preferences for which model to select. The client
              MAY ignore these preferences.
            x-jsonld-id: http://modelcontextprotocol.io/ontology#modelPreferences
          stopSequences:
            items:
              type: string
            type: array
            x-jsonld-id: http://modelcontextprotocol.io/ontology#stopSequences
          systemPrompt:
            description: An optional system prompt the server wants to use for sampling.
              The client MAY modify or omit this prompt.
            type: string
            x-jsonld-id: http://modelcontextprotocol.io/ontology#systemPrompt
          temperature:
            type: number
            x-jsonld-id: http://modelcontextprotocol.io/ontology#temperature
        required:
        - maxTokens
        - messages
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#params
    required:
    - method
    - params
    type: object
  CreateMessageResult:
    description: The client's response to a sampling/create_message request from the
      server. The client should inform the user before returning the sampled message,
      to allow them to inspect the response (human in the loop) and decide whether
      to allow the server to see it.
    properties:
      _meta:
        additionalProperties: {}
        description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
          for notes on `_meta` usage.'
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
      content:
        anyOf:
        - $ref: '#/definitions/TextContent'
        - $ref: '#/definitions/ImageContent'
        - $ref: '#/definitions/AudioContent'
        x-jsonld-id: http://modelcontextprotocol.io/ontology#content
      model:
        description: The name of the model that generated the message.
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#model
      role:
        $ref: '#/definitions/Role'
        x-jsonld-id: http://modelcontextprotocol.io/ontology#role
      stopReason:
        description: The reason why sampling stopped, if known.
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#stopReason
    required:
    - content
    - model
    - role
    type: object
  Cursor:
    description: An opaque token used to represent a cursor for pagination.
    type: string
  ElicitRequest:
    description: A request from the server to elicit additional information from the
      user via the client.
    properties:
      method:
        const: elicitation/create
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#method
      params:
        properties:
          message:
            description: The message to present to the user.
            type: string
            x-jsonld-id: http://modelcontextprotocol.io/ontology#message
          requestedSchema:
            description: 'A restricted subset of JSON Schema.

              Only top-level properties are allowed, without nesting.'
            properties:
              properties:
                additionalProperties:
                  $ref: '#/definitions/PrimitiveSchemaDefinition'
                type: object
                x-jsonld-id: http://modelcontextprotocol.io/ontology#properties
              required:
                items:
                  type: string
                type: array
                x-jsonld-id: http://modelcontextprotocol.io/ontology#required
              type:
                const: object
                type: string
                x-jsonld-id: http://modelcontextprotocol.io/ontology#type
            required:
            - properties
            - type
            type: object
            x-jsonld-id: http://modelcontextprotocol.io/ontology#requestedSchema
        required:
        - message
        - requestedSchema
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#params
    required:
    - method
    - params
    type: object
  ElicitResult:
    description: The client's response to an elicitation request.
    properties:
      _meta:
        additionalProperties: {}
        description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
          for notes on `_meta` usage.'
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
      action:
        description: 'The user action in response to the elicitation.

          - "accept": User submitted the form/confirmed the action

          - "decline": User explicitly declined the action

          - "cancel": User dismissed without making an explicit choice'
        enum:
        - accept
        - cancel
        - decline
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#action
      content:
        additionalProperties:
          type:
          - string
          - integer
          - boolean
        description: 'The submitted form data, only present when action is "accept".

          Contains values matching the requested schema.'
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#content
    required:
    - action
    type: object
  EmbeddedResource:
    description: 'The contents of a resource, embedded into a prompt or tool call
      result.


      It is up to the client how best to render embedded resources for the benefit

      of the LLM and/or the user.'
    properties:
      _meta:
        additionalProperties: {}
        description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
          for notes on `_meta` usage.'
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
      annotations:
        $ref: '#/definitions/Annotations'
        description: Optional annotations for the client.
        x-jsonld-id: http://modelcontextprotocol.io/ontology#annotations
      resource:
        anyOf:
        - $ref: '#/definitions/TextResourceContents'
        - $ref: '#/definitions/BlobResourceContents'
        x-jsonld-id: http://modelcontextprotocol.io/ontology#resource
      type:
        const: resource
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#type
    required:
    - resource
    - type
    type: object
  EmptyResult:
    $ref: '#/definitions/Result'
  EnumSchema:
    properties:
      description:
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#description
      enum:
        items:
          type: string
        type: array
        x-jsonld-id: http://modelcontextprotocol.io/ontology#enum
      enumNames:
        items:
          type: string
        type: array
        x-jsonld-id: http://modelcontextprotocol.io/ontology#enumNames
      title:
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#title
      type:
        const: string
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#type
    required:
    - enum
    - type
    type: object
  GetPromptRequest:
    description: Used by the client to get a prompt provided by the server.
    properties:
      method:
        const: prompts/get
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#method
      params:
        properties:
          arguments:
            additionalProperties:
              type: string
            description: Arguments to use for templating the prompt.
            type: object
            x-jsonld-id: http://modelcontextprotocol.io/ontology#arguments
          name:
            description: The name of the prompt or prompt template.
            type: string
            x-jsonld-id: http://modelcontextprotocol.io/ontology#name
        required:
        - name
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#params
    required:
    - method
    - params
    type: object
  GetPromptResult:
    description: The server's response to a prompts/get request from the client.
    properties:
      _meta:
        additionalProperties: {}
        description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
          for notes on `_meta` usage.'
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
      description:
        description: An optional description for the prompt.
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#description
      messages:
        items:
          $ref: '#/definitions/PromptMessage'
        type: array
        x-jsonld-id: http://modelcontextprotocol.io/ontology#messages
    required:
    - messages
    type: object
  ImageContent:
    description: An image provided to or from an LLM.
    properties:
      _meta:
        additionalProperties: {}
        description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
          for notes on `_meta` usage.'
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
      annotations:
        $ref: '#/definitions/Annotations'
        description: Optional annotations for the client.
        x-jsonld-id: http://modelcontextprotocol.io/ontology#annotations
      data:
        description: The base64-encoded image data.
        format: byte
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#data
      mimeType:
        description: The MIME type of the image. Different providers may support different
          image types.
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#mimeType
      type:
        const: image
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#type
    required:
    - data
    - mimeType
    - type
    type: object
  Implementation:
    description: Describes the name and version of an MCP implementation, with an
      optional title for UI representation.
    properties:
      name:
        description: Intended for programmatic or logical use, but used as a display
          name in past specs or fallback (if title isn't present).
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#name
      title:
        description: "Intended for UI and end-user contexts \u2014 optimized to be
          human-readable and easily understood,\neven by those unfamiliar with domain-specific
          terminology.\n\nIf not provided, the name should be used for display (except
          for Tool,\nwhere `annotations.title` should be given precedence over using
          `name`,\nif present)."
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#title
      version:
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#version
    required:
    - name
    - version
    type: object
  InitializeRequest:
    description: This request is sent from the client to the server when it first
      connects, asking it to begin initialization.
    properties:
      method:
        const: initialize
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#method
      params:
        properties:
          capabilities:
            $ref: '#/definitions/ClientCapabilities'
            x-jsonld-id: http://modelcontextprotocol.io/ontology#capabilities
          clientInfo:
            $ref: '#/definitions/Implementation'
            x-jsonld-id: http://modelcontextprotocol.io/ontology#clientInfo
          protocolVersion:
            description: The latest version of the Model Context Protocol that the
              client supports. The client MAY decide to support older versions as
              well.
            type: string
            x-jsonld-id: http://modelcontextprotocol.io/ontology#protocolVersion
        required:
        - capabilities
        - clientInfo
        - protocolVersion
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#params
    required:
    - method
    - params
    type: object
  InitializeResult:
    description: After receiving an initialize request from the client, the server
      sends this response.
    properties:
      _meta:
        additionalProperties: {}
        description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
          for notes on `_meta` usage.'
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
      capabilities:
        $ref: '#/definitions/ServerCapabilities'
        x-jsonld-id: http://modelcontextprotocol.io/ontology#capabilities
      instructions:
        description: 'Instructions describing how to use the server and its features.


          This can be used by clients to improve the LLM''s understanding of available
          tools, resources, etc. It can be thought of like a "hint" to the model.
          For example, this information MAY be added to the system prompt.'
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#instructions
      protocolVersion:
        description: The version of the Model Context Protocol that the server wants
          to use. This may not match the version that the client requested. If the
          client cannot support this version, it MUST disconnect.
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#protocolVersion
      serverInfo:
        $ref: '#/definitions/Implementation'
        x-jsonld-id: http://modelcontextprotocol.io/ontology#serverInfo
    required:
    - capabilities
    - protocolVersion
    - serverInfo
    type: object
  InitializedNotification:
    description: This notification is sent from the client to the server after initialization
      has finished.
    properties:
      method:
        const: notifications/initialized
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#method
      params:
        additionalProperties: {}
        properties:
          _meta:
            additionalProperties: {}
            description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
              for notes on `_meta` usage.'
            type: object
            x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#params
    required:
    - method
    type: object
  JSONRPCError:
    description: A response to a request that indicates an error occurred.
    properties:
      error:
        properties:
          code:
            description: The error type that occurred.
            type: integer
            x-jsonld-id: http://modelcontextprotocol.io/ontology#code
          data:
            description: Additional information about the error. The value of this
              member is defined by the sender (e.g. detailed error information, nested
              errors etc.).
            x-jsonld-id: http://modelcontextprotocol.io/ontology#data
          message:
            description: A short description of the error. The message SHOULD be limited
              to a concise single sentence.
            type: string
            x-jsonld-id: http://modelcontextprotocol.io/ontology#message
        required:
        - code
        - message
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#error
      id:
        $ref: '#/definitions/RequestId'
        x-jsonld-id: http://modelcontextprotocol.io/ontology#id
      jsonrpc:
        const: '2.0'
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#jsonrpc
    required:
    - error
    - id
    - jsonrpc
    type: object
  JSONRPCMessage:
    anyOf:
    - $ref: '#/definitions/JSONRPCRequest'
    - $ref: '#/definitions/JSONRPCNotification'
    - $ref: '#/definitions/JSONRPCResponse'
    - $ref: '#/definitions/JSONRPCError'
    description: Refers to any valid JSON-RPC object that can be decoded off the wire,
      or encoded to be sent.
  JSONRPCNotification:
    description: A notification which does not expect a response.
    properties:
      jsonrpc:
        const: '2.0'
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#jsonrpc
      method:
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#method
      params:
        additionalProperties: {}
        properties:
          _meta:
            additionalProperties: {}
            description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
              for notes on `_meta` usage.'
            type: object
            x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#params
    required:
    - jsonrpc
    - method
    type: object
  JSONRPCRequest:
    description: A request that expects a response.
    properties:
      id:
        $ref: '#/definitions/RequestId'
        x-jsonld-id: http://modelcontextprotocol.io/ontology#id
      jsonrpc:
        const: '2.0'
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#jsonrpc
      method:
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#method
      params:
        additionalProperties: {}
        properties:
          _meta:
            additionalProperties: {}
            description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
              for notes on `_meta` usage.'
            properties:
              progressToken:
                $ref: '#/definitions/ProgressToken'
                description: If specified, the caller is requesting out-of-band progress
                  notifications for this request (as represented by notifications/progress).
                  The value of this parameter is an opaque token that will be attached
                  to any subsequent notifications. The receiver is not obligated to
                  provide these notifications.
                x-jsonld-id: http://modelcontextprotocol.io/ontology#progressToken
            type: object
            x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#params
    required:
    - id
    - jsonrpc
    - method
    type: object
  JSONRPCResponse:
    description: A successful (non-error) response to a request.
    properties:
      id:
        $ref: '#/definitions/RequestId'
        x-jsonld-id: http://modelcontextprotocol.io/ontology#id
      jsonrpc:
        const: '2.0'
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#jsonrpc
      result:
        $ref: '#/definitions/Result'
        x-jsonld-id: http://modelcontextprotocol.io/ontology#result
    required:
    - id
    - jsonrpc
    - result
    type: object
  ListPromptsRequest:
    description: Sent from the client to request a list of prompts and prompt templates
      the server has.
    properties:
      method:
        const: prompts/list
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#method
      params:
        properties:
          cursor:
            description: 'An opaque token representing the current pagination position.

              If provided, the server should return results starting after this cursor.'
            type: string
            x-jsonld-id: http://modelcontextprotocol.io/ontology#cursor
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#params
    required:
    - method
    type: object
  ListPromptsResult:
    description: The server's response to a prompts/list request from the client.
    properties:
      _meta:
        additionalProperties: {}
        description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
          for notes on `_meta` usage.'
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
      nextCursor:
        description: 'An opaque token representing the pagination position after the
          last returned result.

          If present, there may be more results available.'
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#nextCursor
      prompts:
        items:
          $ref: '#/definitions/Prompt'
        type: array
        x-jsonld-id: http://modelcontextprotocol.io/ontology#prompts
    required:
    - prompts
    type: object
  ListResourceTemplatesRequest:
    description: Sent from the client to request a list of resource templates the
      server has.
    properties:
      method:
        const: resources/templates/list
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#method
      params:
        properties:
          cursor:
            description: 'An opaque token representing the current pagination position.

              If provided, the server should return results starting after this cursor.'
            type: string
            x-jsonld-id: http://modelcontextprotocol.io/ontology#cursor
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#params
    required:
    - method
    type: object
  ListResourceTemplatesResult:
    description: The server's response to a resources/templates/list request from
      the client.
    properties:
      _meta:
        additionalProperties: {}
        description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
          for notes on `_meta` usage.'
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
      nextCursor:
        description: 'An opaque token representing the pagination position after the
          last returned result.

          If present, there may be more results available.'
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#nextCursor
      resourceTemplates:
        items:
          $ref: '#/definitions/ResourceTemplate'
        type: array
        x-jsonld-id: http://modelcontextprotocol.io/ontology#resourceTemplates
    required:
    - resourceTemplates
    type: object
  ListResourcesRequest:
    description: Sent from the client to request a list of resources the server has.
    properties:
      method:
        const: resources/list
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#method
      params:
        properties:
          cursor:
            description: 'An opaque token representing the current pagination position.

              If provided, the server should return results starting after this cursor.'
            type: string
            x-jsonld-id: http://modelcontextprotocol.io/ontology#cursor
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#params
    required:
    - method
    type: object
  ListResourcesResult:
    description: The server's response to a resources/list request from the client.
    properties:
      _meta:
        additionalProperties: {}
        description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
          for notes on `_meta` usage.'
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
      nextCursor:
        description: 'An opaque token representing the pagination position after the
          last returned result.

          If present, there may be more results available.'
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#nextCursor
      resources:
        items:
          $ref: '#/definitions/Resource'
        type: array
        x-jsonld-id: http://modelcontextprotocol.io/ontology#resources
    required:
    - resources
    type: object
  ListRootsRequest:
    description: 'Sent from the server to request a list of root URIs from the client.
      Roots allow

      servers to ask for specific directories or files to operate on. A common example

      for roots is providing a set of repositories or directories a server should
      operate

      on.


      This request is typically used when the server needs to understand the file
      system

      structure or access specific locations that the client has permission to read
      from.'
    properties:
      method:
        const: roots/list
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#method
      params:
        additionalProperties: {}
        properties:
          _meta:
            additionalProperties: {}
            description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
              for notes on `_meta` usage.'
            properties:
              progressToken:
                $ref: '#/definitions/ProgressToken'
                description: If specified, the caller is requesting out-of-band progress
                  notifications for this request (as represented by notifications/progress).
                  The value of this parameter is an opaque token that will be attached
                  to any subsequent notifications. The receiver is not obligated to
                  provide these notifications.
                x-jsonld-id: http://modelcontextprotocol.io/ontology#progressToken
            type: object
            x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#params
    required:
    - method
    type: object
  ListRootsResult:
    description: 'The client''s response to a roots/list request from the server.

      This result contains an array of Root objects, each representing a root directory

      or file that the server can operate on.'
    properties:
      _meta:
        additionalProperties: {}
        description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
          for notes on `_meta` usage.'
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
      roots:
        items:
          $ref: '#/definitions/Root'
        type: array
        x-jsonld-id: http://modelcontextprotocol.io/ontology#roots
    required:
    - roots
    type: object
  ListToolsRequest:
    description: Sent from the client to request a list of tools the server has.
    properties:
      method:
        const: tools/list
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#method
      params:
        properties:
          cursor:
            description: 'An opaque token representing the current pagination position.

              If provided, the server should return results starting after this cursor.'
            type: string
            x-jsonld-id: http://modelcontextprotocol.io/ontology#cursor
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#params
    required:
    - method
    type: object
  ListToolsResult:
    description: The server's response to a tools/list request from the client.
    properties:
      _meta:
        additionalProperties: {}
        description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
          for notes on `_meta` usage.'
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
      nextCursor:
        description: 'An opaque token representing the pagination position after the
          last returned result.

          If present, there may be more results available.'
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#nextCursor
      tools:
        items:
          $ref: '#/definitions/Tool'
        type: array
        x-jsonld-id: http://modelcontextprotocol.io/ontology#tools
    required:
    - tools
    type: object
  LoggingLevel:
    description: 'The severity of a log message.


      These map to syslog message severities, as specified in RFC-5424:

      https://datatracker.ietf.org/doc/html/rfc5424#section-6.2.1'
    enum:
    - alert
    - critical
    - debug
    - emergency
    - error
    - info
    - notice
    - warning
    type: string
  LoggingMessageNotification:
    description: Notification of a log message passed from server to client. If no
      logging/setLevel request has been sent from the client, the server MAY decide
      which messages to send automatically.
    properties:
      method:
        const: notifications/message
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#method
      params:
        properties:
          data:
            description: The data to be logged, such as a string message or an object.
              Any JSON serializable type is allowed here.
            x-jsonld-id: http://modelcontextprotocol.io/ontology#data
          level:
            $ref: '#/definitions/LoggingLevel'
            description: The severity of this log message.
            x-jsonld-id: http://modelcontextprotocol.io/ontology#level
          logger:
            description: An optional name of the logger issuing this message.
            type: string
            x-jsonld-id: http://modelcontextprotocol.io/ontology#logger
        required:
        - data
        - level
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#params
    required:
    - method
    - params
    type: object
  ModelHint:
    description: 'Hints to use for model selection.


      Keys not declared here are currently left unspecified by the spec and are up

      to the client to interpret.'
    properties:
      name:
        description: "A hint for a model name.\n\nThe client SHOULD treat this as
          a substring of a model name; for example:\n - `claude-3-5-sonnet` should
          match `claude-3-5-sonnet-20241022`\n - `sonnet` should match `claude-3-5-sonnet-20241022`,
          `claude-3-sonnet-20240229`, etc.\n - `claude` should match any Claude model\n\nThe
          client MAY also map the string to a different provider's model name or a
          different model family, as long as it fills a similar niche; for example:\n
          - `gemini-1.5-flash` could match `claude-3-haiku-20240307`"
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#name
    type: object
  ModelPreferences:
    description: "The server's preferences for model selection, requested of the client
      during sampling.\n\nBecause LLMs can vary along multiple dimensions, choosing
      the \"best\" model is\nrarely straightforward.  Different models excel in different
      areas\u2014some are\nfaster but less capable, others are more capable but more
      expensive, and so\non. This interface allows servers to express their priorities
      across multiple\ndimensions to help clients make an appropriate selection for
      their use case.\n\nThese preferences are always advisory. The client MAY ignore
      them. It is also\nup to the client to decide how to interpret these preferences
      and how to\nbalance them against other considerations."
    properties:
      costPriority:
        description: 'How much to prioritize cost when selecting a model. A value
          of 0 means cost

          is not important, while a value of 1 means cost is the most important

          factor.'
        maximum: 1
        minimum: 0
        type: number
        x-jsonld-id: http://modelcontextprotocol.io/ontology#costPriority
      hints:
        description: 'Optional hints to use for model selection.


          If multiple hints are specified, the client MUST evaluate them in order

          (such that the first match is taken).


          The client SHOULD prioritize these hints over the numeric priorities, but

          MAY still use the priorities to select from ambiguous matches.'
        items:
          $ref: '#/definitions/ModelHint'
        type: array
        x-jsonld-id: http://modelcontextprotocol.io/ontology#hints
      intelligencePriority:
        description: 'How much to prioritize intelligence and capabilities when selecting
          a

          model. A value of 0 means intelligence is not important, while a value of
          1

          means intelligence is the most important factor.'
        maximum: 1
        minimum: 0
        type: number
        x-jsonld-id: http://modelcontextprotocol.io/ontology#intelligencePriority
      speedPriority:
        description: 'How much to prioritize sampling speed (latency) when selecting
          a model. A

          value of 0 means speed is not important, while a value of 1 means speed
          is

          the most important factor.'
        maximum: 1
        minimum: 0
        type: number
        x-jsonld-id: http://modelcontextprotocol.io/ontology#speedPriority
    type: object
  Notification:
    properties:
      method:
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#method
      params:
        additionalProperties: {}
        properties:
          _meta:
            additionalProperties: {}
            description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
              for notes on `_meta` usage.'
            type: object
            x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#params
    required:
    - method
    type: object
  NumberSchema:
    properties:
      description:
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#description
      maximum:
        type: integer
        x-jsonld-id: http://modelcontextprotocol.io/ontology#maximum
      minimum:
        type: integer
        x-jsonld-id: http://modelcontextprotocol.io/ontology#minimum
      title:
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#title
      type:
        enum:
        - integer
        - number
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#type
    required:
    - type
    type: object
  PaginatedRequest:
    properties:
      method:
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#method
      params:
        properties:
          cursor:
            description: 'An opaque token representing the current pagination position.

              If provided, the server should return results starting after this cursor.'
            type: string
            x-jsonld-id: http://modelcontextprotocol.io/ontology#cursor
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#params
    required:
    - method
    type: object
  PaginatedResult:
    properties:
      _meta:
        additionalProperties: {}
        description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
          for notes on `_meta` usage.'
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
      nextCursor:
        description: 'An opaque token representing the pagination position after the
          last returned result.

          If present, there may be more results available.'
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#nextCursor
    type: object
  PingRequest:
    description: A ping, issued by either the server or the client, to check that
      the other party is still alive. The receiver must promptly respond, or else
      may be disconnected.
    properties:
      method:
        const: ping
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#method
      params:
        additionalProperties: {}
        properties:
          _meta:
            additionalProperties: {}
            description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
              for notes on `_meta` usage.'
            properties:
              progressToken:
                $ref: '#/definitions/ProgressToken'
                description: If specified, the caller is requesting out-of-band progress
                  notifications for this request (as represented by notifications/progress).
                  The value of this parameter is an opaque token that will be attached
                  to any subsequent notifications. The receiver is not obligated to
                  provide these notifications.
                x-jsonld-id: http://modelcontextprotocol.io/ontology#progressToken
            type: object
            x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#params
    required:
    - method
    type: object
  PrimitiveSchemaDefinition:
    anyOf:
    - $ref: '#/definitions/StringSchema'
    - $ref: '#/definitions/NumberSchema'
    - $ref: '#/definitions/BooleanSchema'
    - $ref: '#/definitions/EnumSchema'
    description: 'Restricted schema definitions that only allow primitive types

      without nested objects or arrays.'
  ProgressNotification:
    description: An out-of-band notification used to inform the receiver of a progress
      update for a long-running request.
    properties:
      method:
        const: notifications/progress
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#method
      params:
        properties:
          message:
            description: An optional message describing the current progress.
            type: string
            x-jsonld-id: http://modelcontextprotocol.io/ontology#message
          progress:
            description: The progress thus far. This should increase every time progress
              is made, even if the total is unknown.
            type: number
            x-jsonld-id: http://modelcontextprotocol.io/ontology#progress
          progressToken:
            $ref: '#/definitions/ProgressToken'
            description: The progress token which was given in the initial request,
              used to associate this notification with the request that is proceeding.
            x-jsonld-id: http://modelcontextprotocol.io/ontology#progressToken
          total:
            description: Total number of items to process (or total progress required),
              if known.
            type: number
            x-jsonld-id: http://modelcontextprotocol.io/ontology#total
        required:
        - progress
        - progressToken
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#params
    required:
    - method
    - params
    type: object
  Prompt:
    description: A prompt or prompt template that the server offers.
    properties:
      _meta:
        additionalProperties: {}
        description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
          for notes on `_meta` usage.'
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
      arguments:
        description: A list of arguments to use for templating the prompt.
        items:
          $ref: '#/definitions/PromptArgument'
        type: array
        x-jsonld-id: http://modelcontextprotocol.io/ontology#arguments
      description:
        description: An optional description of what this prompt provides
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#description
      name:
        description: Intended for programmatic or logical use, but used as a display
          name in past specs or fallback (if title isn't present).
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#name
      title:
        description: "Intended for UI and end-user contexts \u2014 optimized to be
          human-readable and easily understood,\neven by those unfamiliar with domain-specific
          terminology.\n\nIf not provided, the name should be used for display (except
          for Tool,\nwhere `annotations.title` should be given precedence over using
          `name`,\nif present)."
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#title
    required:
    - name
    type: object
  PromptArgument:
    description: Describes an argument that a prompt can accept.
    properties:
      description:
        description: A human-readable description of the argument.
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#description
      name:
        description: Intended for programmatic or logical use, but used as a display
          name in past specs or fallback (if title isn't present).
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#name
      required:
        description: Whether this argument must be provided.
        type: boolean
        x-jsonld-id: http://modelcontextprotocol.io/ontology#required
      title:
        description: "Intended for UI and end-user contexts \u2014 optimized to be
          human-readable and easily understood,\neven by those unfamiliar with domain-specific
          terminology.\n\nIf not provided, the name should be used for display (except
          for Tool,\nwhere `annotations.title` should be given precedence over using
          `name`,\nif present)."
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#title
    required:
    - name
    type: object
  PromptListChangedNotification:
    description: An optional notification from the server to the client, informing
      it that the list of prompts it offers has changed. This may be issued by servers
      without any previous subscription from the client.
    properties:
      method:
        const: notifications/prompts/list_changed
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#method
      params:
        additionalProperties: {}
        properties:
          _meta:
            additionalProperties: {}
            description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
              for notes on `_meta` usage.'
            type: object
            x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#params
    required:
    - method
    type: object
  PromptMessage:
    description: 'Describes a message returned as part of a prompt.


      This is similar to `SamplingMessage`, but also supports the embedding of

      resources from the MCP server.'
    properties:
      content:
        $ref: '#/definitions/ContentBlock'
        x-jsonld-id: http://modelcontextprotocol.io/ontology#content
      role:
        $ref: '#/definitions/Role'
        x-jsonld-id: http://modelcontextprotocol.io/ontology#role
    required:
    - content
    - role
    type: object
  PromptReference:
    description: Identifies a prompt.
    properties:
      name:
        description: Intended for programmatic or logical use, but used as a display
          name in past specs or fallback (if title isn't present).
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#name
      title:
        description: "Intended for UI and end-user contexts \u2014 optimized to be
          human-readable and easily understood,\neven by those unfamiliar with domain-specific
          terminology.\n\nIf not provided, the name should be used for display (except
          for Tool,\nwhere `annotations.title` should be given precedence over using
          `name`,\nif present)."
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#title
      type:
        const: ref/prompt
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#type
    required:
    - name
    - type
    type: object
  ReadResourceRequest:
    description: Sent from the client to the server, to read a specific resource URI.
    properties:
      method:
        const: resources/read
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#method
      params:
        properties:
          uri:
            description: The URI of the resource to read. The URI can use any protocol;
              it is up to the server how to interpret it.
            format: uri
            type: string
            x-jsonld-id: http://modelcontextprotocol.io/ontology#uri
        required:
        - uri
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#params
    required:
    - method
    - params
    type: object
  ReadResourceResult:
    description: The server's response to a resources/read request from the client.
    properties:
      _meta:
        additionalProperties: {}
        description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
          for notes on `_meta` usage.'
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
      contents:
        items:
          anyOf:
          - $ref: '#/definitions/TextResourceContents'
          - $ref: '#/definitions/BlobResourceContents'
        type: array
        x-jsonld-id: http://modelcontextprotocol.io/ontology#contents
    required:
    - contents
    type: object
  Request:
    properties:
      method:
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#method
      params:
        additionalProperties: {}
        properties:
          _meta:
            additionalProperties: {}
            description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
              for notes on `_meta` usage.'
            properties:
              progressToken:
                $ref: '#/definitions/ProgressToken'
                description: If specified, the caller is requesting out-of-band progress
                  notifications for this request (as represented by notifications/progress).
                  The value of this parameter is an opaque token that will be attached
                  to any subsequent notifications. The receiver is not obligated to
                  provide these notifications.
                x-jsonld-id: http://modelcontextprotocol.io/ontology#progressToken
            type: object
            x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#params
    required:
    - method
    type: object
  RequestId:
    description: A uniquely identifying ID for a request in JSON-RPC.
    type:
    - string
    - integer
  Resource:
    description: A known resource that the server is capable of reading.
    properties:
      _meta:
        additionalProperties: {}
        description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
          for notes on `_meta` usage.'
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
      annotations:
        $ref: '#/definitions/Annotations'
        description: Optional annotations for the client.
        x-jsonld-id: http://modelcontextprotocol.io/ontology#annotations
      description:
        description: 'A description of what this resource represents.


          This can be used by clients to improve the LLM''s understanding of available
          resources. It can be thought of like a "hint" to the model.'
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#description
      mimeType:
        description: The MIME type of this resource, if known.
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#mimeType
      name:
        description: Intended for programmatic or logical use, but used as a display
          name in past specs or fallback (if title isn't present).
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#name
      size:
        description: 'The size of the raw resource content, in bytes (i.e., before
          base64 encoding or any tokenization), if known.


          This can be used by Hosts to display file sizes and estimate context window
          usage.'
        type: integer
        x-jsonld-id: http://modelcontextprotocol.io/ontology#size
      title:
        description: "Intended for UI and end-user contexts \u2014 optimized to be
          human-readable and easily understood,\neven by those unfamiliar with domain-specific
          terminology.\n\nIf not provided, the name should be used for display (except
          for Tool,\nwhere `annotations.title` should be given precedence over using
          `name`,\nif present)."
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#title
      uri:
        description: The URI of this resource.
        format: uri
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#uri
    required:
    - name
    - uri
    type: object
  ResourceContents:
    description: The contents of a specific resource or sub-resource.
    properties:
      _meta:
        additionalProperties: {}
        description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
          for notes on `_meta` usage.'
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
      mimeType:
        description: The MIME type of this resource, if known.
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#mimeType
      uri:
        description: The URI of this resource.
        format: uri
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#uri
    required:
    - uri
    type: object
  ResourceLink:
    description: 'A resource that the server is capable of reading, included in a
      prompt or tool call result.


      Note: resource links returned by tools are not guaranteed to appear in the results
      of `resources/list` requests.'
    properties:
      _meta:
        additionalProperties: {}
        description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
          for notes on `_meta` usage.'
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
      annotations:
        $ref: '#/definitions/Annotations'
        description: Optional annotations for the client.
        x-jsonld-id: http://modelcontextprotocol.io/ontology#annotations
      description:
        description: 'A description of what this resource represents.


          This can be used by clients to improve the LLM''s understanding of available
          resources. It can be thought of like a "hint" to the model.'
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#description
      mimeType:
        description: The MIME type of this resource, if known.
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#mimeType
      name:
        description: Intended for programmatic or logical use, but used as a display
          name in past specs or fallback (if title isn't present).
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#name
      size:
        description: 'The size of the raw resource content, in bytes (i.e., before
          base64 encoding or any tokenization), if known.


          This can be used by Hosts to display file sizes and estimate context window
          usage.'
        type: integer
        x-jsonld-id: http://modelcontextprotocol.io/ontology#size
      title:
        description: "Intended for UI and end-user contexts \u2014 optimized to be
          human-readable and easily understood,\neven by those unfamiliar with domain-specific
          terminology.\n\nIf not provided, the name should be used for display (except
          for Tool,\nwhere `annotations.title` should be given precedence over using
          `name`,\nif present)."
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#title
      type:
        const: resource_link
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#type
      uri:
        description: The URI of this resource.
        format: uri
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#uri
    required:
    - name
    - type
    - uri
    type: object
  ResourceListChangedNotification:
    description: An optional notification from the server to the client, informing
      it that the list of resources it can read from has changed. This may be issued
      by servers without any previous subscription from the client.
    properties:
      method:
        const: notifications/resources/list_changed
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#method
      params:
        additionalProperties: {}
        properties:
          _meta:
            additionalProperties: {}
            description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
              for notes on `_meta` usage.'
            type: object
            x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#params
    required:
    - method
    type: object
  ResourceTemplate:
    description: A template description for resources available on the server.
    properties:
      _meta:
        additionalProperties: {}
        description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
          for notes on `_meta` usage.'
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
      annotations:
        $ref: '#/definitions/Annotations'
        description: Optional annotations for the client.
        x-jsonld-id: http://modelcontextprotocol.io/ontology#annotations
      description:
        description: 'A description of what this template is for.


          This can be used by clients to improve the LLM''s understanding of available
          resources. It can be thought of like a "hint" to the model.'
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#description
      mimeType:
        description: The MIME type for all resources that match this template. This
          should only be included if all resources matching this template have the
          same type.
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#mimeType
      name:
        description: Intended for programmatic or logical use, but used as a display
          name in past specs or fallback (if title isn't present).
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#name
      title:
        description: "Intended for UI and end-user contexts \u2014 optimized to be
          human-readable and easily understood,\neven by those unfamiliar with domain-specific
          terminology.\n\nIf not provided, the name should be used for display (except
          for Tool,\nwhere `annotations.title` should be given precedence over using
          `name`,\nif present)."
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#title
      uriTemplate:
        description: A URI template (according to RFC 6570) that can be used to construct
          resource URIs.
        format: uri-template
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#uriTemplate
    required:
    - name
    - uriTemplate
    type: object
  ResourceTemplateReference:
    description: A reference to a resource or resource template definition.
    properties:
      type:
        const: ref/resource
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#type
      uri:
        description: The URI or URI template of the resource.
        format: uri-template
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#uri
    required:
    - type
    - uri
    type: object
  ResourceUpdatedNotification:
    description: A notification from the server to the client, informing it that a
      resource has changed and may need to be read again. This should only be sent
      if the client previously sent a resources/subscribe request.
    properties:
      method:
        const: notifications/resources/updated
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#method
      params:
        properties:
          uri:
            description: The URI of the resource that has been updated. This might
              be a sub-resource of the one that the client actually subscribed to.
            format: uri
            type: string
            x-jsonld-id: http://modelcontextprotocol.io/ontology#uri
        required:
        - uri
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#params
    required:
    - method
    - params
    type: object
  Result:
    additionalProperties: {}
    properties:
      _meta:
        additionalProperties: {}
        description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
          for notes on `_meta` usage.'
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
    type: object
  Role:
    description: The sender or recipient of messages and data in a conversation.
    enum:
    - assistant
    - user
    type: string
  Root:
    description: Represents a root directory or file that the server can operate on.
    properties:
      _meta:
        additionalProperties: {}
        description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
          for notes on `_meta` usage.'
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
      name:
        description: 'An optional name for the root. This can be used to provide a
          human-readable

          identifier for the root, which may be useful for display purposes or for

          referencing the root in other parts of the application.'
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#name
      uri:
        description: 'The URI identifying the root. This *must* start with file://
          for now.

          This restriction may be relaxed in future versions of the protocol to allow

          other URI schemes.'
        format: uri
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#uri
    required:
    - uri
    type: object
  RootsListChangedNotification:
    description: 'A notification from the client to the server, informing it that
      the list of roots has changed.

      This notification should be sent whenever the client adds, removes, or modifies
      any root.

      The server should then request an updated list of roots using the ListRootsRequest.'
    properties:
      method:
        const: notifications/roots/list_changed
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#method
      params:
        additionalProperties: {}
        properties:
          _meta:
            additionalProperties: {}
            description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
              for notes on `_meta` usage.'
            type: object
            x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#params
    required:
    - method
    type: object
  SamplingMessage:
    description: Describes a message issued to or received from an LLM API.
    properties:
      content:
        anyOf:
        - $ref: '#/definitions/TextContent'
        - $ref: '#/definitions/ImageContent'
        - $ref: '#/definitions/AudioContent'
        x-jsonld-id: http://modelcontextprotocol.io/ontology#content
      role:
        $ref: '#/definitions/Role'
        x-jsonld-id: http://modelcontextprotocol.io/ontology#role
    required:
    - content
    - role
    type: object
  ServerCapabilities:
    description: 'Capabilities that a server may support. Known capabilities are defined
      here, in this schema, but this is not a closed set: any server can define its
      own, additional capabilities.'
    properties:
      completions:
        additionalProperties: true
        description: Present if the server supports argument autocompletion suggestions.
        properties: {}
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#completions
      experimental:
        additionalProperties:
          additionalProperties: true
          properties: {}
          type: object
        description: Experimental, non-standard capabilities that the server supports.
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#experimental
      logging:
        additionalProperties: true
        description: Present if the server supports sending log messages to the client.
        properties: {}
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#logging
      prompts:
        description: Present if the server offers any prompt templates.
        properties:
          listChanged:
            description: Whether this server supports notifications for changes to
              the prompt list.
            type: boolean
            x-jsonld-id: http://modelcontextprotocol.io/ontology#listChanged
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#prompts
      resources:
        description: Present if the server offers any resources to read.
        properties:
          listChanged:
            description: Whether this server supports notifications for changes to
              the resource list.
            type: boolean
            x-jsonld-id: http://modelcontextprotocol.io/ontology#listChanged
          subscribe:
            description: Whether this server supports subscribing to resource updates.
            type: boolean
            x-jsonld-id: http://modelcontextprotocol.io/ontology#subscribe
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#resources
      tools:
        description: Present if the server offers any tools to call.
        properties:
          listChanged:
            description: Whether this server supports notifications for changes to
              the tool list.
            type: boolean
            x-jsonld-id: http://modelcontextprotocol.io/ontology#listChanged
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#tools
    type: object
  ServerNotification:
    anyOf:
    - $ref: '#/definitions/CancelledNotification'
    - $ref: '#/definitions/ProgressNotification'
    - $ref: '#/definitions/ResourceListChangedNotification'
    - $ref: '#/definitions/ResourceUpdatedNotification'
    - $ref: '#/definitions/PromptListChangedNotification'
    - $ref: '#/definitions/ToolListChangedNotification'
    - $ref: '#/definitions/LoggingMessageNotification'
  ServerRequest:
    anyOf:
    - $ref: '#/definitions/PingRequest'
    - $ref: '#/definitions/CreateMessageRequest'
    - $ref: '#/definitions/ListRootsRequest'
    - $ref: '#/definitions/ElicitRequest'
  ServerResult:
    anyOf:
    - $ref: '#/definitions/Result'
    - $ref: '#/definitions/InitializeResult'
    - $ref: '#/definitions/ListResourcesResult'
    - $ref: '#/definitions/ListResourceTemplatesResult'
    - $ref: '#/definitions/ReadResourceResult'
    - $ref: '#/definitions/ListPromptsResult'
    - $ref: '#/definitions/GetPromptResult'
    - $ref: '#/definitions/ListToolsResult'
    - $ref: '#/definitions/CallToolResult'
    - $ref: '#/definitions/CompleteResult'
  SetLevelRequest:
    description: A request from the client to the server, to enable or adjust logging.
    properties:
      method:
        const: logging/setLevel
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#method
      params:
        properties:
          level:
            $ref: '#/definitions/LoggingLevel'
            description: The level of logging that the client wants to receive from
              the server. The server should send all logs at this level and higher
              (i.e., more severe) to the client as notifications/message.
            x-jsonld-id: http://modelcontextprotocol.io/ontology#level
        required:
        - level
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#params
    required:
    - method
    - params
    type: object
  StringSchema:
    properties:
      description:
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#description
      format:
        enum:
        - date
        - date-time
        - email
        - uri
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#format
      maxLength:
        type: integer
        x-jsonld-id: http://modelcontextprotocol.io/ontology#maxLength
      minLength:
        type: integer
        x-jsonld-id: http://modelcontextprotocol.io/ontology#minLength
      title:
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#title
      type:
        const: string
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#type
    required:
    - type
    type: object
  SubscribeRequest:
    description: Sent from the client to request resources/updated notifications from
      the server whenever a particular resource changes.
    properties:
      method:
        const: resources/subscribe
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#method
      params:
        properties:
          uri:
            description: The URI of the resource to subscribe to. The URI can use
              any protocol; it is up to the server how to interpret it.
            format: uri
            type: string
            x-jsonld-id: http://modelcontextprotocol.io/ontology#uri
        required:
        - uri
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#params
    required:
    - method
    - params
    type: object
  TextContent:
    description: Text provided to or from an LLM.
    properties:
      _meta:
        additionalProperties: {}
        description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
          for notes on `_meta` usage.'
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
      annotations:
        $ref: '#/definitions/Annotations'
        description: Optional annotations for the client.
        x-jsonld-id: http://modelcontextprotocol.io/ontology#annotations
      text:
        description: The text content of the message.
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#text
      type:
        const: text
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#type
    required:
    - text
    - type
    type: object
  TextResourceContents:
    properties:
      _meta:
        additionalProperties: {}
        description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
          for notes on `_meta` usage.'
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
      mimeType:
        description: The MIME type of this resource, if known.
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#mimeType
      text:
        description: The text of the item. This must only be set if the item can actually
          be represented as text (not binary data).
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#text
      uri:
        description: The URI of this resource.
        format: uri
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#uri
    required:
    - text
    - uri
    type: object
  Tool:
    description: Definition for a tool the client can call.
    properties:
      _meta:
        additionalProperties: {}
        description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
          for notes on `_meta` usage.'
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
      annotations:
        $ref: '#/definitions/ToolAnnotations'
        description: 'Optional additional tool information.


          Display name precedence order is: title, annotations.title, then name.'
        x-jsonld-id: http://modelcontextprotocol.io/ontology#annotations
      description:
        description: 'A human-readable description of the tool.


          This can be used by clients to improve the LLM''s understanding of available
          tools. It can be thought of like a "hint" to the model.'
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#description
      inputSchema:
        description: A JSON Schema object defining the expected parameters for the
          tool.
        properties:
          properties:
            additionalProperties:
              additionalProperties: true
              properties: {}
              type: object
            type: object
            x-jsonld-id: http://modelcontextprotocol.io/ontology#properties
          required:
            items:
              type: string
            type: array
            x-jsonld-id: http://modelcontextprotocol.io/ontology#required
          type:
            const: object
            type: string
            x-jsonld-id: http://modelcontextprotocol.io/ontology#type
        required:
        - type
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#inputSchema
      name:
        description: Intended for programmatic or logical use, but used as a display
          name in past specs or fallback (if title isn't present).
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#name
      outputSchema:
        description: 'An optional JSON Schema object defining the structure of the
          tool''s output returned in

          the structuredContent field of a CallToolResult.'
        properties:
          properties:
            additionalProperties:
              additionalProperties: true
              properties: {}
              type: object
            type: object
            x-jsonld-id: http://modelcontextprotocol.io/ontology#properties
          required:
            items:
              type: string
            type: array
            x-jsonld-id: http://modelcontextprotocol.io/ontology#required
          type:
            const: object
            type: string
            x-jsonld-id: http://modelcontextprotocol.io/ontology#type
        required:
        - type
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#outputSchema
      title:
        description: "Intended for UI and end-user contexts \u2014 optimized to be
          human-readable and easily understood,\neven by those unfamiliar with domain-specific
          terminology.\n\nIf not provided, the name should be used for display (except
          for Tool,\nwhere `annotations.title` should be given precedence over using
          `name`,\nif present)."
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#title
    required:
    - inputSchema
    - name
    type: object
  ToolAnnotations:
    description: 'Additional properties describing a Tool to clients.


      NOTE: all properties in ToolAnnotations are **hints**.

      They are not guaranteed to provide a faithful description of

      tool behavior (including descriptive properties like `title`).


      Clients should never make tool use decisions based on ToolAnnotations

      received from untrusted servers.'
    properties:
      destructiveHint:
        description: 'If true, the tool may perform destructive updates to its environment.

          If false, the tool performs only additive updates.


          (This property is meaningful only when `readOnlyHint == false`)


          Default: true'
        type: boolean
        x-jsonld-id: http://modelcontextprotocol.io/ontology#destructiveHint
      idempotentHint:
        description: 'If true, calling the tool repeatedly with the same arguments

          will have no additional effect on the its environment.


          (This property is meaningful only when `readOnlyHint == false`)


          Default: false'
        type: boolean
        x-jsonld-id: http://modelcontextprotocol.io/ontology#idempotentHint
      openWorldHint:
        description: 'If true, this tool may interact with an "open world" of external

          entities. If false, the tool''s domain of interaction is closed.

          For example, the world of a web search tool is open, whereas that

          of a memory tool is not.


          Default: true'
        type: boolean
        x-jsonld-id: http://modelcontextprotocol.io/ontology#openWorldHint
      readOnlyHint:
        description: 'If true, the tool does not modify its environment.


          Default: false'
        type: boolean
        x-jsonld-id: http://modelcontextprotocol.io/ontology#readOnlyHint
      title:
        description: A human-readable title for the tool.
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#title
    type: object
  ToolListChangedNotification:
    description: An optional notification from the server to the client, informing
      it that the list of tools it offers has changed. This may be issued by servers
      without any previous subscription from the client.
    properties:
      method:
        const: notifications/tools/list_changed
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#method
      params:
        additionalProperties: {}
        properties:
          _meta:
            additionalProperties: {}
            description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
              for notes on `_meta` usage.'
            type: object
            x-jsonld-id: http://modelcontextprotocol.io/ontology#_meta
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#params
    required:
    - method
    type: object
  UnsubscribeRequest:
    description: Sent from the client to request cancellation of resources/updated
      notifications from the server. This should follow a previous resources/subscribe
      request.
    properties:
      method:
        const: resources/unsubscribe
        type: string
        x-jsonld-id: http://modelcontextprotocol.io/ontology#method
      params:
        properties:
          uri:
            description: The URI of the resource to unsubscribe from.
            format: uri
            type: string
            x-jsonld-id: http://modelcontextprotocol.io/ontology#uri
        required:
        - uri
        type: object
        x-jsonld-id: http://modelcontextprotocol.io/ontology#params
    required:
    - method
    - params
    type: object
x-jsonld-vocab: http://modelcontextprotocol.io/ontology#
x-jsonld-prefixes:
  mcp: http://modelcontextprotocol.io/ontology#
  xsd: http://www.w3.org/2001/XMLSchema#
  rdfs: http://www.w3.org/2000/01/rdf-schema#

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/modelcontextprotocol/build/annotated/mcp/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/modelcontextprotocol/build/annotated/mcp/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@vocab": "http://modelcontextprotocol.io/ontology#",
    "mcp": "http://modelcontextprotocol.io/ontology#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/modelcontextprotocol/build/annotated/mcp/context.jsonld)

## Sources

* [Model Context Protocol](https://modelcontextprotocol.io/specification/2025-06-18)
* [Model Context Protocol schema](https://raw.githubusercontent.com/modelcontextprotocol/modelcontextprotocol/refs/heads/main/schema/2025-06-18/schema.json)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/modelcontextprotocol](https://github.com/ogcincubator/modelcontextprotocol)
* Path: `_sources/mcp`

