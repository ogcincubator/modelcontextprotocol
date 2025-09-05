
# JSON-RPC (Model)

`ogc.bbr.template.json-rpc` *v2.0.0*

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

Note the JSON-LD enabled of the RPC elements is necessary to build a graph out of a JSON MCP object - it supports RDF identifiers of the object containers, which then allows MCP components to be mapped to RDF models

## Usage


## Validation

Validation of examples is implemented using the JSON schema

At this stage no additional semantic rules have been defined.

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/modelcontextprotocol](https://github.com/ogcincubator/modelcontextprotocol)
* Path: `_sources/json-rpc`

