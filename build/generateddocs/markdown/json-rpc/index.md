
# JSON-RPC (Model)

`mcp.json-rpc` *v2.0.0*

None

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# JSON-RPC

This BBlock implements the JSON-RPC specification as reusable ontology and JSON schema linked with a JSON-LD context.


## Purpose

- To support a modular descriptions of the Model Context Protocol and any other JSON-RPC based approaches

## Contents

- `schema.json`: JSON schema for the JSON-RPC specification
- `ontology.ttl`: Ontology terms for the JSON-RPC container objects
- `bblock.json` / `bblock.yaml`: BBlock registration metadata.
- `context.jsonld`: JSON-LD context for the RPC model
- `examples.ttl`:  Register of examples mapped to specific sub-schema elements.

## Status

There is no official schema for JSON-RPC or the Model Context Protocol that uses it - unofficial schemas tend to bundle the JSON-RPC elements into the MCP schema, which hides the dependencies, reduces re-usability and obscures testing.

Note the JSON-LD enabled of the RPC elements is necessary to build a graph out of a JSON MCP object - it supports RDF identifiers of the object containers, which then allows MCP components to be mapped to RDF models.

## Usage


## Validation

Validation of examples is implemented using the JSON schema

At this stage no additional semantic rules have been defined.
## Examples

### Call (positional params)
#### json
```json
{"jsonrpc": "2.0", "method": "subtract", "params": {"p1": 42, "p2": 23}, "id": "1"}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "mydata": "http://example.com/rpc/"
    },
    "https://ogcincubator.github.io/modelcontextprotocol/build/annotated/json-rpc/context.jsonld"
  ],
  "jsonrpc": "2.0",
  "method": "subtract",
  "params": {
    "p1": 42,
    "p2": 23
  },
  "id": "1"
}
```

#### ttl
```ttl


```


### Call (named params)
#### json
```json
{"jsonrpc": "2.0", "method": "subtract",  "params": {"subtrahend": 23, "minuend": 42}, "id": "1"}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "mydata": "http://example.com/rpc/"
    },
    "https://ogcincubator.github.io/modelcontextprotocol/build/annotated/json-rpc/context.jsonld"
  ],
  "jsonrpc": "2.0",
  "method": "subtract",
  "params": {
    "subtrahend": 23,
    "minuend": 42
  },
  "id": "1"
}
```

#### ttl
```ttl


```


### Response
#### json
```json
{"jsonrpc": "2.0", "result": {"value": 19}, "id": "1"}
```

#### jsonld
```jsonld
{
  "@context": [
    {
      "mydata": "http://example.com/rpc/"
    },
    "https://ogcincubator.github.io/modelcontextprotocol/build/annotated/json-rpc/context.jsonld"
  ],
  "jsonrpc": "2.0",
  "result": {
    "value": 19
  },
  "id": "1"
}
```

#### ttl
```ttl


```

## Schema

```yaml
$schema: http://json-schema.org/draft-07/schema#
definitions:
  jsonrpc:
    $anchor: jsonrpc
    description: JSON-RPC version
    const: '2.0'
    type: string
  RequestId:
    $anchor: RequestId
    description: A uniquely identifying ID for a request in JSON-RPC.
    type:
    - string
  ProgressToken:
    $anchor: ProgressToken
    description: A progress token, used to associate progress notifications with the
      original request.
    type:
    - string
  Request:
    $anchor: Request
    properties:
      method:
        type: string
        x-jsonld-id: http://json-rpc.org/ontology#hasMethod
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
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
            type: object
        type: object
        x-jsonld-id: http://json-rpc.org/ontology#hasParameters
        x-jsonld-type: '@json'
    required:
    - method
    type: object
  Result:
    $anchor: Result
    additionalProperties: {}
    properties:
      _meta:
        additionalProperties: {}
        description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
          for notes on `_meta` usage.'
        type: object
    type: object
  JSONRPCError:
    $anchor: JSONRPCError
    description: A response to a request that indicates an error occurred.
    properties:
      error:
        properties:
          code:
            description: The error type that occurred.
            type: integer
            x-jsonld-id: http://json-rpc.org/ontology#hasErrorCode
            x-jsonld-type: http://www.w3.org/2001/XMLSchema#integer
          data:
            description: Additional information about the error. The value of this
              member is defined by the sender (e.g. detailed error information, nested
              errors etc.).
            x-jsonld-id: http://json-rpc.org/ontology#hasErrorData
            x-jsonld-type: '@json'
          message:
            description: A short description of the error. The message SHOULD be limited
              to a concise single sentence.
            type: string
            x-jsonld-id: http://json-rpc.org/ontology#hasErrorMessage
            x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
        required:
        - code
        - message
        type: object
        x-jsonld-id: http://json-rpc.org/ontology#hasError
        x-jsonld-type: '@id'
      id:
        $ref: '#/definitions/RequestId'
        x-jsonld-id: http://json-rpc.org/ontology#hasId
        x-jsonld-type: '@id'
      jsonrpc:
        $ref: '#/definitions/jsonrpc'
        x-jsonld-id: http://json-rpc.org/ontology#version
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
    required:
    - error
    - id
    - jsonrpc
    type: object
  JSONRPCMessage:
    $anchor: JSONRPCMessage
    anyOf:
    - $ref: '#/definitions/JSONRPCRequest'
    - $ref: '#/definitions/JSONRPCNotification'
    - $ref: '#/definitions/JSONRPCResponse'
    - $ref: '#/definitions/JSONRPCError'
    description: Refers to any valid JSON-RPC object that can be decoded off the wire,
      or encoded to be sent.
  JSONRPCNotification:
    $anchor: JSONRPCNotification
    description: A notification which does not expect a response.
    properties:
      jsonrpc:
        $ref: '#/definitions/jsonrpc'
        x-jsonld-id: http://json-rpc.org/ontology#version
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
      method:
        type: string
        x-jsonld-id: http://json-rpc.org/ontology#hasMethod
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
      params:
        additionalProperties: {}
        properties:
          _meta:
            additionalProperties: {}
            description: 'See [General fields: `_meta`](/specification/2025-06-18/basic/index#meta)
              for notes on `_meta` usage.'
            type: object
        type: object
        x-jsonld-id: http://json-rpc.org/ontology#hasParameters
        x-jsonld-type: '@json'
    required:
    - jsonrpc
    - method
    type: object
  JSONRPCRequest:
    $anchor: JSONRPCRequest
    description: A request that expects a response.
    properties:
      id:
        $ref: '#/definitions/RequestId'
        x-jsonld-id: http://json-rpc.org/ontology#hasId
        x-jsonld-type: '@id'
      jsonrpc:
        $ref: '#/definitions/jsonrpc'
        x-jsonld-id: http://json-rpc.org/ontology#version
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
      method:
        type: string
        x-jsonld-id: http://json-rpc.org/ontology#hasMethod
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
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
            type: object
        type: object
        x-jsonld-id: http://json-rpc.org/ontology#hasParameters
        x-jsonld-type: '@json'
    required:
    - id
    - jsonrpc
    - method
    type: object
  JSONRPCResponse:
    $anchor: JSONRPCResponse
    description: A successful (non-error) response to a request.
    properties:
      id:
        $ref: '#/definitions/RequestId'
        x-jsonld-id: http://json-rpc.org/ontology#hasId
        x-jsonld-type: '@id'
      jsonrpc:
        $ref: '#/definitions/jsonrpc'
        x-jsonld-id: http://json-rpc.org/ontology#version
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
      result:
        $ref: '#/definitions/Result'
        x-jsonld-id: http://json-rpc.org/ontology#hasResult
        x-jsonld-type: '@json'
    required:
    - id
    - jsonrpc
    - result
    type: object
x-jsonld-extra-terms:
  Message:
    x-jsonld-id: http://json-rpc.org/ontology#Message
    x-jsonld-type: '@id'
  Request:
    x-jsonld-id: http://json-rpc.org/ontology#Request
    x-jsonld-type: '@id'
  Notification:
    x-jsonld-id: http://json-rpc.org/ontology#Notification
    x-jsonld-type: '@id'
  Response:
    x-jsonld-id: http://json-rpc.org/ontology#Response
    x-jsonld-type: '@id'
  ErrorResponse:
    x-jsonld-id: http://json-rpc.org/ontology#ErrorResponse
    x-jsonld-type: '@id'
  Error:
    x-jsonld-id: http://json-rpc.org/ontology#Error
    x-jsonld-type: '@id'
  RequestId:
    x-jsonld-id: http://json-rpc.org/ontology#RequestId
    x-jsonld-type: '@id'
  StringId:
    x-jsonld-id: http://json-rpc.org/ontology#StringId
    x-jsonld-type: '@id'
  NumberId:
    x-jsonld-id: http://json-rpc.org/ontology#NumberId
    x-jsonld-type: '@id'
  NullId:
    x-jsonld-id: http://json-rpc.org/ontology#NullId
    x-jsonld-type: '@id'
  stringValue:
    x-jsonld-id: http://json-rpc.org/ontology#hasStringValue
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  numberValue:
    x-jsonld-id: http://json-rpc.org/ontology#hasNumberValue
    x-jsonld-type: http://www.w3.org/2001/XMLSchema#decimal
  ParseError:
    x-jsonld-id: http://json-rpc.org/ontology#ParseError
    x-jsonld-type: '@id'
  InvalidRequest:
    x-jsonld-id: http://json-rpc.org/ontology#InvalidRequest
    x-jsonld-type: '@id'
  MethodNotFound:
    x-jsonld-id: http://json-rpc.org/ontology#MethodNotFound
    x-jsonld-type: '@id'
  InvalidParams:
    x-jsonld-id: http://json-rpc.org/ontology#InvalidParams
    x-jsonld-type: '@id'
  InternalError:
    x-jsonld-id: http://json-rpc.org/ontology#InternalError
    x-jsonld-type: '@id'
  ServerError:
    x-jsonld-id: http://json-rpc.org/ontology#ServerError
    x-jsonld-type: '@id'
x-jsonld-base: https://override-me-for-custom-content.eg/
x-jsonld-prefixes:
  jrpc: http://json-rpc.org/ontology#
  xsd: http://www.w3.org/2001/XMLSchema#
  x@vocab: http://json-rpc.org/ontology#
  rdfs: http://www.w3.org/2000/01/rdf-schema#

```

Links to the schema:

* YAML version: [schema.yaml](https://ogcincubator.github.io/modelcontextprotocol/build/annotated/json-rpc/schema.json)
* JSON version: [schema.json](https://ogcincubator.github.io/modelcontextprotocol/build/annotated/json-rpc/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "@base": "https://override-me-for-custom-content.eg/",
    "Message": {
      "@id": "jrpc:Message",
      "@type": "@id"
    },
    "Request": {
      "@id": "jrpc:Request",
      "@type": "@id"
    },
    "Notification": {
      "@id": "jrpc:Notification",
      "@type": "@id"
    },
    "Response": {
      "@id": "jrpc:Response",
      "@type": "@id"
    },
    "ErrorResponse": {
      "@id": "jrpc:ErrorResponse",
      "@type": "@id"
    },
    "Error": {
      "@id": "jrpc:Error",
      "@type": "@id"
    },
    "RequestId": {
      "@id": "jrpc:RequestId",
      "@type": "@id"
    },
    "StringId": {
      "@id": "jrpc:StringId",
      "@type": "@id"
    },
    "NumberId": {
      "@id": "jrpc:NumberId",
      "@type": "@id"
    },
    "NullId": {
      "@id": "jrpc:NullId",
      "@type": "@id"
    },
    "stringValue": {
      "@id": "jrpc:hasStringValue",
      "@type": "xsd:string"
    },
    "numberValue": {
      "@id": "jrpc:hasNumberValue",
      "@type": "xsd:decimal"
    },
    "ParseError": {
      "@id": "jrpc:ParseError",
      "@type": "@id"
    },
    "InvalidRequest": {
      "@id": "jrpc:InvalidRequest",
      "@type": "@id"
    },
    "MethodNotFound": {
      "@id": "jrpc:MethodNotFound",
      "@type": "@id"
    },
    "InvalidParams": {
      "@id": "jrpc:InvalidParams",
      "@type": "@id"
    },
    "InternalError": {
      "@id": "jrpc:InternalError",
      "@type": "@id"
    },
    "ServerError": {
      "@id": "jrpc:ServerError",
      "@type": "@id"
    },
    "jrpc": "http://json-rpc.org/ontology#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "x@vocab": "http://json-rpc.org/ontology#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://ogcincubator.github.io/modelcontextprotocol/build/annotated/json-rpc/context.jsonld)


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/modelcontextprotocol](https://github.com/ogcincubator/modelcontextprotocol)
* Path: `_sources/json-rpc`

