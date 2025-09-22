
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
@prefix jrpc: <http://json-rpc.org/ontology#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] jrpc:hasId <https://override-me-for-custom-content.eg/1> ;
    jrpc:hasMethod "subtract"^^xsd:string ;
    jrpc:hasParameters "{\"p1\":42,\"p2\":23}"^^rdf:JSON ;
    jrpc:version "2.0"^^xsd:string .


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
@prefix jrpc: <http://json-rpc.org/ontology#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] jrpc:hasId <https://override-me-for-custom-content.eg/1> ;
    jrpc:hasMethod "subtract"^^xsd:string ;
    jrpc:hasParameters "{\"minuend\":42,\"subtrahend\":23}"^^rdf:JSON ;
    jrpc:version "2.0"^^xsd:string .


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
@prefix jrpc: <http://json-rpc.org/ontology#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] jrpc:hasId <https://override-me-for-custom-content.eg/1> ;
    jrpc:hasResult "{\"value\":19}"^^rdf:JSON ;
    jrpc:version "2.0"^^xsd:string .


```

## Schema

```yaml
$schema: http://json-schema.org/draft-07/schema#
$defs:
  JSONRPC2Object:
    type: object
    required:
    - jsonrpc
    properties:
      jsonrpc:
        const: '2.0'
        x-jsonld-id: http://json-rpc.org/ontology#version
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
  IDObject:
    allOf:
    - $ref: '#/$defs/JSONRPC2Object'
    - type: object
      properties:
        id:
          type:
          - string
          - integer
          - 'null'
          x-jsonld-id: http://json-rpc.org/ontology#hasId
          x-jsonld-type: '@id'
  ErrorObject:
    type: object
    required:
    - code
    - message
    properties:
      code:
        type: integer
        x-jsonld-id: http://json-rpc.org/ontology#hasErrorCode
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#integer
      message:
        type: string
        x-jsonld-id: http://json-rpc.org/ontology#hasErrorMessage
        x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
      data:
        x-jsonld-id: http://json-rpc.org/ontology#hasErrorData
        x-jsonld-type: '@json'
  Notification:
    $anchor: Notification
    allOf:
    - $ref: '#/$defs/JSONRPC2Object'
    - type: object
      required:
      - method
      properties:
        method:
          type: string
          x-jsonld-id: http://json-rpc.org/ontology#hasMethod
          x-jsonld-type: http://www.w3.org/2001/XMLSchema#string
        params:
          type:
          - object
          - array
          x-jsonld-id: http://json-rpc.org/ontology#hasParameters
          x-jsonld-type: '@json'
  Request:
    $anchor: Request
    allOf:
    - $ref: '#/$defs/IDObject'
    - $ref: '#/$defs/Notification'
  Response:
    $anchor: Response
    allOf:
    - $ref: '#/$defs/IDObject'
    - oneOf:
      - required:
        - result
        properties:
          result:
            x-jsonld-id: http://json-rpc.org/ontology#hasResult
            x-jsonld-type: '@json'
      - required:
        - error
        properties:
          error:
            $ref: '#/$defs/ErrorObject'
            x-jsonld-id: http://json-rpc.org/ontology#hasError
            x-jsonld-type: '@id'
  BatchRequest:
    $anchor: BatchRequest
    type: array
    items:
      $ref: '#/$defs/Request'
  BatchResponse:
    $anchor: BatchResponse
    type: array
    items:
      $ref: '#/$defs/Response'
oneOf:
- $ref: '#/$defs/Request'
- $ref: '#/$defs/Notification'
- $ref: '#/$defs/Response'
- $ref: '#/$defs/BatchRequest'
- $ref: '#/$defs/BatchResponse'
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
    "jsonrpc": {
      "@id": "jrpc:version",
      "@type": "xsd:string"
    },
    "id": {
      "@id": "jrpc:hasId",
      "@type": "@id"
    },
    "method": {
      "@id": "jrpc:hasMethod",
      "@type": "xsd:string"
    },
    "params": {
      "@id": "jrpc:hasParameters",
      "@type": "@json"
    },
    "result": {
      "@id": "jrpc:hasResult",
      "@type": "@json"
    },
    "error": {
      "@context": {
        "code": {
          "@id": "jrpc:hasErrorCode",
          "@type": "xsd:integer"
        },
        "message": {
          "@id": "jrpc:hasErrorMessage",
          "@type": "xsd:string"
        },
        "data": {
          "@id": "jrpc:hasErrorData",
          "@type": "@json"
        }
      },
      "@id": "jrpc:hasError",
      "@type": "@id"
    },
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

